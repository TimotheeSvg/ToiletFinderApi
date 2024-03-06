FROM python:3

RUN apt-get install && apt-get update

WORKDIR /usr/src/app

COPY /api .

RUN pip install --no-cache-dir -r requirements.txt
RUN python manage.py migrate

EXPOSE 8000
