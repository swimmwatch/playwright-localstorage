import typing

import pytest
from playwright.sync_api import Page

from tests.types import TempFileFactoryType
from tests.utils import make_fs_url


@pytest.fixture
def temp_page(page: Page, temp_page_maker: TempFileFactoryType):
    def wrapper(js_code: typing.Optional[str] = None) -> Page:
        if js_code is None:
            js_code = ""

        path = temp_page_maker(js_code)
        url = make_fs_url(path)

        page.goto(url)

        return page

    return wrapper
