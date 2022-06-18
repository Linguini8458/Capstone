#Image of day
#By Patrick O'Hara
#Verison 1.0.0

#Imports
import datetime
import requests
from pprint import PrettyPrinter

#Def Statment for contacting NASA API
def fetchAPOD():
    #Global Variable Setting
    global url1
    global desc
    global title
    global date
    #Setting Variables
    pp = PrettyPrinter()
    apiKey = 'YiGuGJVpT9n3uBMjOBdzYpPTIkkeBqvTD806nAKO' #API Key
    day = datetime.datetime.now()
    URL_APOD = "https://api.nasa.gov/planetary/apod" #AOI
    date = day.strftime("%Y"+"-%m"+"-%d") #Gets Current Date
    #Pulls API data
    params = {
        'api_key':apiKey,
        'date':date,
        'hd':'True'
    }
    #Response from API Conversion to JSON File
    response = requests.get(URL_APOD,params=params).json()
    pp.pprint(response)
    #Variable to Set Globlly for all PY Files
    url1 = response["url"]
    desc = response['explanation']
    title = response['title']

fetchAPOD()
