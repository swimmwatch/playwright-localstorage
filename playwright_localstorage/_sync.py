import typing

from playwright.sync_api import Page

from playwright_localstorage.base import BaseLocalStorageAccessor


class LocalStorageAccessor(BaseLocalStorageAccessor):
    def __init__(self, page: Page) -> None:
        self._page = page

    def len(self) -> int:
        return self._page.evaluate(self.LEN_COMMAND)

    def items(self) -> dict[str, typing.Any]:
        return self._page.evaluate(self.ITEMS_COMMAND)

    def keys(self) -> typing.Sequence[str]:
        return self._page.evaluate(self.KEYS_COMMAND)

    def get(self, key: str) -> typing.Any:
        return self._page.evaluate(
            self.GET_COMMAND,
            {"key": key},
        )

    def set(self, key, value) -> None:
        self._page.evaluate(
            self.SET_COMMAND,
            {"key": key, "value": value},
        )

    def has(self, key: str) -> bool:
        return key in self.keys()

    def remove(self, key: str) -> None:
        self._page.evaluate(
            self.REMOVE_COMMAND,
            {"key": key},
        )

    def clear(self) -> None:
        self._page.evaluate(self.CLEAR_COMMAND)
