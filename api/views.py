from urllib import response
from django.shortcuts import render
import dotenv
import os
import requests
import tweepy
from pathlib import Path

# Create your views here.
BASE_DIR = Path(__file__).resolve().parent.parent
dotenv_file = os.path.join(BASE_DIR, ".env")
if os.path.isfile(dotenv_file):
        dotenv.load_dotenv(dotenv_file)
NEWS_API_KEY = os.environ['NEWS_API_KEY']
BEARER_TOKEN = os.environ['BEARER_TOKEN']
WEATHER_API_KEY = os.environ['WEATHER_API_KEY']

def index(request):
    # API function
    news_titles=news_API()
    tweets=twitter_API()
    date_time=time_API()
    weather=weather_API()
    users=all_users()

    # Data transformation for display
    response={"news":news_titles, "tweets":tweets,'date_time':date_time, 'weather':weather, 'users':users}

    return render(request, "index.html", response)

# HELPER FUNCTIONS TO PERFORM AND PROCESS THE API requests
def news_API():

    # Link for making request
    url="https://newsapi.org/v2/top-headlines?country=us&apiKey="+NEWS_API_KEY

    news=requests.get(url).json()

    # Storing the top headings
    titles=[]

    for i in range(5):
        titles+=[news['articles'][i]['title']]
    
    return titles

def twitter_API():
    # Link for making request
    client = tweepy.Client(bearer_token=BEARER_TOKEN)
    query = 'from:elonmusk -is:retweet'

    tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at'], max_results=10)

    tweets_data=[]

    for tweet in tweets.data:
        tweets_data.append(tweet.text)
    
    return tweets_data

def time_API():
    url="https://www.timeapi.io/api/Time/current/zone?timeZone=America/Chicago"
    date_time=requests.get(url).json()
    date=date_time['dateTime'].split("T")[0]
    time=date_time['time']

    date_time=[date,str(time)]
    return date_time


def weather_API():
    """
    {'coord': {'lon': -96.33, 'lat': 30.62}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}], 
    'base': 'stations', 'main': {'temp': 280.43, 'feels_like': 276.22, 'temp_min': 279.85, 'temp_max': 281.29, 'pressure': 1021, 'humidity': 89}, 
    'visibility': 10000, 'wind': {'speed': 8.23, 'deg': 330, 'gust': 11.32}, 'clouds': {'all': 100}, 'dt': 1668490847, 
    'sys': {'type': 2, 'id': 2004581, 'country': 'US', 'sunrise': 1668430250, 'sunset': 1668468535}, 'timezone': -21600, 'id': 4682464, 
    'name': 'College Station', 'cod': 200}
    """

    url="https://api.openweathermap.org/data/2.5/weather?lat=30.62&lon=-96.33&appid="+WEATHER_API_KEY
    weather=requests.get(url).json()
    results=[weather['weather'][0]['main'],str(weather['main']['humidity']),str(int(weather['main']['temp'])-273)+"\xb0"+"C", 'http://openweathermap.org/img/w/'+weather['weather'][0]['icon']+'.png']

    return results



"""

Accessing User Information

"""
from .models import UserAccount

def all_users():
     users=UserAccount.objects.all()
     print(users)
     print(users[0].first_name)
     print(users[0].last_name)
     print(users[0].head_shot)
     return users
