#!/bin/bash

# Verifica si venv existe
if [ ! -d "venv" ]; then
    echo "Creando entorno virtual..."
    python3 -m venv venv
fi

# Activa el entorno virtual
echo "Activando entorno virtual..."
source venv/bin/activate

# Instala/actualiza dependencias
echo "Instalando dependencias..."
pip install -r requirements.txt

# Ejecuta el servidor
echo "Iniciando servidor..."
python main.py
