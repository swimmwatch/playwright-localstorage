<!-- markdownlint-disable -->

<a href="../../playwright_localstorage/async_.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `playwright_localstorage.async_`






---

<a href="../../playwright_localstorage/async_.py#L8"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `AsyncLocalStorageAccessor`
Provides access to local storage and allows you to perform various data operations. 

<a href="../../playwright_localstorage/async_.py#L11"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(page: Page) → None
```








---

<a href="../../playwright_localstorage/async_.py#L92"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `clear`

```python
clear() → None
```

Clears all keys stored. 



**Returns:**
  None 

---

<a href="../../playwright_localstorage/async_.py#L38"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get`

```python
get(key: str) → Optional[Any]
```

Returns key's value, or None if the key does not exist. 



**Args:**
 
 - <b>`key`</b>:  A string containing the name of the key you want to retrieve the value of. 



**Returns:**
 
 - <b>`any`</b>:  The value of the key if it exists, or None if the key does not exist. 

---

<a href="../../playwright_localstorage/async_.py#L67"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `has`

```python
has(key: str) → bool
```

Returns True if the key exists, False otherwise. 



**Args:**
 
 - <b>`key`</b>:  A string containing the name of the key you want to check existence. 



**Returns:**
 
 - <b>`bool`</b>:  True if the key exists, False otherwise. 

---

<a href="../../playwright_localstorage/async_.py#L22"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `items`

```python
items() → dict[str, Any]
```

Returns dictionary with all data items stored. 



**Returns:**
 
 - <b>`dict[str, typing.Any]`</b>:  A dictionary with all data items stored. 

---

<a href="../../playwright_localstorage/async_.py#L30"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `keys`

```python
keys() → Sequence[str]
```

Returns all stored keys. 



**Returns:**
 
 - <b>`typing.Sequence[str]`</b>:  A list of all stored keys. 

---

<a href="../../playwright_localstorage/async_.py#L14"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `len`

```python
len() → int
```

Returns an integer representing the number of data items stored. 



**Returns:**
 
 - <b>`int`</b>:  The number of data items stored. 

---

<a href="../../playwright_localstorage/async_.py#L78"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `remove`

```python
remove(key: str) → None
```

Remove the key from the storage if it exists. 



**Args:**
 
 - <b>`key`</b>:  A string containing the name of the key you want to remove. 



**Returns:**
 None 

---

<a href="../../playwright_localstorage/async_.py#L52"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set`

```python
set(key: str, value: Optional[Any]) → None
```

Add the key or update that key's value if it already exists. 



**Args:**
 
 - <b>`key`</b>:  A string containing the name of the key you want to create/update. 
 - <b>`value`</b>:  A string containing the value you want to give the key you are creating/updating. 



**Returns:**
 None 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._