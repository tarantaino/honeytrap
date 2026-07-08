FROM python:3.10-slim 

WORKDIR /app

COPY requirements.txt
RUN pip instasll --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONBUFFERED=1