FROM python:3.11-slim

RUN pip install pipenv

WORKDIR /app

COPY Pipfile* ./

RUN mkdir ./.venv

RUN pipenv install

COPY . /app

EXPOSE 80

ENTRYPOINT ["pipenv"]
CMD [ "run", "server" ]
