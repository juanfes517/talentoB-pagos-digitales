# Proyecto FastAPI

Este es un proyecto basado en FastAPI.

## Requisitos

- Python 3.7 o superior
- Pip (gestor de paquetes de Python)
- Docker

## Instalación

1. **Clona el repositorio:**
  ```bash
   git clone https://github.com/tu_usuario/tu_repositorio.git
   cd tu_repositorio
  ```

2. **Crea un entorno virtual - Windows (opcional):**
  ```bash
  python -m venv venv
  ./venv/Scripts/activate
  ```

3. **Instala las dependencias:**
  ```bash
  python -m venv venv
  ./venv/Scripts/activate
  ```

4. **Instala las dependencias:**
  ```bash
  pip install -r requirements.txt
  ```

5. **Ejecuta la aplicación:**
  - Sin Docker:
  ```bash
  uvicorn main:app --reload
  ```
  - Con Docker:
  ```bash
  docker compose up -d
  ```