FROM python:3.10.3


ENV PYTHONBUFFERED 1

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Explicitly install keras and tensorflow
RUN pip install keras tensorflow
RUN pip install --no-cache-dir mysql-connector-python

COPY . /app/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
