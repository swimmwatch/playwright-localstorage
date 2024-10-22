import typing

from playwright.async_api import Page

from .base import BaseLocalStorageAccessor
from .base import BaseSessionStorageAccessor


class AsyncLocalStorageAccessor(BaseLocalStorageAccessor):
    """Provides access to local storage and allows you to perform various data operations."""

    def __init__(self, page: Page) -> None:
        self._page = page

    async def len(self) -> int:
        """Returns an integer representing the number of data items stored.

        Returns:
            int: The number of data items stored.
        """
        return await self._page.evaluate(self.LEN_COMMAND)

    async def items(self) -> dict[str, typing.Any]:
        """Returns dictionary with all data items stored.

        Returns:
            dict[str, typing.Any]: A dictionary with all data items stored.
        """
        return await self._page.evaluate(self.ITEMS_COMMAND)

    async def keys(self) -> typing.Sequence[str]:
        """Returns all stored keys.

        Returns:
            typing.Sequence[str]: A list of all stored keys.
        """
        return await self._page.evaluate(self.KEYS_COMMAND)

    async def get(self, key: str) -> typing.Union[typing.Any, None]:
        """Returns key's value, or None if the key does not exist.

        Args:
            key: A string containing the name of the key you want to retrieve the value of.

        Returns:
            any: The value of the key if it exists, or None if the key does not exist.
        """
        return await self._page.evaluate(
            self.GET_COMMAND,
            {"key": key},
        )

    async def set(self, key: str, value: typing.Union[typing.Any, None]) -> None:
        """Add the key or update that key's value if it already exists.

        Args:
            key: A string containing the name of the key you want to create/update.
            value: A string containing the value you want to give the key you are creating/updating.

        Returns:
            None
        """
        await self._page.evaluate(
            self.SET_COMMAND,
            {"key": key, "value": value},
        )

    async def has(self, key: str) -> bool:
        """Returns True if the key exists, False otherwise.

        Args:
            key: A string containing the name of the key you want to check existence.

        Returns:
            bool: True if the key exists, False otherwise.
        """
        return key in (await self.keys())

    async def remove(self, key: str) -> None:
        """Remove the key from the storage if it exists.

        Args:
            key: A string containing the name of the key you want to remove.

        Returns:
            None
        """
        await self._page.evaluate(
            self.REMOVE_COMMAND,
            {"key": key},
        )

    async def clear(self) -> None:
        """Clears all keys stored.

        Returns:
            None
        """
        await self._page.evaluate(self.CLEAR_COMMAND)


class AsyncSessionStorageAccessor(BaseSessionStorageAccessor):
    """Provides access to local storage and allows you to perform various data operations."""

    def __init__(self, page: Page) -> None:
        self._page = page

    async def len(self) -> int:
        """Returns an integer representing the number of data items stored.

        Returns:
            int: The number of data items stored.
        """
        return await self._page.evaluate(self.LEN_COMMAND)

    async def items(self) -> dict[str, typing.Any]:
        """Returns dictionary with all data items stored.

        Returns:
            dict[str, typing.Any]: A dictionary with all data items stored.
        """
        return await self._page.evaluate(self.ITEMS_COMMAND)

    async def keys(self) -> typing.Sequence[str]:
        """Returns all stored keys.

        Returns:
            typing.Sequence[str]: A list of all stored keys.
        """
        return await self._page.evaluate(self.KEYS_COMMAND)

    async def get(self, key: str) -> typing.Union[typing.Any, None]:
        """Returns key's value, or None if the key does not exist.

        Args:
            key: A string containing the name of the key you want to retrieve the value of.

        Returns:
            any: The value of the key if it exists, or None if the key does not exist.
        """
        return await self._page.evaluate(
            self.GET_COMMAND,
            {"key": key},
        )

    async def set(self, key: str, value: typing.Union[typing.Any, None]) -> None:
        """Add the key or update that key's value if it already exists.

        Args:
            key: A string containing the name of the key you want to create/update.
            value: A string containing the value you want to give the key you are creating/updating.

        Returns:
            None
        """
        await self._page.evaluate(
            self.SET_COMMAND,
            {"key": key, "value": value},
        )

    async def has(self, key: str) -> bool:
        """Returns True if the key exists, False otherwise.

        Args:
            key: A string containing the name of the key you want to check existence.

        Returns:
            bool: True if the key exists, False otherwise.
        """
        return key in (await self.keys())

    async def remove(self, key: str) -> None:
        """Remove the key from the storage if it exists.

        Args:
            key: A string containing the name of the key you want to remove.

        Returns:
            None
        """
        await self._page.evaluate(
            self.REMOVE_COMMAND,
            {"key": key},
        )

    async def clear(self) -> None:
        """Clears all keys stored.

        Returns:
            None
        """
        await self._page.evaluate(self.CLEAR_COMMAND)
