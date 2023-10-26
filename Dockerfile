# syntax=docker/dockerfile:1

FROM python:alpine

WORKDIR /

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "gunicorn", "-w", "4", "--bind=0.0.0.0:5000", "wsgi:app"]
