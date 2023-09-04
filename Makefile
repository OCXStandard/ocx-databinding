# A self-documenting Makefile
# You can set these variables from the command line, and also
# from the environment for the first two.

SOURCEDIR = ./ocx_generator
CONDA_ENV = generator
PYPI_USER = $(env:PYPI_USER)
PSWD = $(env:PYPI_PSWD)

# PROJECT setup using conda and powershell
.PHONY: conda-create
conda-create:  ## Create a new conda environment with the python version and basic development tools as specified in environment.yml
	@conda env create -f environment.yml

conda-upd:  ## Update the conda development environment when environment.yml has changed
	@conda env update -f environment.yml
.PHONY:conda-upd

conda-clean: ## Purge all conda tarballs, log files and caches
	conda clean -a -y
.PHONY: conda-clean

conda-activate: ## Activate the conda environment for the project
	@conda activate $(CONDA_ENV)

# Color output
BLUE='\033[0;34m'
NC='\033[0m' # No Color

check:
	@echo ${PYPI_USER}
	@echo {$PSWD}
.PHONY: check

# BUILD ########################################################################
build:   ## Build the package dist with poetry
	@poetry update
	@poetry build
.PHONY: build

publish:   ## Publish the package dist with poetry
	@poetry publish --username=$(PYPI_USER) --password=$(PSWD)
.PHONY: publish

# Poetry fix
.PHONY: poetry-fix ## In case poetry fails, update the package with this command
	@pip install poetry --upgrade

# TESTS #######################################################################

FAILURES := .pytest_cache/pytest/v/cache/lastfailed


test:  ## Run unit and integration tests
	@pytest --durations=5  --cov-report html --cov ocx_generator .
.PHONY: test

test-cov:  ## View the test coverage report
	cmd /c start $(CURDIR)/htmlcov/index.html
.PHONY: test-cov


# HELP ########################################################################


.PHONY: help
help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help

#-----------------------------------------------------------------------------------------------



