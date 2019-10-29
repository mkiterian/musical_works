FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /musical_works
WORKDIR /musical_works

RUN pip install pipenv

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

RUN pipenv install --system --deploy --ignore-pipfile

COPY . /musical_works