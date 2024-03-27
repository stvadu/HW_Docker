FROM python:3.10
WORKDIR /usr/src/app
ADD DJ-HW-5 /usr/src/app
RUN pip install django djangorestframework psycopg2-binary
RUN python manage.py migrate
EXPOSE 7000
CMD python manage.py runserver 0.0.0.0:7000
