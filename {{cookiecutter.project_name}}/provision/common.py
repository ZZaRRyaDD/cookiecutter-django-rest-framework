from rich import panel, print


def success(msg):
    """Print success message."""
    return print(panel.Panel(msg, style="green bold"))


def warn(msg):
    """Print warning message."""
    return print(panel.Panel(msg, style="yellow bold"))


def error(msg):
    """Print error message."""
    return print(panel.Panel(msg, style="red bold"))
