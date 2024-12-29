SRC_DIR=.
TESTS_DIR=tests
REFERENCES_DIR=docs/references
PACKAGE_DIR=playwright_localstorage

mypy:
	poetry run mypy --config formatters-cfg.toml $(SRC_DIR)

flake:
	poetry run flake8 --toml-config formatters-cfg.toml $(SRC_DIR)

doc-lint:
	poetry run lazydocs --validate --output-path $(REFERENCES_DIR) $(SRC_DIR)

black:
	poetry run black --config formatters-cfg.toml $(SRC_DIR)

poetry-check:
	poetry check

black-lint:
	poetry run black --check --config formatters-cfg.toml $(SRC_DIR)

isort:
	poetry run isort --settings-path formatters-cfg.toml $(SRC_DIR)

format: black isort

remove-docs:
	rm -rf $(REFERENCES_DIR)/tests.* $(REFERENCES_DIR)/playwright_localstorage.md

build:
	poetry build

lint: flake mypy black-lint poetry-check doc-lint remove-docs

test:
	poetry run pytest --browser firefox webkit chromium --cov=playwright_localstorage -n logical $(TESTS_DIR)

install:
	poetry install --no-root

lock:
	poetry lock --no-update

browser-install:
	poetry run playwright install

mkdocs-serve:
	poetry run mkdocs serve

mkdocs-deploy:
	poetry run mkdocs gh-deploy --force
