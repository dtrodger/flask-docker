FROM python:3.6.1

RUN groupadd flaskgroup && \
   useradd -m -g flaskgroup -s /bin/bash flask && \
   mkdir -p /home/flask/app/web

WORKDIR /home/flask/app/web

COPY requirements.txt /home/flask/app/web
RUN pip install --no-cache-dir -r requirements.txt

COPY . /home/flask/app/web

USER flask