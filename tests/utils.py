import typing
from pathlib import Path


def make_fs_url(path: typing.Union[str, Path]) -> str:
    """Return File URL.

    Args:
        path: File path.

    Returns:
        File URL.
    """
    if not path:
        raise ValueError("Path cannot be empty.")

    return f"file://{path!s}"
