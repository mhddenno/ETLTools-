# ETLTools-

## Activate Virtual env:
```
virtualenv --python=/usr/bin/python3* venv
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt 
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