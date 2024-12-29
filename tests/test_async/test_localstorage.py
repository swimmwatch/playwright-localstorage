import typing
import uuid
from collections import Counter

import pytest

from playwright_localstorage import AsyncLocalStorageAccessor
from tests.types import TempPageFactoryType


class TestGetValue:
    async def test_random_key_not_exist(self, temp_page: TempPageFactoryType) -> None:
        page = await temp_page()

        random_key = uuid.uuid4().hex
        accessor = AsyncLocalStorageAccessor(page)
        value = await accessor.get(random_key)
        assert value is None

    @pytest.mark.parametrize(
        ("js_code", "expected"),
        [
            ('ls.setItem("key", 1)', "1"),
            ('ls.setItem("key", "abc")', "abc"),
        ],
    )
    async def test_values(
        self,
        temp_page: TempPageFactoryType,
        js_code: str,
        expected: typing.Any,
    ) -> None:
        page = await temp_page(js_code)
        accessor = AsyncLocalStorageAccessor(page)
        actual = await accessor.get("key")
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
    async def test_values(
        self,
        temp_page: TempPageFactoryType,
        value: typing.Any,
        expected: str,
    ) -> None:
        key = "key"
        page = await temp_page()
        accessor = AsyncLocalStorageAccessor(page)
        await accessor.set(key, value)
        actual = await accessor.get(key)
        assert actual == expected


class TestHasKey:
    async def test_not_exists(
        self,
        temp_page: TempPageFactoryType,
    ) -> None:
        key = "key"
        page = await temp_page()
        accessor = AsyncLocalStorageAccessor(page)
        assert not (await accessor.has(key))

    async def test_exists(
        self,
        temp_page: TempPageFactoryType,
    ) -> None:
        key = "key"
        page = await temp_page('ls.setItem("key", "abc")')
        accessor = AsyncLocalStorageAccessor(page)
        assert await accessor.has(key)


class TestRemoveKey:
    async def test_not_exists(
        self,
        temp_page: TempPageFactoryType,
    ) -> None:
        key = "key"
        page = await temp_page()
        accessor = AsyncLocalStorageAccessor(page)
        await accessor.remove(key)

    async def test_exists(
        self,
        temp_page: TempPageFactoryType,
    ) -> None:
        key = "key"
        page = await temp_page('ls.setItem("key", "abc")')
        accessor = AsyncLocalStorageAccessor(page)
        assert await accessor.has(key)

        await accessor.remove(key)
        assert not (await accessor.has(key))


class TestGetKeys:
    @pytest.mark.parametrize(
        "keys",
        [
            [],
            ["a"],
            ["a", "b"],
        ],
    )
    async def test_keys(
        self,
        temp_page: TempPageFactoryType,
        keys: typing.Sequence[str],
    ) -> None:
        page = await temp_page()
        accessor = AsyncLocalStorageAccessor(page)

        for i, key in enumerate(keys):
            await accessor.set(key, i)

        actual = await accessor.keys()
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
    async def test_items(
        self,
        temp_page: TempPageFactoryType,
        items: dict[str, str],
    ) -> None:
        page = await temp_page()
        accessor = AsyncLocalStorageAccessor(page)

        for key, val in items.items():
            await accessor.set(key, val)

        actual = await accessor.items()
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
    async def test_length(
        self,
        temp_page: TempPageFactoryType,
        keys: typing.Sequence[str],
    ) -> None:
        page = await temp_page()
        accessor = AsyncLocalStorageAccessor(page)

        for i, key in enumerate(keys):
            await accessor.set(key, i)

        actual = await accessor.len()
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
    async def test_length(
        self,
        temp_page: TempPageFactoryType,
        keys: typing.Sequence[str],
    ) -> None:
        page = await temp_page()
        accessor = AsyncLocalStorageAccessor(page)

        for i, key in enumerate(keys):
            await accessor.set(key, i)

        await accessor.clear()

        assert (await accessor.len()) == 0
