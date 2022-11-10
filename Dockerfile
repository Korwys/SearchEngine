FROM python:3.10

WORKDIR /app

COPY . .

#COPY ./requirements.txt /requirements.txt
#COPY ./alembic.ini /alembic.ini
#COPY ./.env /.env
COPY ./posts.csv /posts.csv

RUN pip install -r requirements.txt

CMD ["python","main.py"]


#CMD ["uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8000"]

# If running behind a proxy like Nginx or Traefik add --proxy-headers
# CMD ["uvicorn", "main:app", d"--host", "0.0.0.0", "--port", "80", "--proxy-headers"]