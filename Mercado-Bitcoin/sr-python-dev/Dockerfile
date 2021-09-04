FROM python:3.7
ENV TZ America/Sao_Paulo

LABEL maintainer="Allan Santos <alan_souzas9@hotmail.com>"

ENV PYTHONPATH /app

WORKDIR /app
COPY Pipfile ./

RUN pip install pipenv
RUN pipenv install --skip-lock --system --dev

COPY . .

ENTRYPOINT python server.py