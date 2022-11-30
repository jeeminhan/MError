from urllib import response
import dotenv
import os
import requests
import tweepy
from pathlib import Path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import datetime
import os.path

BASE_DIR = Path(__file__).resolve().parent.parent
dotenv_file = os.path.join(BASE_DIR, ".env")
if os.path.isfile(dotenv_file):
        dotenv.load_dotenv(dotenv_file)
NEWS_API_KEY = os.environ['NEWS_API_KEY']
BEARER_TOKEN = os.environ['BEARER_TOKEN']
WEATHER_API_KEY = os.environ['WEATHER_API_KEY']

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
    # OPENWEATHER API - get long lat from the user.city

    url="https://api.openweathermap.org/data/2.5/weather?lat=30.62&lon=-96.33&appid="+WEATHER_API_KEY
    weather=requests.get(url).json()
    results=[weather['weather'][0]['main'],str(weather['main']['humidity']),str(int(weather['main']['temp'])-273)+"\xb0"+"C", 'http://openweathermap.org/img/w/'+weather['weather'][0]['icon']+'.png']

    return results


# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

def googleCal_API():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                '../credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    # try:
    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    # print('Getting the upcoming 10 events')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                            maxResults=10, singleEvents=True,
                                            orderBy='startTime').execute()
    events = events_result.get('items', [])
    # page_token = None
    # while True:
    #     events = service.events().list(calendarId='primary', pageToken=page_token).execute()
    #     for event in events['items']:
    #         print(event['summary'])
    #     page_token = events.get('nextPageToken')
    #     if not page_token:
    #         break

    if not events:
        # print('No upcoming events found.')
        return

    # Prints the start and name of the next 10 events
    calList = []
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        end = event['end'].get('dateTime', event['end'].get('date'))
        calList.append({'date':start[0:10], 'startTime':start[11:19], 'endTime':end[11:19], 'summary':event['summary']})
        # return (start, end, event['summary'])
    return calList

    # except HttpError as error:
    #     return ('An error occurred: %s' % error)