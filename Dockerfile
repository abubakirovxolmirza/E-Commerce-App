FROM python:3.11-alpine

RUN pip install --upgrade pip

WORKDIR /commerce
COPY . /comerce

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]