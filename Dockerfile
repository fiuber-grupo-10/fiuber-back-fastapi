FROM python:3.9

RUN apt update -y

WORKDIR /fiuber-back-fastapi

COPY ./requirements.txt /fiuber-back-fastapi/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /fiuber-back-fastapi/requirements.txt
RUN pip install pytest

COPY ./app /fiuber-back-fastapi/app
