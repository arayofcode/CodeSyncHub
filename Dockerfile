# Use an official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.12-slim

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

COPY . /app/

RUN apt-get update && apt-get install -y gcc libc-dev
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]
