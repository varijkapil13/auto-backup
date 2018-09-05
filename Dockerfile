FROM python:3.6
COPY . /app
WORKDIR /app
RUN apt-get update && apt-get install -y postgresql-client-10
RUN pip install -r requirements.txt
VOLUME /app/Backups
VOLUME /app

CMD bash