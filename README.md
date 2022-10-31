# MError

## Virtual Environment Setup

Cd into project directory

Run these commands to setup, activate and deactivate virtual environment
```
virtualenv venv
venv\scripts\activate
deactivate
```

## Installing dependencies

All dependencies have been added to the requirements.txt file

Note: Edit requirements.txt with new dependencies as the application needs more
```
pip install -r requirements.txt
```

## Django Run-time commands
Note: Migration commands only required when changes made to the data models/database
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```