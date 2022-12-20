from invoke import Collection

from provision import django, docker, git, linters, project, tests

ns = Collection(
    django,
    docker,
    linters,
    project,
    tests,
    git,
)

ns.configure(
    dict(
        run=dict(
            pty=True,
            echo=True,
        ),
    ),
)
