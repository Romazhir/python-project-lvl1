install:
	poetry install

brain-games:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-uninstall:
	python3 -m pip uninstall hexlet-code

package-reinstall:
	pip install --user --force-reinstall dist/*.whl

make lint:
	poetry run flake8 brain_games

brain-even:
	poetry run brain-even
