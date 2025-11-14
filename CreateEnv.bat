set "carpeta=%cd%\.venv"

IF EXIST %carpeta% RMDIR /S /Q %carpeta%
python -m venv %carpeta%
pause