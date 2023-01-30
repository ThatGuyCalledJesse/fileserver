@echo off
if not defined venv_path (
if not exist env (
python -m venv env
)
set "venv_path=%cd%\env"
call %venv_path%\Scripts\activate.bat
pip install -r requirements.txt
pip install flask
)

python server.py