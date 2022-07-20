FROM python:3.8

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install --upgrade pip && \ 
    pip3 install -r requirements.txt

# ENV PYTHONUNBUFFERED=1 \
#     DEBUG=True \
#     PORT=8000

ENV PORT=8000

COPY . .

# EXPOSE 8000

# RUN python manage.py runserver
CMD python3 manage.py runserver 0.0.0.0:$PORT
# CMD python3 manage.py runserver 127.0.0.1:$PORT
# CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:${PORT}