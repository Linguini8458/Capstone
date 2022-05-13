# Test Files(Nothing to see here)
# 
#  import json
# import requests
# import json
# from urllib.request import urlretrieve
# from pprint import PrettyPrinter
# import datetime
# pp = PrettyPrinter()

# apiKey = 'YiGuGJVpT9n3uBMjOBdzYpPTIkkeBqvTD806nAKO'
# day = datetime.datetime.now()

# def fetchAPOD():
#   global url1
#   URL_APOD = "https://api.nasa.gov/planetary/apod"
#   date = '2022-05-05'
#   params = {
#       'api_key':apiKey,
#       'date':date,
#       'hd':'True'
#   }
#   response = requests.get(URL_APOD,params=params).json()
#   pp.pprint(response)
#   url1 = response["url"]
#   print(url1)

# fetchAPOD()

# day = day.strftime("%Y" + "-%m" + "-%d")
# print(day)




# from tkinter import *
# import os
 
 
# root = Tk()
# if os.path.exists('config\python_apod_uuid_and_cookie.json'):
#     os.remove('config\python_apod_uuid_and_cookie.json')

# from instabot import Bot
# bot = Bot()
 

# def log():
#     if os.path.exists('image.png.REMOVE_ME'):
#         os.remove('image.png.REMOVE_ME')
#     bot.login(username = "python_apod", password = "$Cout2013")
# def upload():
#     from ioda import desc, title, date
#     instadesc = f''' 
# {date}
# {title} - 
# {desc}'''
#     bot.upload_photo("image.png", caption =instadesc)
# log()
# upload()
