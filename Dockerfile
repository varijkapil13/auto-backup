FROM python:3.6
COPY . /app
WORKDIR /app
SHELL ["/bin/bash", "-c"]
RUN deb http://apt.postgresql.org/pub/repos/apt/ xenial-pgdg main
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -
RUN apt-get update && apt-get install -y postgresql-client-10
RUN pip install virtualenv
RUN virtualenv venv
RUN source venv/bin/activate
RUN pip install -r requirements.txt
VOLUME /app/Backups
CMD python3 backup.py