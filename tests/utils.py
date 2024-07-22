from pathlib import Path


def make_fs_url(path: str | Path) -> str:
    """
    Return File URL.

    :param path: File path.
    :return: File URL.
    """
    if not path:
        raise ValueError("Path cannot be empty.")

    return f"file://{path!s}"
