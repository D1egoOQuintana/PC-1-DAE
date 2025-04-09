# Gestión de Contactos

Este es un proyecto de gestión de contactos desarrollado con Django. La aplicación permite a los usuarios crear, listar, editar y eliminar contactos de manera sencilla.

## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

```
gestion-contactos/
├── contactos/                # Aplicación principal para la gestión de contactos
│   ├── migrations/           # Migraciones de la base de datos
│   ├── templates/            # Plantillas HTML
│   ├── __init__.py
│   ├── admin.py              # Configuración del panel de administración
│   ├── apps.py               # Configuración de la aplicación
│   ├── models.py             # Modelos de datos
│   ├── tests.py              # Pruebas unitarias
│   ├── urls.py               # Rutas de la aplicación
│   └── views.py              # Vistas de la aplicación
├── gestion_contactos/        # Configuración del proyecto Django
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py           # Configuración del proyecto
│   ├── urls.py               # Rutas principales del proyecto
│   └── wsgi.py
├── static/                   # Archivos estáticos
│   └── css/
│       └── styles.css        # Estilos CSS
├── db.sqlite3                # Base de datos SQLite
├── manage.py                 # Script de gestión del proyecto
├── Procfile                  # Archivo para el despliegue en producción
├── requirements.txt          # Dependencias del proyecto
└── README.md                 # Documentación del proyecto
```

## Funcionalidades

- **Listar Contactos**: Visualiza todos los contactos almacenados.
- **Crear Contacto**: Permite agregar un nuevo contacto.
- **Editar Contacto**: Modifica la información de un contacto existente.
- **Eliminar Contacto**: Elimina un contacto después de una confirmación.

## Despliegue

Para desplegar la aplicación en Render.com, asegúrate de:

1. Configurar `ALLOWED_HOSTS` en `settings.py` para incluir el dominio de Render.
2. Asegurarte de que los archivos estáticos se sirvan correctamente, configurando `STATIC_URL` y `STATIC_ROOT`.
3. Incluir `whitenoise` en `requirements.txt` para manejar archivos estáticos en producción.

## Instalación

1. Clona el repositorio:
   ```
   git clone <URL_DEL_REPOSITORIO>
   cd gestion-contactos
   ```

2. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```

3. Realiza las migraciones de la base de datos:
   ```
   python manage.py migrate
   ```

4. Ejecuta el servidor de desarrollo:
   ```
   python manage.py runserver
   ```

Accede a la aplicación en `http://127.0.0.1:8000/`.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas colaborar, por favor abre un issue o envía un pull request.