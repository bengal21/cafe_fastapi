# Чтобы запустить проект склонируйте репозиторий, а потом можете воспользоваться одним из нескольких способов.

## Способ первый:
разверните базу данных следующей командой (можете использовать любой образ):

````
docker run --name db_for_cafe -p 555:5432 -e POSTGRES_PASSWORD=postgres -d postgres:16

````
запусти следующие команды:
````
pip intall -r requirements.txt
````
````
alembic upgrade 7622307d6eae
````
````
uvicorn src.main:app --reload
````

## Способ второй:

можете использовать свою базу данных с данными из файла 
### .env

далее запустить команды:
````
pip intall -r requirements.txt
````
````
alembic upgrade 7622307d6eae
````
````
uvicorn src.main:app --reload
````
## После запуска проекта документацию можно посмотреть по адресу:
### http://localhost:8000/docs

