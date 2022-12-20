from invoke import Exit, UnexpectedExit, task

from . import common, linters


@task
def hooks(context):
    """Install git hooks."""
    common.success("Setting up GitHooks")
    context.run("git config core.hooksPath .git-hooks")


@task
def pre_push(context):
    """Perform pre push check."""
    common.success("Perform pre-push check")
    code_style_passed = _run_check(
        context=context,
        checker=linters.all,
        error_msg="Code style checks failed!",
    )
    if not all(
        [
            code_style_passed,
        ]
    ):
        common.error("Push aborted due to errors\nPLS fix them first!")
        raise Exit(code=1)
    common.success("Wonderful JOB! Thank You!")


def _run_check(context, checker, error_msg: str, *args, **kwargs):
    try:
        checker(context, *args, **kwargs)
    except (UnexpectedExit, Exit):
        common.warn(error_msg)
        return False
    return True
