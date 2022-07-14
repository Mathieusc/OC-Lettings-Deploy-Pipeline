FROM python:3.8

WORKDIR /app

ENV PYTHONUNBUFFERED=1 \
    DEBUG=False \
    PORT=8000

ADD . /app

RUN pip install --upgrade pip &&\ 
    pip install -r requirements.txt

EXPOSE 8000

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:${PORT}