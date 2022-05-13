#Image of day
#By Patrick O'Hara
#Verison 1.0.0

import datetime
import requests
from pprint import PrettyPrinter


def fetchAPOD():
    global url1
    global desc
    global title
    global date
    pp = PrettyPrinter()
    apiKey = 'YiGuGJVpT9n3uBMjOBdzYpPTIkkeBqvTD806nAKO'
    day = datetime.datetime.now()
    URL_APOD = "https://api.nasa.gov/planetary/apod"
    date = day.strftime("%Y"+"-%m"+"-%d")
    params = {
        'api_key':apiKey,
        'date':date,
        'hd':'True'
    }
    response = requests.get(URL_APOD,params=params).json()
    pp.pprint(response)
    url1 = response["url"]
    desc = response['explanation']
    title = response['title']

fetchAPOD()
