REM filepath: d:\current\code\tebar-software\ts_v5\scripts\recreate_venv.bat
@echo off
set "PYTHON_EXE=d:\python\python.exe"

if not exist "%PYTHON_EXE%" (
  echo ERROR: Global python not found at %PYTHON_EXE%
  exit /b 1
)

REM Change to repo root (script is in scripts)
pushd "%~dp0..\\"

set "VENV_DIR=%cd%\ts_v5_venv"

REM Remove existing venv (optional)
if exist "%VENV_DIR%" (
  rmdir /s /q "%VENV_DIR%"
)

REM Create venv using specified global python and allow access to global site-packages
"%PYTHON_EXE%" -m venv "%VENV_DIR%" --system-site-packages
if %ERRORLEVEL% neq 0 (
  popd
  exit /b %ERRORLEVEL%
)

REM Check if venv is already active
if "%VIRTUAL_ENV%"=="%VENV_DIR%" (
  echo Virtual environment already active, skipping activation.
) else (
  call "%VENV_DIR%\Scripts\activate.bat"
)

python -m pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

popd
echo Virtual environment created at %VENV_DIR% and requirements installed.
exit /b 0