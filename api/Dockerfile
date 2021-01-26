FROM python:3.8.7-buster
EXPOSE 8000
ADD . /usr/api
WORKDIR /usr/api
RUN apt-get update &&\
    pip install 'poetry==1.1.4' &&\
    poetry install

CMD poetry run uvicorn main:app --reload --port 8000 --host 0.0.0.0