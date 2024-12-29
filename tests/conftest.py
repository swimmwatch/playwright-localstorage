import typing
from pathlib import Path

import jinja2
import pytest

from tests.types import TempFileFactoryType

BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / Path("assets")

TEMP_PAGE_TEMPLATE_NAME = "page.html.j2"
TEMP_PAGE_TEMPLATE_PATH = ASSETS_DIR / TEMP_PAGE_TEMPLATE_NAME
TEMP_PAGE_PATH = ASSETS_DIR / "page_%s.html"


@pytest.fixture
def template_loader() -> jinja2.FileSystemLoader:
    return jinja2.FileSystemLoader(searchpath=ASSETS_DIR)


@pytest.fixture
def template_env(template_loader: jinja2.FileSystemLoader):
    return jinja2.Environment(  # noqa: S701
        loader=template_loader,
        trim_blocks=True,
        lstrip_blocks=True,
    )


@pytest.fixture
def template_temp_page(template_env: jinja2.Environment) -> jinja2.Template:
    return template_env.get_template(TEMP_PAGE_TEMPLATE_NAME)


@pytest.fixture
def temp_page_maker(
    template_temp_page: jinja2.Template,
    worker_id: str,
) -> typing.Generator[TempFileFactoryType, None, None]:
    path = str(TEMP_PAGE_PATH)
    path = path % worker_id  # create file per process
    temp_file_path = Path(path)

    def wrapper(js_code: str) -> Path:
        """Creates HTML file with passed `js_code`.

        Args:
            js_code: JavaScript code.

        Returns:
            HTML file path.
        """
        content = template_temp_page.render(js_code=js_code)

        with open(path, "w") as file:
            file.write(content)

        return temp_file_path

    yield wrapper

    if temp_file_path.exists():
        temp_file_path.unlink()
