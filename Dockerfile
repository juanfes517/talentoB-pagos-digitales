FROM python:3.9.20-slim-bullseye

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

# Usa una versión oficial de Python basada en slim
# FROM python:3.9.20-slim-bullseye

# # Instalar las dependencias necesarias (como Rust y build-essential)
# RUN apt-get update \
#     && apt-get install -y --no-install-recommends \
#     build-essential \
#     rustc \
#     cargo \
#     && rm -rf /var/lib/apt/lists/*  # Limpiar la caché de apt para reducir el tamaño de la imagen

# # Establecer el directorio de trabajo
# WORKDIR /app

# # Copiar el archivo de requerimientos
# COPY requirements.txt .

# # Instalar las dependencias de Python
# RUN pip install --no-cache-dir -r requirements.txt

# # Copiar el resto de la aplicación
# COPY . /app

# # Exponer el puerto 8000 para acceder a la API
# EXPOSE 8000

# # Comando para ejecutar FastAPI con Uvicorn
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]