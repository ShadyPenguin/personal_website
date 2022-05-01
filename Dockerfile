# syntax=docker/dockerfile:1
FROM python:3.9.6-alpine as django_builder
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
# Prevents Python from writing pyc files to disk
ENV PYTHONDONTWRITEBYTECODE 1
# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1
# TODO: Don't copy everything
COPY personal_website personal_website
COPY mentoring mentoring
COPY manage.py manage.py
EXPOSE 8000
RUN python manage.py collectstatic --noinput
CMD gunicorn personal_website.wsgi:application --bind 0.0.0.0:8000