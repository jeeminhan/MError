# MError


# Virtual Environment Setup
WINDOWS

virtualenv venv
venv\scripts\activate

Within the virtual environment
pip install django==4.1.2
pip install requests


Each time a change is made in the Django project - Run these three commands
python manage.py makemigrations
python manage.py migrate
python manage.py runserver