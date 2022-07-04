FROM python:3.10
ENV TZ America/Sao_Paulo
ENV PYTHONPATH /app

WORKDIR /app

COPY . .

RUN pip install -r settings/requirements.txt

ENTRYPOINT python server.py
