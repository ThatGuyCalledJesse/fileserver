@echo off
if not exist env_windows (
    python -m venv env_windows
    pip install -r requirements.txt
)
set "venv_path=%cd%\env_windows"
call %venv_path%\Scripts\activate.bat
python server.py