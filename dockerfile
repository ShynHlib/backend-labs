FROM python:3.8.8-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install -r requirements.txt

COPY . /app

CMD flask --app module/views run -h 0.0.0.0 -p 8080

