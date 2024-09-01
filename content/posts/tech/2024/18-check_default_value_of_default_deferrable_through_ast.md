Title: Building a Customized Linter
Subtitle: Checking the Default Value of default_deferrable through AST
Date: 2024-09-01 19:15
Category: Tech
Tags: Python, Airflow, Airflow 2.7, AST
Slug: check_default_value_of_default_deferrable_through_ast
Authors: Wei Lee
Series: Unleash the Chaos: Developing a Linter for Un-Pythonic Code!
Cover: /images/posts-image/2024-check_default_value_of_default_deferrable_through_ast/surely-you-can-do-better.jpg

In the previous article, I mentioned that we can only kindly ask users to add the default value of deferrable correctly. But... the fact is we can do better.

<!--more-->

![surely-you-can-do-better](/images/posts-image/2024-check_default_value_of_default_deferrable_through_ast/surely-you-can-do-better.jpg)

[TOC]

## What can we do?

There may not be an existing linter that we can configure to check this default value, so we'll need to create our own customized linter. The good news is that we already have some in Airflow. It shouldn't be too difficult for me to add one. The pull request that included this change was [build(pre-commit): check deferrable default value #32370](https://github.com/apache/airflow/pull/32370/). I added `scripts/ci/pre_commit/pre_commit_check_deferrable_default.py` so that if anyone is pushing an operator with the wrong `deferrable` default value, it will be blocked by this pre-commit hook. (Looks like this file has later be renamed as [scripts/ci/pre_commit/check_deferrable_default.py](https://github.com/apache/airflow/blob/725a9b6cabcf8b6814de883db361eca6f58fd16b/scripts/ci/pre_commit/check_deferrable_default.py) 👀)

## Let's formalize our goal
If the argument `deferrable` is present in the `__init__` method of any of the operators, its default value should be set as `conf.getboolean("operators", "default_deferrable", fallback=False)`.

For instance, having an operator without a `deferrable` argument is okay.

```python
from airflow.models.baseoperator import BaseOperator


class ExampleOperator(BaseOperator):
    def __init__(self, *, **kwargs) -> None:
        super().__init__(**kwargs)
```

However, if an operator includes a `deferrable` argument without a default value or with a default value other than `conf.getboolean("operators", "default_deferrable", fallback=False)`, we need to raise a warning.

```python
from airflow.models.baseoperator import BaseOperator


class ExampleOperator(BaseOperator):
    def __init__(self, *, deferrable=False, **kwargs) -> None:
        super().__init__(**kwargs)
```

## Let's build the linter with ast
[ast](https://docs.python.org/3/library/ast.html) is a built-in Python module that can parse Python code into an abstract syntax tree. I won't go into depth here; that's a post for another day. We'll only discuss `ast.parse` and `ast.iter_child_nodes` here. Airflow already uses `ast` for this kind of checking in various places.

### Search for candidate modules
We already know that all the operators (including sensors), whether they are in the core or in the providers, will be put under `operators` or `sensors` directories. So we first iterate all the modules we need to check [here](https://github.com/apache/airflow/blob/725a9b6cabcf8b6814de883db361eca6f58fd16b/scripts/ci/pre_commit/check_deferrable_default.py#L88-L93).

```python
modules = itertools.chain(
    glob.glob(f"{ROOT_DIR}/airflow/**/sensors/**.py", recursive=True),
    glob.glob(f"{ROOT_DIR}/airflow/**/operators/**.py", recursive=True),
)

errors = [error for module in modules for error in iter_check_deferrable_default_errors(module)]
```

### Parse the modules into an abstract syntax tree
Then, we pass the module names to `iter_check_deferrable_default_errors` [function](https://github.com/apache/airflow/blob/725a9b6cabcf8b6814de883db361eca6f58fd16b/scripts/ci/pre_commit/check_deferrable_default.py#L65-L84). It parses the module into abstract syntax tree through `ast.parse`.

```python
def iter_check_deferrable_default_errors(module_filename: str) -> Iterator[str]:
    ast_obj = ast.parse(open(module_filename).read())
    ...
```

Before delving further into the function, let's consider the functionality of `ast.parse` in the simple case we used earlier (the string in the `ast.parse` function). Additionally, we utilize `ast.dump` to create a visual representation of the ast, making it easier to read.

```python
import ast

print(
    ast.dump(
        ast.parse(
            "from airflow.models.baseoperator import BaseOperator\n\n\nclass ExampleOperator(BaseOperator):\n    def __init__(self, *, deferrable=False, **kwargs) -> None:\n        super().__init__(**kwargs)\n"
        ),
        indent=4,
    )
)
```

Even for a simple case like this, the generated AST is already quite large.

```python
Module(
    body=[
        ImportFrom(
            module="airflow.models.baseoperator",
            names=[alias(name="BaseOperator")],
            level=0,
        ),
        ClassDef(
            name="ExampleOperator",
            bases=[Name(id="BaseOperator", ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name="__init__",
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg="self")],
                        kwonlyargs=[arg(arg="deferrable")],
                        kw_defaults=[Constant(value=False)],
                        kwarg=arg(arg="kwargs"),
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id="super", ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr="__init__",
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[keyword(value=Name(id="kwargs", ctx=Load()))],
                            )
                        )
                    ],
                    decorator_list=[],
                    returns=Constant(value=None),
                    type_params=[],
                )
            ],
            decorator_list=[],
            type_params=[],
        ),
    ],
    type_ignores=[],
)
```

### Find the `__init__` methods in the operators
After reading this AST, we can already guess how to obtain the arguments to check. First, we use `ast.iter_child_nodes` to list all the top-level child nodes and filter out the ones with class definitions (i.e., `isinstance(node, ast.ClassDef)`). Then, we filter out those functions with the name `__init__` (i.e., `if isinstance(node, ast.FunctionDef) and node.name == "__init__"`).

```python
def iter_check_deferrable_default_errors(module_filename: str) -> Iterator[str]:
    ...
    cls_nodes = (node for node in ast.iter_child_nodes(ast_obj) if isinstance(node, ast.ClassDef))
    init_method_nodes = (
        node
        for cls_node in cls_nodes
        for node in ast.iter_child_nodes(cls_node)
        if isinstance(node, ast.FunctionDef) and node.name == "__init__"
    )
    ...
```

### Filter out the arguments and their default values
After finding the init methods, we loop through these nodes and search for their arguments. As arguments **with** defaults always comes after those **without**
ones, we reverse the order [here](https://github.com/apache/airflow/blob/725a9b6cabcf8b6814de883db361eca6f58fd16b/scripts/ci/pre_commit/check_deferrable_default.py#L75-L84) and zip the arguments and defaults together.

```python
def iter_check_deferrable_default_errors(module_filename: str) -> Iterator[str]:
    ...
    for node in init_method_nodes:
        args = node.args
        arguments = reversed([*args.args, *args.kwonlyargs])
        defaults = reversed([*args.defaults, *args.kw_defaults])
        for argument, default in zip(arguments, defaults):
            if argument is None or default is None:
                continue
            if argument.arg != "deferrable" or _is_valid_deferrable_default(default):
                continue
            yield f"{module_filename}:{default.lineno}"
```

### Validate the default value

This is the final part of the script. We now check if the default value is an `ast.Call` (i.e., `conf.getboolean(...)`). The identifier (id) should be `conf` and the attribute (attr) should be `getboolean`. If this check passes, we will proceed to examine the argument of this call (i.g., `"operators", "default_deferrable", fallback=False`).

```python
def _is_valid_deferrable_default(default: ast.AST) -> bool:
    """Check whether default is 'conf.getboolean("operators", "default_deferrable", fallback=False)'"""
    if not isinstance(default, ast.Call):
        return False  # Not a function call.

    # Check the function callee is exactly 'conf.getboolean'.
    call_to_conf_getboolean = (
        isinstance(default.func, ast.Attribute)
        and isinstance(default.func.value, ast.Name)
        and default.func.value.id == "conf"
        and default.func.attr == "getboolean"
    )
    if not call_to_conf_getboolean:
        return False

    # Check arguments.
    return (
        len(default.args) == 2
        and isinstance(default.args[0], ast.Constant)
        and default.args[0].value == "operators"
        and isinstance(default.args[1], ast.Constant)
        and default.args[1].value == "default_deferrable"
        and len(default.keywords) == 1
        and default.keywords[0].arg == "fallback"
        and isinstance(default.keywords[0].value, ast.Constant)
        and default.keywords[0].value.value is False
    )
```

## Conclusion
After introducing this check, many deferrable operators were added, and none came without `deferrable = conf.getboolean("operators", "default_deferrable", fallback=False)`. This is expected to continue.

![actally-no](/images/posts-image/2024-check_default_value_of_default_deferrable_through_ast/actually-no.jpg)

While writing this post and examining the AST, I realized that there are still some edge cases I missed, so I improved it by [ci: improve check_deferrable_default script to cover positional variables #41924](https://github.com/apache/airflow/pull/41924). Before checking that PR, you can try reread the script to see whether you can find where the missing piece is.
