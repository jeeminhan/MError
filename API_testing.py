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

# print(news_API())


def time_API():
    url="https://www.timeapi.io/api/Time/current/zone?timeZone=America/Chicago"
    date_time=requests.get(url).json()
    date=date_time['dateTime'].split("T")[0]
    time=date_time['time']

    date_time=[date,str(time)]
    return date_time


print(time_API())


def weather_API():
    """
    {'coord': {'lon': -96.33, 'lat': 30.62}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}], 
    'base': 'stations', 'main': {'temp': 280.43, 'feels_like': 276.22, 'temp_min': 279.85, 'temp_max': 281.29, 'pressure': 1021, 'humidity': 89}, 
    'visibility': 10000, 'wind': {'speed': 8.23, 'deg': 330, 'gust': 11.32}, 'clouds': {'all': 100}, 'dt': 1668490847, 
    'sys': {'type': 2, 'id': 2004581, 'country': 'US', 'sunrise': 1668430250, 'sunset': 1668468535}, 'timezone': -21600, 'id': 4682464, 
    'name': 'College Station', 'cod': 200}
    """

    ur1="https://api.openweathermap.org/data/2.5/weather?lat=30.62&lon=-96.33&appid=XXXXXXXXXXXXXXXXXXXXXXXXX"
    weather=requests.get(ur1).json()
    temp=[weather['weather'][0]['main'],str(weather['main']['humidity']),str(int(weather['main']['temp'])-273)+"\xb0"+"C", 'http://openweathermap.org/img/w/'+weather['weather'][0]['icon']+'.png']
    print(temp)


weather_API()
