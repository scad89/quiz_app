FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app
RUN pip3 install --upgrade pip -r requirements.txt

EXPOSE 5000

COPY . /usr/src/app



