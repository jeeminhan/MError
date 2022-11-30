# Import auth functions
from pathlib import Path
import dotenv
import numpy as np
from django.shortcuts import render
from .models import UserAccount

# IMPORTING HELPER
from .api_helpers import twitter_API, news_API, weather_API, time_API
from .user_auth_helpers import all_users, examine_user


def index(request):

    # USER SCANNING
    auth_user=examine_user()
    users=all_users()

    # API Data
    news_titles=news_API()
    tweets=twitter_API()
    date_time=time_API()
    weather=weather_API()

    # Data transformation for display
    response={"news":news_titles, "tweets":tweets,'date_time':date_time, 'weather':weather, 'users':users, 'auth_user':auth_user}

    if (auth_user[0]):
        return render(request, "auth.html", response)
    else:
        return render(request, "index.html", response)

def registrationPage(request):

    if request.method == 'POST':
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        city = request.POST['city']
        head_shot = request.POST['head_shot']

        new_user = UserAccount(email=email,first_name=first_name,last_name=last_name,city=city,head_shot=head_shot)
        new_user.save()

    return render(request, "registration.html", response)
