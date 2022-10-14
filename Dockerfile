FROM ubuntu:22.10
COPY . /app
WORKDIR /app
SHELL ["/bin/bash", "-c"]
RUN apt-get update && apt-get install -y postgresql postgresql-contrib python3-pip mysql-client
RUN pip3 install --upgrade pip
RUN pip3 install virtualenv
RUN virtualenv venv
RUN source venv/bin/activate
RUN pip3 install -r requirements.txt
VOLUME /app/Backups
CMD python3 backup.py
