# Proyecto FastAPI

Este es un proyecto básico utilizando **FastAPI** para crear una API RESTful

## Requisitos

- Python 3.7 o superior
- Pip (gestor de paquetes de Python)
- Docker

## Instalación

1. **Clona el repositorio:**
  ```bash
   git clone https://github.com/juanfes517/talentoB-pagos-digitales.git
   cd talentoB-pagos-digitales
  ```

2. **Crea un entorno virtual (Windows):**
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

5. **Configuración de las variables de entorno. Crea un archivo <.env> en la raiz del proyecto con las siguientes variables:**
  ```bash
  MYSQL_USER=
  MYSQL_DATABASE=
  MYSQL_ROOT_PASSWORD=

  DB_PORT=
  APP_PORT=
  HOST=

  JWT_SECRET_KEY=
  JWT_ALGORITHM=
  ACCESS_TOKEN_EXPIRE_MINUTES=
  ```

## **Ejecuta la aplicación:**
  - Si no tienes Docker en tu maquina:
  ```bash
  uvicorn main:app --reload
  ```
  - Si tienes Docker, puedes usar el sisguinete comando en la raiz del proyecto:
  ```bash
  docker compose up -d
  ```

## Estructura del proyecto:
```
fastapi-project/
│
├── app/                    # Código de la aplicación
│   ├── __init__.py
│   ├── main.py             # Punto de entrada de la aplicación
│   ├── database.py         # Configuración de la base de datos
│   ├── models/             # Modelos de la base de datos
│   ├── schemas/            # Esquemas
│   ├── crud/               # Lógica de acceso a la base de datos
│   ├── routers/            # Endpoints de la API
│   ├── security/           # Autenticación
│   └── utils/              # Utilidades generales (validaciones, excepciones)
│
├── docker-compose.yml      # Servicios de Docker compose
├── Dockerfile              # Dockerfile para la aplicación
├── requirements.txt        # Dependencias de Python
├── README.md               # Este archivo
└── tests/                  # Pruebas unitarias
```

## Endpoints principales

### `POST /auth/login`
Autentica a un usuario y devuelve un token de acceso JWT.

Ejemplo de solicitud:
```json
{
  "username": "testuser",
  "password": "password123"
}
```

Respuesta exitosa:
```json
{
  "access_token": "your-jwt-token",
  "token_type": "bearer"
}
```

### `POST /bank_account/payments`
Realiza un pago desde una cuenta bancaria.

Ejemplo de solicitu:
```json
{
  "user_id": 1,
  "amount": 1000
}
```

Respuesta exitosa:
```json
{
  "status": "Successful",
  "data": {
    "user_id": 1,
    "new_balance": 5000.00
  }
}
```