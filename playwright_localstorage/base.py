class BaseLocalStorageAccessor:
    LEN_COMMAND = "() => window.localStorage.length;"
    ITEMS_COMMAND = (
        "() => {"
        "   let ls = window.localStorage, items = {}; "
        "   for (let i = 0, k; i < ls.length; ++i) "
        "       items[k = ls.key(i)] = ls.getItem(k); "
        "   return items; "
        "}"
    )
    KEYS_COMMAND = (
        "() => {"
        "   let ls = window.localStorage, keys = []; "
        "   for (var i = 0; i < ls.length; ++i) "
        "       keys[i] = ls.key(i); "
        "   return keys; "
        "}"
    )
    GET_COMMAND = "(kwargs) => window.localStorage.getItem(kwargs.key)"
    SET_COMMAND = "(kwargs) => window.localStorage.setItem(kwargs.key, kwargs.value)"
    REMOVE_COMMAND = "(kwargs) => window.localStorage.removeItem(kwargs.key);"
    CLEAR_COMMAND = "() => window.localStorage.clear();"


class BaseSessionStorageAccessor:
    LEN_COMMAND = "() => window.sessionStorage.length;"
    ITEMS_COMMAND = (
        "() => {"
        "   let ls = window.sessionStorage, items = {}; "
        "   for (let i = 0, k; i < ls.length; ++i) "
        "       items[k = ls.key(i)] = ls.getItem(k); "
        "   return items; "
        "}"
    )
    KEYS_COMMAND = (
        "() => {"
        "   let ls = window.sessionStorage, keys = []; "
        "   for (var i = 0; i < ls.length; ++i) "
        "       keys[i] = ls.key(i); "
        "   return keys; "
        "}"
    )
    GET_COMMAND = "(kwargs) => window.sessionStorage.getItem(kwargs.key)"
    SET_COMMAND = "(kwargs) => window.sessionStorage.setItem(kwargs.key, kwargs.value)"
    REMOVE_COMMAND = "(kwargs) => window.sessionStorage.removeItem(kwargs.key);"
    CLEAR_COMMAND = "() => window.sessionStorage.clear();"
