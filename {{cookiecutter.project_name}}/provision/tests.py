from invoke import task

from . import common, docker


@task
def pytest(context, service="django", params="", compose="dev"):
    """Run django tests."""
    common.success("Tests running")
    docker.docker_compose_run(context, service, f"pytest {params}", compose)
