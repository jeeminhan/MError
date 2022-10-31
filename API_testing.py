import dotenv
import os
import requests


def news_API():
    # Link for making request
    url="https://newsapi.org/v2/top-headlines?q=Fed&country=us&apiKey=$$$$$$$$$$"

    news=requests.get(url).json()
    print(news)

    # Storing the top headings

    titles=[]

    for i in range(4):
        titles+=[news['articles'][i]['title']]
    print("HERE")
    return titles

print(news_API())