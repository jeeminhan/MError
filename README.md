# MError


# Virtual Environment Setup
virtualenv venv

venv\scripts\activate

Within the virtual environment

pip install django==4.1.2

pip install requests


Each time a change is made in the Django project concerning models/database stuff - Run all of these commands

python manage.py makemigrations

python manage.py migrate

python manage.py runserver