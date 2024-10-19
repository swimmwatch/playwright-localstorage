from pathlib import Path

import pytest

from tests.utils import make_fs_url


@pytest.mark.parametrize(
    ("path", "expected_url"),
    [
        ("index.html", "file://index.html"),
        (Path("index.html"), "file://index.html"),
    ],
)
def test_make_fs_url(path, expected_url):
    assert make_fs_url(path) == expected_url


def test_make_fs_url_invalid():
    with pytest.raises(ValueError, match="cannot be empty"):
        make_fs_url("")
