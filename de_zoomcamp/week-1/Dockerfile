FROM python:3.9.1

WORKDIR /app

RUN apt-get install wget
RUN pip install pandas sqlalchemy psycopg2
COPY etl.py etl.py

ENTRYPOINT ["python", "etl.py"]
