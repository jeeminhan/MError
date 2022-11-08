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

# def index(request):
#     # API function
#     news_titles=news_API()

#     # Data transformation for display
#     response={"news":news_titles}

#     return render(request, "index.html", response)

# # HELPER FUNCTIONS TO PERFORM AND PROCESS THE API requests
# def news_API():

#     # Link for making request
#     url="https://newsapi.org/v2/top-headlines?country=us&apiKey="+NEWS_API_KEY

#     news=requests.get(url).json()

#     # Storing the top headings
#     titles=[]

#     for i in range(5):
#         titles+=[news['articles'][i]['title']]
    
#     return titles

def index(request):
    # API function
    tweets=twitter_API()

    # Data transformation for display
    response={"tweets":tweets}

    return render(request, "index.html", response)


def twitter_API():
    # Link for making request
    client = tweepy.Client(bearer_token=BEARER_TOKEN)
    query = 'from:elonmusk -is:retweet'

    tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at'], max_results=10)

    tweets_data=[]

    for tweet in tweets.data:
        tweets_data.append(tweet.text)
    
    return tweets_data