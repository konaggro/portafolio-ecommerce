PORTAFOLIO M6 - Sistema de Autenticación Django

DESCRIPCION

El proyecto que se desarollo en Django implementa un sistema de autenticacion e usuarios.
En este se uso:

-Registro de usuarios
-Inicio de sesión
-Cierre de sesión
-Vista protegida para usuarios autenticados

REQUISITOS

-Python 3.x
-Django 6.x

INSTALACION 

-descargar el proyecto.
-Crear entorno virtual:

    python -m venv env
    Activar entorno virtual:
    env\Scripts\activate

Instalar dependencias:

    pip install django

Ejecutar migraciones:

    python manage.py migrate

Iniciar servidor:

    python manage.py runserver

Rutas principales

Inicio:
/

Registro:
/registro/

Login:
/accounts/login/

Panel protegido:
/panel/

Usuario: Javiera
Contraseña: channie0310