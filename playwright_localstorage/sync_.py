import typing

from playwright.sync_api import Page

from .base import BaseLocalStorageAccessor
from .base import BaseSessionStorageAccessor


class LocalStorageAccessor(BaseLocalStorageAccessor):
    """Provides access to local storage and allows you to perform various data operations."""

    def __init__(self, page: Page) -> None:
        self._page = page

    def len(self) -> int:
        """Returns an integer representing the number of data items stored.

        Returns:
            int: The number of data items stored.
        """
        return self._page.evaluate(self.LEN_COMMAND)

    def items(self) -> dict[str, typing.Any]:
        """Returns dictionary with all data items stored.

        Returns:
            dict[str, typing.Any]: A dictionary with all data items stored.
        """
        return self._page.evaluate(self.ITEMS_COMMAND)

    def keys(self) -> typing.Sequence[str]:
        """Returns all stored keys.

        Returns:
            typing.Sequence[str]: A list of all stored keys.
        """
        return self._page.evaluate(self.KEYS_COMMAND)

    def get(self, key: str) -> typing.Union[typing.Any, None]:
        """Returns key's value, or None if the key does not exist.

        Args:
            key: A string containing the name of the key you want to retrieve the value of.

        Returns:
            any: The value of the key if it exists, or None if the key does not exist.
        """
        return self._page.evaluate(
            self.GET_COMMAND,
            {"key": key},
        )

    def set(self, key: str, value: typing.Union[typing.Any, None]) -> None:
        """Add the key or update that key's value if it already exists.

        Args:
            key: A string containing the name of the key you want to create/update.
            value: A string containing the value you want to give the key you are creating/updating.

        Returns:
            None
        """
        self._page.evaluate(
            self.SET_COMMAND,
            {"key": key, "value": value},
        )

    def has(self, key: str) -> bool:
        """Returns True if the key exists, False otherwise.

        Args:
            key: A string containing the name of the key you want to check existence.

        Returns:
            bool: True if the key exists, False otherwise.
        """
        return key in self.keys()

    def remove(self, key: str) -> None:
        """Remove the key from the storage if it exists.

        Args:
            key: A string containing the name of the key you want to remove.

        Returns:
            None
        """
        self._page.evaluate(
            self.REMOVE_COMMAND,
            {"key": key},
        )

    def clear(self) -> None:
        """Clears all keys stored.

        Returns:
            None
        """
        self._page.evaluate(self.CLEAR_COMMAND)


class SessionStorageAccessor(BaseSessionStorageAccessor):
    """Provides access to session storage and allows you to perform various data operations."""

    def __init__(self, page: Page) -> None:
        self._page = page

    def len(self) -> int:
        """Returns an integer representing the number of data items stored.

        Returns:
            int: The number of data items stored.
        """
        return self._page.evaluate(self.LEN_COMMAND)

    def items(self) -> dict[str, typing.Any]:
        """Returns dictionary with all data items stored.

        Returns:
            dict[str, typing.Any]: A dictionary with all data items stored.
        """
        return self._page.evaluate(self.ITEMS_COMMAND)

    def keys(self) -> typing.Sequence[str]:
        """Returns all stored keys.

        Returns:
            typing.Sequence[str]: A list of all stored keys.
        """
        return self._page.evaluate(self.KEYS_COMMAND)

    def get(self, key: str) -> typing.Union[typing.Any, None]:
        """Returns key's value, or None if the key does not exist.

        Args:
            key: A string containing the name of the key you want to retrieve the value of.

        Returns:
            any: The value of the key if it exists, or None if the key does not exist.
        """
        return self._page.evaluate(
            self.GET_COMMAND,
            {"key": key},
        )

    def set(self, key: str, value: typing.Union[typing.Any, None]) -> None:
        """Add the key or update that key's value if it already exists.

        Args:
            key: A string containing the name of the key you want to create/update.
            value: A string containing the value you want to give the key you are creating/updating.

        Returns:
            None
        """
        self._page.evaluate(
            self.SET_COMMAND,
            {"key": key, "value": value},
        )

    def has(self, key: str) -> bool:
        """Returns True if the key exists, False otherwise.

        Args:
            key: A string containing the name of the key you want to check existence.

        Returns:
            bool: True if the key exists, False otherwise.
        """
        return key in self.keys()

    def remove(self, key: str) -> None:
        """Remove the key from the storage if it exists.

        Args:
            key: A string containing the name of the key you want to remove.

        Returns:
            None
        """
        self._page.evaluate(
            self.REMOVE_COMMAND,
            {"key": key},
        )

    def clear(self) -> None:
        """Clears all keys stored.

        Returns:
            None
        """
        self._page.evaluate(self.CLEAR_COMMAND)
