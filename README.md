# playwright-localstorage

<!-- markdownlint-disable -->
![playwright-localstorage](https://socialify.git.ci/swimmwatch/playwright-localstorage/image?description=1&font=Raleway&language=1&name=1&owner=1&pattern=Brick%20Wall&theme=Dark)

<div align="center">
  <p>
    <a href="https://pypi.org/project/playwright-localstorage">
        <img src="https://img.shields.io/pypi/v/playwright-localstorage.svg" alt="PyPI">
    </a>
    <a href="pyproject.toml">
        <img src="https://img.shields.io/pypi/pyversions/playwright-localstorage" alt="Supported Python Versions">
    </a>
    <br/>
    <a href="LICENSE">
        <img src="https://img.shields.io/github/license/swimmwatch/playwright-localstorage" alt="License">
    </a>
    <a href="https://github.com/ambv/black">
        <img src="https://img.shields.io/badge/code%20style-black-black" alt="Code style">
    </a>
    <a href="https://github.com/pycqa/flake8">
        <img src="https://img.shields.io/badge/lint-flake8-black" alt="Linter">
    </a>
    <a href="https://github.com/python/mypy">
        <img src="https://img.shields.io/badge/type%20checker-mypy-black" alt="Type checker">
    </a>
    <a href="https://snyk.io/advisor/python/playwright-localstorage">
        <img src="https://snyk.io/advisor/python/playwright-localstorage/badge.svg" alt="Package health">
    </a>
    <br/>
    <a href="https://github.com/swimmwatch/playwright-localstorage/actions/workflows/python-check.yml">
        <img src="https://github.com/swimmwatch/playwright-localstorage/actions/workflows/python-check.yml/badge.svg" alt="Tests">
    </a>
    <a href="https://coverage-badge.samuelcolvin.workers.dev/redirect/playwright-localstorage/playwright-localstorage" target="_blank">
        <img src="https://coverage-badge.samuelcolvin.workers.dev/playwright-localstorage/playwright-localstorage.svg" alt="Coverage">
    </a>
    <a href="https://github.com/swimmwatch/playwright-localstorage/actions/workflows/release.yml">
        <img src="https://github.com/swimmwatch/playwright-localstorage/actions/workflows/release.yml/badge.svg" alt="Release">
    </a>
    <a href="https://github.com/swimmwatch/playwright-localstorage/actions/workflows/docs.yml">
        <img src="https://github.com/swimmwatch/playwright-localstorage/actions/workflows/docs.yml/badge.svg" alt="Docs">
    </a>
  </p>
</div>
<!-- markdownlint-enable -->

Extension for the Playwright package 
that allows access to the [Web Storage API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Storage_API).

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
