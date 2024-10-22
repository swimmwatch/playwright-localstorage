import typing
import uuid
from collections import Counter

import pytest

from playwright_localstorage.sync_ import SessionStorageAccessor
from tests.types import TempPageFactoryType


class TestGetValue:
    def test_random_key_not_exist(self, temp_page: TempPageFactoryType) -> None:
        page = temp_page()

        random_key = uuid.uuid4().hex
        accessor = SessionStorageAccessor(page)
        value = accessor.get(random_key)
        assert value is None

    @pytest.mark.parametrize(
        ("js_code", "expected"),
        [
            ('ss.setItem("key", 1)', "1"),
            ('ss.setItem("key", "abc")', "abc"),
        ],
    )
    def test_values(
        self,
        temp_page: TempPageFactoryType,
        js_code: str,
        expected: typing.Any,
    ) -> None:
        page = temp_page(js_code)
        accessor = SessionStorageAccessor(page)
        actual = accessor.get("key")
        assert actual == expected


class TestSetValue:
    @pytest.mark.parametrize(
        ("value", "expected"),
        [
            (None, "null"),
            (0, "0"),
            ("abc", "abc"),
            (True, "true"),
            (False, "false"),
            ({}, "[object Object]"),
        ],
    )
    def test_values(
        self,
        temp_page: TempPageFactoryType,
        value: typing.Any,
        expected: str,
    ) -> None:
        key = "key"
        page = temp_page()
        accessor = SessionStorageAccessor(page)
        accessor.set(key, value)
        actual = accessor.get(key)
        assert actual == expected


class TestHasKey:
    def test_not_exists(
        self,
        temp_page: TempPageFactoryType,
    ) -> None:
        key = "key"
        page = temp_page()
        accessor = SessionStorageAccessor(page)
        assert not accessor.has(key)

    def test_exists(
        self,
        temp_page: TempPageFactoryType,
    ) -> None:
        key = "key"
        page = temp_page('ss.setItem("key", "abc")')
        accessor = SessionStorageAccessor(page)
        assert accessor.has(key)


class TestRemoveKey:
    def test_not_exists(
        self,
        temp_page: TempPageFactoryType,
    ) -> None:
        key = "key"
        page = temp_page()
        accessor = SessionStorageAccessor(page)
        accessor.remove(key)

    def test_exists(
        self,
        temp_page: TempPageFactoryType,
    ) -> None:
        key = "key"
        page = temp_page('ss.setItem("key", "abc")')
        accessor = SessionStorageAccessor(page)
        assert accessor.has(key)

        accessor.remove(key)
        assert not accessor.has(key)


class TestGetKeys:
    @pytest.mark.parametrize(
        "keys",
        [
            [],
            ["a"],
            ["a", "b"],
        ],
    )
    def test_keys(
        self,
        temp_page: TempPageFactoryType,
        keys: typing.Sequence[str],
    ) -> None:
        page = temp_page()
        accessor = SessionStorageAccessor(page)

        for i, key in enumerate(keys):
            accessor.set(key, i)

        actual = accessor.keys()
        assert Counter(actual) == Counter(keys)


class TestGetItems:
    @pytest.mark.parametrize(
        "items",
        [
            {},
            {"a": "1"},
            {"a": "1", "b": "2"},
        ],
    )
    def test_items(
        self,
        temp_page: TempPageFactoryType,
        items: dict[str, str],
    ) -> None:
        page = temp_page()
        accessor = SessionStorageAccessor(page)

        for key, val in items.items():
            accessor.set(key, val)

        actual = accessor.items()
        assert actual == items


class TestGetLength:
    @pytest.mark.parametrize(
        "keys",
        [
            [],
            ["a"],
            ["a", "b"],
        ],
    )
    def test_length(
        self,
        temp_page: TempPageFactoryType,
        keys: typing.Sequence[str],
    ) -> None:
        page = temp_page()
        accessor = SessionStorageAccessor(page)

        for i, key in enumerate(keys):
            accessor.set(key, i)

        actual = accessor.len()
        assert actual == len(keys)


class TestClear:
    @pytest.mark.parametrize(
        "keys",
        [
            [],
            ["a"],
            ["a", "b"],
        ],
    )
    def test_length(
        self,
        temp_page: TempPageFactoryType,
        keys: typing.Sequence[str],
    ) -> None:
        page = temp_page()
        accessor = SessionStorageAccessor(page)

        for i, key in enumerate(keys):
            accessor.set(key, i)

        accessor.clear()

        assert accessor.len() == 0
