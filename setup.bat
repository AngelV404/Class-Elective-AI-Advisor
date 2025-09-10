@echo off
SETLOCAL

:: Check Python is installed
python --version >nul 2>&1 || (
    echo Python is not installed or not in PATH.
    exit /b 1
)

:: Create virtual environment
python -m venv venv

:: Activate virtual environment
call venv\Scripts\activate

:: Upgrade pip
python -m pip install --upgrade pip

:: Install dependencies
pip install -r requirements.txt

echo Setup complete! Activate the virtual environment with: venv\Scripts\activate.bat

ENDLOCAL
pause
