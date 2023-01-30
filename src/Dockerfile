FROM python:3.10

WORKDIR /app

COPY .. .

COPY posts.csv /posts.csv

RUN pip install -r requirements.txt

ENV PYTHONPATH "${PYTHONPATH}:/app"

CMD ["python","main.py"]