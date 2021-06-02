FROM python:3.7
LABEL maintainer="Allan Santos <alan_souzas9@hotmail.com>"
WORKDIR /app
COPY Pipfile ./Pipfile
RUN pip install pipenv pylint pytest
RUN pipenv install --skip-lock --system
COPY . .
ENTRYPOINT python server.py