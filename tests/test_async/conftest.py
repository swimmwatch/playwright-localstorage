import asyncio

import nest_asyncio
import pytest
import pytest_asyncio
from playwright.async_api import Page

from tests.types import TempFileFactoryType
from tests.types import TempPageFactoryType
from tests.utils import make_fs_url


@pytest.fixture
async def temp_page(page_async: Page, temp_page_maker: TempFileFactoryType) -> TempPageFactoryType:
    async def wrapper(js_code: str | None = None) -> Page:
        if js_code is None:
            js_code = ""

        path = temp_page_maker(js_code)
        url = make_fs_url(path)

        await page_async.goto(url)

        return page_async

    return wrapper


@pytest_asyncio.fixture(scope="session", autouse=True)
def event_loop():
    policy = asyncio.get_event_loop_policy()
    loop = policy.new_event_loop()
    nest_asyncio.apply(loop)
    yield loop
    loop.close()
