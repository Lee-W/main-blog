Title: Dive deeper into AST
Subtitle: but not too deeply
Date: 2024-09-02 21:35
Category: Tech
Tags: Python, Airflow, AST
Slug: dig-into-ast-a-bit-more
Authors: Wei Lee
Series: Unleash the Chaos: Developing a Linter for Un-Pythonic Code!

The purpose of this post was to delve into the [ast](https://docs.python.org/3/library/ast.html)
But...

<!--more-->

The documentation appears to be clear, and the naming is straightforward enough. 🤔 So, I'll only add a few examples and make some notes that might make sense to me and help me pick up ast much faster next time. Also, it's worth noting that parsed ast might change from version to version. The Python version used here is 3.12.5.

For those unfamiliar with Abstract Syntax Trees (AST), it is a way to represent your code in a tree structure. Experiment with the following code snippet using different Python code to gain a better understanding of what AST is.

```python
import ast

module_name = "the path to you code"
ast_tree = ast.parse(open(module_name).read())
print(ast.dump(ast_tree, indent=4))
print(ast.unparse(ast_tree))
```

---

[TOC]

## Helpers
* functions
    * `ast.parse`
        * parse code as the ast node
    * `ast.unparse`
        * unparse the ast node as code
    * `ast.dump`
        * return a formatted dump of the ast tree
    * `ast.walk`
        * walk through the ast tree (iterator)
    * `ast.iter_child_nodes`
    * `ast.iter_fields`
    * `ast.fix_missing_locations`
        * recalculate the location information (commonly used after adding a new ast node)
    * `ast.literal_eval`
    * `ast.get_docstring`
    * `ast.get_source_segment`
    * `ast.increment_lineno`
    * `ast.copy_location`
* classes
    * `ast.NodeVisitor`: base class for visiting an ast tree
        * `visit`
    * `ast.NodeTransformer`: base class for modifying an ast tree
        * `visit_{Node Class}`

In the [previous article]({filename}/posts/tech/2024/18-check_default_value_of_default_deferrable_through_ast.md), I improved the linter with [CI: improved check_deferrable_default script to cover positional variables #41924](https://github.com/apache/airflow/pull/41924). But after digging into the [ast](https://docs.python.org/3/library/ast.html) module, I found out things don't need to be that complicated.

### Let's refactor the default_deferrable linter

To validate the default value, I can unparse the `default` ast to a string and compare it with the expected value `conf.getboolean('operators', 'default_deferrable', fallback=False)`. (the string representation of an ast node use `'` instead of `"` to quote a string)

```python
def _is_valid_deferrable_default(default: ast.AST) -> bool:
    """Check whether default is 'conf.getboolean("operators", "default_deferrable", fallback=False)'"""
    return ast.unparse(default) == "conf.getboolean('operators', 'default_deferrable', fallback=False)"
```

To replace the functionality of finding the `__init__` method in classes, I use an `ast.NodeVisitor` with `visit_FunctionDef` instead. The logic after finding `__init__` remains mostly the same. The only difference is that we are now collecting the line numbers that contain an error instead of yielding it.

```python
class DefaultDeferrableVisitor(ast.NodeVisitor):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, *kwargs)
        self.error_linenos: list[int] = []

    def visit_FunctionDef(self, node: ast.FunctionDef) -> ast.FunctionDef:
        if node.name == "__init__":
            args = node.args
            arguments = reversed([*args.args, *args.posonlyargs, *args.kwonlyargs])
            defaults = reversed([*args.defaults, *args.kw_defaults])
            for argument, default in itertools.zip_longest(arguments, defaults):
                # argument is not deferrable
                if argument is None or argument.arg != "deferrable":
                    continue

                # argument is deferrable, but comes with no default value
                if default is None:
                    self.error_linenos.append(argument.lineno)
                    continue

                # argument is deferrable, but the default value is not valid
                if not _is_valid_deferrable_default(default):
                    self.error_linenos.append(default.lineno)
        return node
```

We then use the newly implemented `DefaultDeferrableVisitor` to traverse the module AST tree and check the default value. Now, the `iter_check_deferrable_default_errors` is much cleaner. 🎉

```python
def iter_check_deferrable_default_errors(module_filename: str) -> Iterator[str]:
    ast_tree = ast.parse(open(module_filename).read())
    visitor = DefaultDeferrableVisitor()
    visitor.visit(ast_tree)
    yield from (f"{module_filename}:{lineno}" for lineno in visitor.error_linenos)
```

## Node Classes
This section lists all the nodes available in an AST tree in Python 3.12. It's pretty much the same as the documentation, but I've reorganized it in a way that I can easily understand.

* Root nodes
    * `Module`
        * when `ast.parse(..., mode="exec")`
    * `Expression`
        * when `ast.parse(..., mode="eval")`
    * `Interactive`
        * When `ast.parse(..., mode="single")`
    * `FunctionType`
        * When `ast.parse(..., mode="func_type")`
        * for expressions such as `# type: (int, int) -> int` back to the time PEP 484 wasn't there
* Expressions
    * Literals
        * `Constant`
        * `FormattedValue`
        * `List`
        * `Tuple`
        * `Set`
        * `Dict`
    * Variables
        * `Name`
            * `ctx=`
                * `Load`
                * `Store`
                * `Del`
        * `Starred`
            * e.g., `*var`
    * `Expr`
        * Operators (`op=`)
            * `UnaryOp`
                * `UAdd`
                * `USub`
                * `Not`
                * `Invert`
            * `BinOp`
                * `Add`
                * `Sub`
                * `Mult`
                * `Div`
                * `FloorDiv`
                * `Mod`
                * `Lshift`
                * `RShift`
                * `BitOr`
                * `BitXor`
                * `BitAnd`
                * `MatMult`
            * `BoolOp`
                * `And`
                * `OR`
            * `Compare`
                * `Eq`
                * `NotEq`
                * `Lt`
                * `LtE`
                * `Gt`
                * `GtE`
                * `Is`
                * `IsNot`
                * `In`
                * `NotIn`
        * `Call` (`keywords=keyword(..)`)
        * `IfExp`
        * `Attribute`
        * `NamedExpr`
    * `Subscript`
    * `Slice`
    * Comprehensions (`generators=[comprehension(...)]`)
        * `ListComp`
        * `SetComp`
        * `GeneratorExp`
        * `DictComp`
* Statements
    * `Assign`
        * `type_comment=`
    * `AnnAssign`
        * annotated assignment
    * `AugAssign`
        * augmented assignment
        * e.g., `x += 1`
    * `Raise`
    * `Assert`
    * `Delete`
    * `Pass`
    * `TypeAlias`
    * `Import`
    * `ImportFrom`
    * `alias`
    * Control Flow
        * `If`
        * `For`
        * `While`
        * `Break`
        * `Continue`
        * `Try`
        * `TryStart`
            * e.g., `except*`
        * `ExceptHandler`
        * `With` (`items=[withitem(...)]`)
* Pattern matching
    * `Match`
        * `cases=match_case(pattern=...), ...)`
            * `MatchValue`
            * `MatchSingleton`
            * `MatchSequence`
            * `MatchStar`
            * `MatchMapping`
            * `MatchClass`
            * `MatchAs`
            * `MatchOr`
* Type parameters
    * `TypeVar`
    * `ParamSpec`
    * `TypeVarTuple`
* Function and class definitions
    * `FunctionDef`, `Lambda`
        * `args=arguments(...)`
            * `args`, `posonlyargs`, `kwonlyargs`
                * `...=[arg(...), ...]`
            * `defaults`, `kw_defaults`
            * `vararg`, `kwarg`
                * i.e. `*args, **kwargs`
    * `Return`
    * `Yield`
    * `YieldFrom`
    * `Global`
    * `Nonlocal`
    * `ClassDef`
    * `AsyncFunctionDef`
    * `Await`
    * `AsyncFor`
    * `AsyncWith`
