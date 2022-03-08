FROM python:3.10-buster

RUN pip install --upgrade pip

RUN mkdir /app

WORKDIR /app

ADD . .

RUN pip install -r requirements.txt

CMD gunicorn =run:app --bind 0.0.0.0:$PORT --reload

