from invoke import task

DEVELOPMENT_CONTAINER = "dev"
PRODUCTION_CONTAINER = "prod"

CONTAINERS = {
    DEVELOPMENT_CONTAINER: "docker-compose",
    PRODUCTION_CONTAINER: "docker-compose -f docker-compose.prod.yml",
}


@task
def build(context, compose="dev"):
    """Build project."""
    context.run(f"{CONTAINERS[compose]} build")


@task
def run_build(context, compose="dev"):
    """Run and build app."""
    context.run(f"{CONTAINERS[compose]} up --build")


@task
def run(context, compose="dev"):
    """Run postgres, redis, telegram app."""
    context.run(f"{CONTAINERS[compose]} up")


@task
def run_build_background(context, compose="dev"):
    """Build project."""
    context.run(f"{CONTAINERS[compose]} up -d --build")


@task
def run_background(context, compose="dev"):
    """Build project."""
    context.run(f"{CONTAINERS[compose]} up -d")


@task
def clean_volumes(context, compose="dev"):
    """Clean volumes."""
    context.run(f"{CONTAINERS[compose]} down -v")


@task
def stop(context, compose="dev"):
    """Stop and remove all containers defined in docker-compose."""
    context.run(f"{CONTAINERS[compose]} stop")


@task
def clear(context, compose="dev"):
    """Stop and remove all containers defined in docker-compose."""
    stop(context, compose)
    context.run("docker system prune -f")


def docker_compose_run(context, service, command, compose="dev"):
    """Run ``run`` using docker-compose."""
    context.run(f"{CONTAINERS[compose]} run --rm {service} {command}")
