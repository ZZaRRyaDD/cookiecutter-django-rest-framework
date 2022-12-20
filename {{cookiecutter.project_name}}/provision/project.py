from invoke import task

from . import django


@task
def fill_sample_data(context, compose="dev"):
    """Prepare sample data for local usage."""
    django.manage(
        context,
        command="runscript fill_sample_data",
        compose=compose,
    )
