# Proyecto: Videojuego API & Web Service

Este proyecto consiste en una API desarrollada en Python utilizando el framework Django, diseñada para integrarse con un videojuego y servicios de servidor local (XAMPP).

## Estructura del Proyecto

* /xampp/ApiVideojuego: Contiene la lógica del servidor, modelos y controladores de la API.
* /videojuego/Lib/site-packages: Entorno virtual con las dependencias de Python (Django, Django Rest Framework)[cite: 32419, 33614].
* /MonoBleedingEdge: Archivos de soporte para el runtime de Unity/Mono[cite: 9].

## Tecnologías Utilizadas

* Lenguaje: Python 3.11[cite: 30011].
* Framework Web: Django & Django Rest Framework[cite: 32419, 33614].
* Servidor: XAMPP para la gestión de bases de datos y servicios locales[cite: 30011].
* Motor de Juego: Unity (Componentes de integración Mono)[cite: 9].

## Requisitos Previos

1.  Tener instalado Python 3.11+.
2.  XAMPP instalado y configurado.
3.  Instalar las dependencias listadas en el entorno virtual.

## Configuración e Instalación

1.  Configurar la base de datos en XAMPP (MySQL).
2.  Activar el entorno virtual ubicado en `Videojuego/xampp/ApiVideojuego/videojuego/Scripts/activate`.
3.  Ejecutar las migraciones de Django:
    python manage.py migrate
4.  Iniciar el servidor de desarrollo:
    python manage.py runserver

## Notas Adicionales
El proyecto incluye paquetes específicos para la serialización de datos y compatibilidad de API (rest_framework), lo que facilita la comunicación entre el motor del videojuego y la base de datos[cite: 32419, 33614].
