FROM python:3.7.4-slim-stretch

RUN apt-get update && apt-get install -y \
    python-dev python-pip python-setuptools locales locales-all
ENV LC_ALL es_ES.UTF-8
ENV LANG es_ES.UTF-8
ENV LANGUAGE es_ES.UTF-8
RUN pip install scrapy psycopg2-binary python-dotenv
COPY . /app
WORKDIR /app/vosmovies
EXPOSE 5432

