FROM python:3.7
ENV TZ America/Sao_Paulo
ENV PYTHONPATH /app

WORKDIR /app
COPY Pipfile ./

RUN pip install pipenv
RUN pipenv install --skip-lock --system --dev

COPY . .

ENTRYPOINT python server.py
