# DungeonMasterIA

Proyecto base para una aplicación con un backend en FastAPI, un frontend JavaScript y una base de datos MySQL, preparado para ejecutarse con Docker Compose.

## Estructura del proyecto

- `/API`: contiene el API desarrollado con [FastAPI](https://fastapi.tiangolo.com/). Su contenedor escucha en el puerto `8000`.
- `/FRONT`: contiene el proyecto frontend. Docker levanta un entorno Node.js para alojar una aplicación creada con un framework como Angular, React o Vue. Su contenedor escucha en el puerto `3000`.
- `docker-compose.yml`: configura todos los servicios necesarios para el entorno de desarrollo.

## Requisitos

- [Docker](https://docs.docker.com/get-docker/)
- Docker Compose, incluido en Docker Desktop y en las versiones actuales de Docker mediante el comando `docker compose`

## Levantar el proyecto

Desde la carpeta raíz del proyecto, donde se encuentra `docker-compose.yml`, ejecuta:

```bash
docker compose up --build
```

La opción `--build` construye o actualiza las imágenes de los servicios. Para iniciar los contenedores en segundo plano:

```bash
docker compose up --build -d
```

Una vez levantado el entorno, los servicios estarán disponibles en:

- API FastAPI: http://localhost:8000
- Documentación interactiva de FastAPI: http://localhost:8000/docs
- Frontend: http://localhost:3000
- phpMyAdmin: http://localhost:8080
- MySQL desde el equipo local: puerto `3307`

## Detener el proyecto

Para detener los contenedores sin eliminar los datos de MySQL:

```bash
docker compose down
```

Para detenerlos y eliminar también el volumen de la base de datos:

```bash
docker compose down -v
```

## Servicios configurados

| Servicio | Tecnología | Puerto local | Descripción |
| --- | --- | --- | --- |
| `db` | MySQL 8.0 | `3307` | Base de datos de la aplicación |
| `phpmyadmin` | phpMyAdmin | `8080` | Gestión de MySQL desde el navegador |
| `api` | FastAPI + Python 3.11 | `8000` | API backend |
| `front` | Node.js 20 | `3000` | Aplicación frontend |

El backend se conecta a MySQL usando la siguiente configuración interna de Docker Compose:

```text
Host: db
Puerto: 3306
Base de datos: mi_base_datos
Usuario: platano_user
Contraseña: platano_password
```

Los directorios `/API` y `/FRONT` están montados como volúmenes, por lo que los cambios realizados localmente se reflejan dentro de los contenedores durante el desarrollo.

## Comandos útiles

Ver el estado de los servicios:

```bash
docker compose ps
```

Ver los logs de todos los servicios:

```bash
docker compose logs -f
```

Ver únicamente los logs del API o del frontend:

```bash
docker compose logs -f api
docker compose logs -f front
```
