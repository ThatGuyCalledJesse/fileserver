#!/bin/bash

venv_name="env"

# check if the venv already exists
if [ ! -d "$venv_name" ]; then
    # create a new venv
    python3 -m venv "$venv_name"
fi

# activate the venv
source "$venv_name/bin/activate"

# run the server
python3 server.py
