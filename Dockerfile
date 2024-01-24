FROM ubuntu

WORKDIR /app

RUN apt-get update

RUN apt-get install -y python3 python3-pip

COPY ./requirements.txt /app

RUN pip3 install -r /app/requirements.txt

COPY . /app/

#RUN alembic upgrade 7622307d6eae

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]