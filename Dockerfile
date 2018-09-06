FROM ubuntu:16.04
COPY . /app
WORKDIR /app
SHELL ["/bin/bash", "-c"]
RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ xenial-pgdg main" > /etc/apt/sources.list.d/pgdg.list
RUN apt-get update && apt-get install -y postgresql-10 python3-pip
RUN which pg_dump
RUN pip3 install --upgrade pip
RUN pip3 install virtualenv
RUN virtualenv venv
RUN source venv/bin/activate
RUN pip3 install -r requirements.txt
VOLUME /app/Backups
CMD python3 backup.py