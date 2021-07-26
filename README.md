# ETLTools-

## Activate Virtual env:
```
virtualenv venv
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt 
```

## install and open notebook from the virtual environment:
```
python -m pip install ipykernel
ipython kernel install --user --name=RecommederSystem
jupyter lab &
```

## Poetry dependencies:
```
poetry install
```