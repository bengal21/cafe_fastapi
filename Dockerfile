FROM ubuntu

WORKDIR /app

RUN apt-get update

RUN apt-get install -y python3 python3-pip

COPY ./requirements.txt /app
#COPY ./src/db_creation.py /app
RUN pip3 install -r /app/requirements.txt

COPY . /app/

#RUN python3 /app/src/db_creation.py

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]