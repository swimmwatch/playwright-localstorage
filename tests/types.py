import typing
from pathlib import Path

from playwright.async_api import Page as AsyncPage
from playwright.sync_api import Page as SyncPage

PageType = typing.TypeVar("PageType", bound=AsyncPage | SyncPage)
TempPageFactoryType = typing.Callable[..., PageType]
TempFileFactoryType = typing.Callable[[str], Path]
