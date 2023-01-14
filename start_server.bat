@echo off
set "venv_path=%cd%\env"
call %venv_path%\Scripts\activate.bat
python %cd%\server.py
