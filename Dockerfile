FROM python:3.9

WORKDIR /app

RUN chmod 777 /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

RUN rm -rf ./config/config.php

ADD ./config/example_config.json ./config/config.json

CMD pytest --alluredir=allure-results -n 16 --remote docker --reruns 5 --reruns-delay 5
