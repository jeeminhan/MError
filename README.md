# MError

After installing the project directory follow these steps to succesfully run the program. 

## Virtual Environment Setup

First you must start the virtual environment.

Cd into project directory

Run these commands to setup, activate and deactivate virtual environment
```
virtualenv venv
venv\scripts\activate
deactivate
```

If using mac, instead of venv\scripts\activate

```
source venv/bin/activate
```

## Installing dependencies

Once in the virtual environment you'll install the needed dependencies.

All dependencies have been added to the requirements.txt file

Note: Edit requirements.txt with new dependencies as the application needs more
```
pip install -r requirements.txt
pip install requests
pip install tweepy
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
pip install python-dotenv

(in case of errors pip3 install --upgrade oauth2client)
```

Make sure you have the necessary .env file. (You may have to rename the file to .env) If using mac (⌘ + ⇧ + SHIFT) to view '.' files.

## Django Run-time commands

Run these commands to start the Django server. Go to the specified server location (i.e. http://127.0.0.1:8000/) to view the end product.

Note: Migration commands only required when changes made to the data models/database
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Notes

The main files that are being changed are the views.py and the index.html file. Look at these files if you need to add API's / change the HTML.
