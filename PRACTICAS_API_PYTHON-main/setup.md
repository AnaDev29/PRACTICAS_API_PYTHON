# Setup - Rick and Morty API Server

## Configuración del Entorno Virtual

### En Windows (PowerShell):

```powershell
# Crear el entorno virtual
python -m venv venv

# Activar el entorno virtual
.\venv\Scripts\Activate.ps1

# Si tienes problemas de permisos, ejecuta en PowerShell como administrador:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### En Windows (CMD):

```cmd
# Crear el entorno virtual
python -m venv venv

# Activar el entorno virtual
venv\Scripts\activate.bat
```

### En Linux/macOS:

```bash
# Crear el entorno virtual
python3 -m venv venv

# Activar el entorno virtual
source venv/bin/activate
```

## Instalación de Dependencias

Una vez activado el entorno virtual:

```bash
pip install -r requirements.txt
```

## Configuración de Variables de Entorno

1. El archivo `.env` contiene la configuración por defecto
2. El archivo `.env.local` es para desarrollo local (no se sube a git)
3. FastAPI cargará automáticamente `.env.local` si existe

## Ejecutar el Servidor

```bash
python main.py
```

O con uvicorn directamente:

```bash
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

## Acceder a la API

- **Servidor**: http://localhost:8000
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Endpoints Disponibles

### Personajes
- `GET /characters` - Obtener todos los personajes (con paginación)
- `GET /characters?name=Rick` - Buscar personajes por nombre
- `GET /characters/{id}` - Obtener un personaje específico

### Ubicaciones
- `GET /locations` - Obtener todas las ubicaciones (con paginación)
- `GET /locations?name=Earth` - Buscar ubicaciones por nombre
- `GET /locations/{id}` - Obtener una ubicación específica

### Episodios
- `GET /episodes` - Obtener todos los episodios (con paginación)
- `GET /episodes/{id}` - Obtener un episodio específico

### Salud
- `GET /health` - Verificar estado del servidor
- `GET /` - Información del servidor

## Gestión de Versiones de Python

Para trabajar con diferentes versiones de Python:

```bash
# Ver versión actual
python --version

# Crear venv con una versión específica (si está instalada)
python3.11 -m venv venv
```

## Deactivar el Entorno Virtual

```bash
deactivate
```
