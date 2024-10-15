# -*- coding: utf-8 -*-

import datetime
import os
import shlex
import shutil
import subprocess
import sys

from invoke import task
from invoke.main import program
from pelican import main as pelican_main
from pelican.server import ComplexHTTPRequestHandler, RootedHTTPServer
from pelican.settings import DEFAULT_CONFIG, get_settings_from_file

OPEN_BROWSER_ON_SERVE = True
SETTINGS_FILE_BASE = "pelicanconf.py"
SETTINGS = {}
SETTINGS.update(DEFAULT_CONFIG)
LOCAL_SETTINGS = get_settings_from_file(SETTINGS_FILE_BASE)
SETTINGS.update(LOCAL_SETTINGS)

CONFIG = {
    "settings_base": SETTINGS_FILE_BASE,
    "settings_publish": "publishconf.py",
    # Output path. Can be absolute or relative to tasks.py. Default: 'output'
    "deploy_path": SETTINGS["OUTPUT_PATH"],
    # Github Pages configuration
    "github_pages_branch": "gh-pages",
    "commit_message": "'Publish site on {}'".format(datetime.date.today().isoformat()),
    # Host and port for `serve`
    "host": "localhost",
    "port": 8000,
}


@task
def clean(c):
    """Remove generated files"""
    if os.path.isdir(CONFIG["deploy_path"]):
        shutil.rmtree(CONFIG["deploy_path"])
        os.makedirs(CONFIG["deploy_path"])


@task(optional=["--build-pagefind"])
def build(c, build_pagefind=False):
    """Build local version of site"""
    if (
        build_pagefind
        and subprocess.call(["npx", "-y", "pagefind", "--site", "output"]) == 1
    ):
        print("failed to call 'npx -y pagefind --site output'")
    pelican_run("-s {settings_base}".format(**CONFIG))


@task(optional=["--build-pagefind"])
def rebuild(c, build_pagefind=False):
    """`build` with the delete switch"""
    if (
        build_pagefind
        and subprocess.call(["npx", "-y", "pagefind", "--site", "output"]) == 1
    ):
        print("failed to call 'npx -y pagefind --site output'")
    pelican_run("-d -s {settings_base}".format(**CONFIG))


@task
def regenerate(c):
    """Automatically regenerate site upon file modification"""
    pelican_run("-r -s {settings_base}".format(**CONFIG))


@task
def serve(c):
    """Serve site at http://$HOST:$PORT/ (default is localhost:8000)"""

    class AddressReuseTCPServer(RootedHTTPServer):
        allow_reuse_address = True

    server = AddressReuseTCPServer(
        CONFIG["deploy_path"],
        (CONFIG["host"], CONFIG["port"]),
        ComplexHTTPRequestHandler,
    )

    if OPEN_BROWSER_ON_SERVE:
        # Open site in default browser
        import webbrowser

        webbrowser.open("http://{host}:{port}".format(**CONFIG))

    sys.stderr.write("Serving at {host}:{port} ...\n".format(**CONFIG))
    server.serve_forever()


@task
def reserve(c):
    """`build`, then `serve`"""
    build(c, build_pagefind=False)
    serve(c)


@task
def preview(c):
    """Build production version of site"""
    pelican_run("-s {settings_publish}".format(**CONFIG))


@task
def livereload(c):
    """Automatically reload browser tab upon file modification."""
    from livereload import Server

    def cached_build():
        cmd = "-s {settings_base} -e CACHE_CONTENT=true LOAD_CONTENT_CACHE=true"
        pelican_run(cmd.format(**CONFIG))

    cached_build()
    server = Server()
    theme_path = SETTINGS["THEME"]
    watched_globs = [
        CONFIG["settings_base"],
        "{}/templates/**/*.html".format(theme_path),
    ]

    content_file_extensions = [".md", ".rst"]
    for extension in content_file_extensions:
        content_glob = "{0}/**/*{1}".format(SETTINGS["PATH"], extension)
        watched_globs.append(content_glob)

    static_file_extensions = [".css", ".js"]
    for extension in static_file_extensions:
        static_file_glob = "{0}/static/**/*{1}".format(theme_path, extension)
        watched_globs.append(static_file_glob)

    for glob in watched_globs:
        server.watch(glob, cached_build)

    if OPEN_BROWSER_ON_SERVE:
        # Open site in default browser
        import webbrowser

        webbrowser.open("http://{host}:{port}".format(**CONFIG))

    server.serve(host=CONFIG["host"], port=CONFIG["port"], root=CONFIG["deploy_path"])


@task(optional=["--build-pagefind"])
def build_publish(c, build_pagefind=False):
    """Build pages with publishconf.py"""
    if (
        build_pagefind
        and subprocess.call(["npx", "-y", "pagefind", "--site", "output"]) == 1
    ):
        print("failed to call 'npx -y pagefind --site output'")
    pelican_run("-s {settings_publish}".format(**CONFIG))


@task
def gh_pages(c):
    """Publish to GitHub Pages"""
    preview(c)
    c.run(
        "ghp-import -b {github_pages_branch} "
        "-m {commit_message} "
        "{deploy_path} -p".format(**CONFIG)
    )


def pelican_run(cmd):
    cmd += " " + program.core.remainder  # allows to pass-through args to pelican
    pelican_main(shlex.split(cmd))


@task
def style(c):
    """Run style check on python code"""
    python_targets = "pelicanconf.py publishconf.py tasks.py"
    c.run(
        f"""
        uv run ruff check {python_targets} && \
        uv run cz check --rev-range origin/main..
        """
    )


@task
def format(c):
    """Run autoformater on python code"""
    python_targets = "pelicanconf.py publishconf.py tasks.py"
    c.run(
        f"""
        uv run ruff check {python_targets} --fix
        """
    )


# @task
# def security_check(c):
#     """Run pip-autid on dependencies"""
#     c.run(
#         """
#         uv export --output=requirements.txt --without-hashes && \
#         uv run pip-audit -r requirements.txt && \
#         rm -rf requirements.txt
#         """
#     )
