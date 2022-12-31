from invoke import task

from . import django, common


@task
def fill_sample_data(context, compose="dev"):
    """Prepare sample data for local usage."""
    django.manage(
        context,
        command="runscript fill_sample_data",
        compose=compose,
    )


@task
def install_tools(context):
    """Install cli dependencies, and tools needed to install requirements."""
    context.run("pip install setuptools pip pip-tools wheel poetry")


@task
def install_requirements(context):
    """Install local development requirements."""
    common.success("Install requirements with poetry")
    context.run("cd src && poetry install")
