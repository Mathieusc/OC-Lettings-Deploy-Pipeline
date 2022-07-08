FROM python:3.8

WORKDIR /app

ADD . /app

RUN pip install --upgrade pip &&\ 
    pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]