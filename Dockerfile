From python:3

WORKDIR /app

ENV MYSQL_URL_PATTERN=mysql://peter:Pass_123@13.233.83.152/flask

copy ./requirements.txt ./

RUN pip install -r requirements.txt

EXPOSE 5000

COPY . ./

cmd python app.py