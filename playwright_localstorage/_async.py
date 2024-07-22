import typing

from playwright.async_api import Page

from playwright_localstorage.base import BaseLocalStorageAccessor


class AsyncLocalStorageAccessor(BaseLocalStorageAccessor):
    def __init__(self, page: Page) -> None:
        self._page = page

    async def len(self) -> int:
        return await self._page.evaluate(self.LEN_COMMAND)

    async def items(self) -> dict[str, typing.Any]:
        return await self._page.evaluate(self.ITEMS_COMMAND)

    async def keys(self) -> typing.Sequence[str]:
        return await self._page.evaluate(self.KEYS_COMMAND)

    async def get(self, key: str) -> typing.Any:
        return await self._page.evaluate(
            self.GET_COMMAND,
            {"key": key},
        )

    async def set(self, key, value) -> None:
        await self._page.evaluate(
            self.SET_COMMAND,
            {"key": key, "value": value},
        )

    async def has(self, key: str) -> bool:
        return key in (await self.keys())

    async def remove(self, key: str) -> None:
        await self._page.evaluate(
            self.REMOVE_COMMAND,
            {"key": key},
        )

    async def clear(self) -> None:
        await self._page.evaluate(self.CLEAR_COMMAND)
