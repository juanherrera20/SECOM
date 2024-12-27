# Proyecto Backend/Frontend - Django con DRF y Vue.js

Este proyecto combina un backend en Django (rest framework) y un frontend en Vue.js en un único repositorio para facilitar la gestión y despliegue.

## Estructura del proyecto

```Renta_Casa/
├── Backend/
│   ├── core/                  # Configuración principal de Django
│   │   ├── settings.py        # Configuración general del proyecto
│   │   ├── urls.py            # Enrutamiento del proyecto
│   │   ├── wsgi.py            # Configuración WSGI para despliegue
│   │   ├── asgi.py            # Configuración ASGI para websockets y más
│   │   └── __init__.py        # Archivo de inicialización del módulo
│   ├── apps/                  # Aplicaciones Django personalizadas
│   │   └── (tu aplicación aquí) 
│   ├── env/                   # Entorno virtual (no se incluye en Git)
│   ├── manage.py              # Script principal para gestionar Django
│   └── requirements.txt       # Dependencias del proyecto Django
├── Frontend/
│   ├── public/                # Archivos públicos accesibles desde el navegador
│   ├── src/                   # Código fuente del proyecto Vue.js
│   │   ├── components/        # Componentes reutilizables de Vue.js
│   │   ├── views/             # Vistas específicas del proyecto
│   │   ├── router/            # Configuración de enrutamiento Vue.js
│   │   ├── store/             # Gestión del estado (Vuex o Pinia)
│   │   └── main.js            # Punto de entrada del proyecto
│   ├── node_modules/          # Dependencias de Node.js (no se incluye en Git)
│   ├── package.json           # Dependencias y scripts del proyecto
│   ├── package-lock.json      # Archivo de bloqueo para npm
│   ├── .env                   # Variables de entorno para Vue.js
│   └── vite.config.js         # Configuración de Vite (o Webpack)
├── .gitignore                 # Archivos y carpetas a ignorar en Git
└── README.md                  # Documentación del proyecto
```

## Requisitos

- Python 3.12.6
- Django 5.1.3
- Node.js 22.11.0 o superiores
- vue 5.0.8 o superiores
- PostgreSQL/mysql (Aun no esta decidido)


## Instalación

1. Clona este repositorio:

    ```bash
    git clone https://github.com/juanherrera20/Renta_Casa
    cd Renta_Casa
    ```

2. Crea y activa un entorno virtual:

    - En Windows:

        ```bash
        python -m venv env
        venv\Scripts\activate
        ```

    - En macOS/Linux:

        ```bash
        python3 -m venv env
        source venv/bin/activate
        ```

3. Instala las dependencias:

    En la carpeta donde se desea crear usar el siguiente comando para crear el archivo: 

    ```bash
    pip freeze > requirements.txt
    ```

    ```bash
    pip install -r requirements.txt
    ```

4. Configura las variables de entorno (por ejemplo, en un archivo `.env`):

    - `DEBUG=True`
    - `SECRET_KEY=<tu_clave_secreta>`
    - `DATABASE_URL=<url_de_tu_base_de_datos>`

5. Realiza las migraciones de la base de datos:

    ```bash
    python manage.py makemigrations
    ```

    ```bash
    python manage.py migrate
    ```

6. Ejecuta el servidor de desarrollo:

    ```bash
    python manage.py runserver
    ```

## Endpoints de la API

- Sin definir
- ...


