# fiuber-back-fastapi

## Armado de env file

Para ir armando nuestro .env file, podemos bajarnos las env vars que estan
en el entorno de develop desde heroku, haciendo:

```
heroku config:get <NOMBRE_DE_ENV_VAR> -s -a fiuber-back-fastapi-dev-g10 >> .env
```

Asi podemos hacer con todas las variables de entorno que esten en el entorno
de desarrollo para armar nuestro env file.

## Cómo buildear y correr (docker-compose)

En la raiz del repo
```
docker-compose build
```

Luego:

```
docker-compose up
```

Como se monta el código como volumen al container, se puede desarrollar mientras corre la app.
A medida que vayamos guardando el código, se rebuildeará (flag --reload en el comando de uvicorn) automaticamente. La idea es no rebuildear la imagen cada vez que hagamos un cambio y reducir el delay entre
desarrollo y resultado.


## Cómo buildear y correr (solo docker)

Parados en la raiz del repo y con docker instalado, correr:

```
docker build -t fiuber-back-fastapi .
```

Esto nos va a crear una imagen (podemos ver las imagenes con `docker image ls`) de nombre "fiuber-back-fastapi".

Con la imagen lista, podemos levantarla haciendo:

```
docker run -it -p <puerto_container>:<puerto_local> fiuber-back-fastapi /bin/sh
```

Esto nos va a levantar una shell ya dentro del container. Docker va a mappear el puerto <puerto_container> dentro del container al puerto <puerto_local> en nuestro OS. Es decir, si mi aplicación dentro del container corre en 0.0.0.0:8000, puedo pasarle a docker run `-p 8000:8000`, y eso va a mappear el puerto 8000 del container al 8000 de nuestro OS, es decir, podremos acceder desde localhost:8000 a nuestra aplicación corriendo en el container.

Desde dentro de la shell, podemos levantar la aplicacion, pero antes, copiamos nuestro .env file al container haciendo (desde la raiz del repo):

```
docker cp ./.env <CONTAINER_ID>:/fiuber-back-fastapi
```

El container id lo podemos obtener corriendo, en otra terminal (asumiendo que tenemos corriendo un solo container):

```
docker container ls
```

Una vez que tenemos el .env dentro del container, podemos correr:

```
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

y ya tendremos escuchando a la aplicación en el puerto 8000, en localhost.

## Agregar una biblioteca/dependencia con poetry (por ejemplo, Pandas):

```
poetry add pandas==1.5.0
```
Mas docs en https://python-poetry.org/docs/cli

Para exportar un `requirements.txt` en un ambiente de poetry, corremos:
```
poetry export --without-hashes --format=requirements.txt > requirements.txt
```
