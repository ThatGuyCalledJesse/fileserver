#!/bin/bash

if [ ! -d "env" ]; then
python -m venv env
venv_path=$(pwd)/env
source $venv_path/bin/activate
pip install -r requirements.txt
pip install flask
python server.py
else
venv_path=$(pwd)/env
source $venv_path/bin/activate
python server.py
fi