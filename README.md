# playwright-localstorage

[![Python](https://img.shields.io/pypi/pyversions/playwright-localstorage.svg)](https://www.python.org/downloads/)
![Python linters and tests](https://github.com/swimmwatch/playwright-localstorage/actions/workflows/python-check.yml/badge.svg?branch=dev)
[![PyPI](https://img.shields.io/pypi/v/playwright-localstorage.svg)](https://pypi.org/project/playwright-localstorage/)
[![Downloads](https://img.shields.io/pypi/dm/playwright-localstorage.svg)](https://pypi.org/project/playwright-localstorage/)
[![License](https://img.shields.io/badge/license-MIT-green)](https://github.com/swimmwatch/playwright-localstorage/blob/master/LICENSE)

Extension for the Playwright package that allows access to the Web Storage API.

## Installation

```shell
pip install playwright-localstorage
```

## Usage

### Synchronous

```python
from playwright.sync_api import Playwright
from playwright.sync_api import sync_playwright

from playwright_localstorage import LocalStorageAccessor


def run(p: Playwright):
    chromium = p.chromium
    browser = chromium.launch(headless=False)
    
    page = browser.new_page()
    page.goto("http://example.com")
    
    accessor = LocalStorageAccessor(page)
    
    accessor.set("token", "secret-token")  # Set value
    token = accessor.get("token")          # Get value
    
    print(token)                           # >> "secret-token"
    
    exists = accessor.has("token")         # Check key for existence
    
    print(exists)                          # >> True
    
    keys = accessor.keys()                 # Get all keys
    
    print(keys)                            # >> ["token"]
    
    items = accessor.items()               # Get all items
    
    print(items)                           # >> {"token": "secret-token"}
    
    accessor.remove("token")               # Remove key
    
    exists = accessor.has("token")
    
    print(exists)                          # >> False
    
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

```

### Asynchronous

The package supports asynchronous implementation.
