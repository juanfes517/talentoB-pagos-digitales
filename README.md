# Proyecto Prueba Técnica Talento B

Este proyecto es el desarrollo de la prueba técnica para Talento B - Bancolombia. El objetivo del proyecto es crear una API que permita la autenticación de usuarios y simular los pagos que realizan.

Actualmente la aplicación se encuentra desplegada en AWS y podrá acceder a través de este [enlace.](http://18.220.201.115:8000/docs#/) 

## Requisitos

- Python 3.7 o superior
- Pip (gestor de paquetes de Python)
- Docker

## Instalación

### Opción 1: Usando Docker compose

**Clona el repositorio:**
  ```bash
   git clone https://github.com/juanfes517/talentoB-pagos-digitales.git
   cd talentoB-pagos-digitales
  ```

**Ejecuta el docker compose:**
  ```bash
  docker compose up -d
  ```

### Opción 2: Usando uvicorn 

**Clona el repositorio:**
  ```bash
   git clone https://github.com/juanfes517/talentoB-pagos-digitales.git
   cd talentoB-pagos-digitales
  ```

**Instala las dependencias:**
  ```bash
  pip install --no-cache-dir -r requirements.txt
  ```

**Ejecuta el proyecto:**
  ```bash
  uvicorn app.main:app --reload
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

Para realizar pruebas, usar uno de los siguiente usuarios:
|ID |   User   | Password  |
|---|----------|-----------|
| 1 | user_0   |   1234    |
| 2 | user_1   |   1234    |
| 3 | user_2   |   1234    |
| 4 | user_3   |   1234    |
| 5 | user_4   |   1234    |

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


## Información de contacto
- **Nombre:** Juan Felipe Escobar Rendón
- **Correo Electrónico:** juanfes517@gmail.com
- **Teléfono:** 320 881 7689