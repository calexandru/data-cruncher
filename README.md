# DataCruncher

## Description

Data Cruncher- CLI tool.

Project requirements: python 3.8+

## Usage

### From local project

* ``python wayf -f <file_path>``

> note:: Checkout the CLI help section

* ``python wayf --help``

> note:: Example

* ``python wayf -f ~/input/input1.txt -s 2020 -m pair``

### From Git

> note:: You need to have Python 3.8+ installed and accessible in your path

* ``pip install git+https://github.com/calexandru/data-cruncher@master``
* ``wfcli -f ~/input/input1.txt``
* ``wfcli -f ~/input/input1.txt -m trio``

## Local development

For a more lightweight local development it is recommended to use python virtual environment.

### Using pyenv

* ``curl https://pyenv.run | bash`` Install pyenv if you don't have it already (https://github.com/pyenv/pyenv)

> note:: If you are using zsh execute the script above using zsh rather than bash
> note:: Run ``pyenv init`` and follow the instruct1ions to enable pyenv in your terminal

* ``pyenv install 3.8.10 -s`` Ensure Python 3.8 is available in the Pyenv versions
* ``cd`` into your local project directory
* ``pyenv local 3.8.10`` Activate Python 3.8 for the current project (each time you cd to the project the default Python interpreter will be python3.8.10)
* ``pip install -r requirements-dev.txt`` Install project dependencies

### Using virtualenv

> note:: You need to have Python 3.8+ installed and accessible in your PATH

* ``python3 -m venv .venv`` Create a new Python virtual environment
* ``source app-venv/bin/activate`` Activate the Python 3.8 virtual environment
* ``pip install -r requirements-dev.txt`` Install project dependencies

## Install Git pre-commit hooks

For a clean development and to ensure the quality of the code commits it is highly recommended to install

> note:: there should be an existent Git repository - ``git init``

``pre-commit install`` This will add git pre commit hooks

## Test application

``pytest`` (run existing test suite).

## Run code style checks

``pre-commit run --all-files``
