# fiuber-back-fastapi

Agregar una biblioteca/dependencia con poetry (por ejemplo, Pandas):
```
poetry add pandas==1.5.0
```
Mas docs en https://python-poetry.org/docs/cli

Para exportar un `requirements.txt` en un ambiente de poetry, corremos:
```
poetry export --without-hashes --format=requirements.txt > requirements.txt
```
