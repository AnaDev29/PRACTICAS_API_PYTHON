@echo off
REM Verifica si venv existe
if not exist venv (
    echo Creando entorno virtual...
    python -m venv venv
)

REM Activa el entorno virtual
echo Activando entorno virtual...
call venv\Scripts\activate.bat

REM Instala/actualiza dependencias
echo Instalando dependencias...
pip install -r requirements.txt

REM Ejecuta el servidor
echo Iniciando servidor...
python main.py
pause
