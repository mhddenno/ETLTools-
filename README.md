# ETLTools-

## Getting started
In the Docu, you will see three ways to run the API
- Using pyenv and pyenv virtualenv
- Using virtualenv alone
- Using docker

## Manage python versions:
```
pyenv install --list
pyenv install 3.9.6
```
### See the link:
[https://realpython.com/intro-to-pyenv/#why-use-pyenv]


## Activate Virtual env:
```
virtualenv --python=/usr/bin/python3* venv
python3 -m venv venv # for python 2: virtualenv env
source venv/bin/activate
```

## Using pyenv-virtualenv instead of virtual env:
```
pyenv virtualenv 3.9.6 ETLTOOLS-
pyenv local ETLTOOLS-
```

## install and open notebook from the virtual environment:
```
python -m pip install ipykernel
ipython kernel install --user --name=Something
jupyter lab &
```

## Poetry dependencies:
```
poetry install
```

## Run server:
```
FLASK_APP=run.py flask run
```

## Deactive localenv:
```
deactivate
```

## Deactive localenv in case of pyenv-virtualenv:
```
pyenv deactivate
```