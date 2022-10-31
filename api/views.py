from urllib import response
from django.shortcuts import render
import dotenv
import os
import requests
from pathlib import Path

# Create your views here.
BASE_DIR = Path(__file__).resolve().parent.parent
dotenv_file = os.path.join(BASE_DIR, ".env")
if os.path.isfile(dotenv_file):
        dotenv.load_dotenv(dotenv_file)
NEWS_API_KEY = os.environ['NEWS_API_KEY']

def index(request):
    # API function
    news_titles=news_API()

    # Data transformation for display
    response={"news":news_titles}

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