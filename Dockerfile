FROM python

WORKDIR ./maria

RUN apt update
RUN apt install nano

COPY . .

RUN pip install Django
RUN pip install sqlparse

CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000