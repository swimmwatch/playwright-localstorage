import typing

import pytest
from playwright.async_api import Page

from tests.types import TempFileFactoryType
from tests.types import TempPageFactoryType
from tests.utils import make_fs_url


@pytest.fixture
async def temp_page(page: Page, temp_page_maker: TempFileFactoryType) -> TempPageFactoryType:
    async def wrapper(js_code: typing.Optional[str] = None) -> Page:
        if js_code is None:
            js_code = ""

        path = temp_page_maker(js_code)
        url = make_fs_url(path)

        await page.goto(url)

        return page

    return wrapper
