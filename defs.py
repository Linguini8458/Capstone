#Def file for Calling 
#By Patrick O'Hara
#Version 1.0.3

#imports
from tkinter import *
import urllib
from PIL import ImageTk, Image
import os
from login import usern, passw
import tkinter.font as tkFont


#Deleting File That Breaks Code
if os.path.exists('config\python_apod_uuid_and_cookie.json'):
    os.remove('config\python_apod_uuid_and_cookie.json')
#Import for Instagram Posting
from instabot import Bot

#Variable setting
bot = Bot()
descon = True

#Def Statement for Window Creation
def iod():
    from day import fetchAPOD, desc,title,url1
    #Global Variables
    global descon
    global iodgui
    global font  
    #Font setting
    font = tkFont.Font(family="Helvetica",size=16,weight="bold")
    #Window Creation/Config
    iodgui = Toplevel()
    iodgui.config(bg="midnight blue")
    iodgui.title("Nasa Image of the day")
    print("Image of the Day!")
    fetchAPOD()
    width= iodgui.winfo_screenwidth() #Gets Screen width
    height= iodgui.winfo_screenheight() #Gets Screen Height
    iodgui.geometry("%dx%d" % (width, height)) #Size of Window
    #Def for Image Description
    def iodtxt():
        global descon
        if descon == True:
            #Label and Button Creation
            txt = Label(iodgui, text=desc,  bg="midnight blue", fg="white",wraplength=775)
            txt.pack()
            logbtn = Button(iodgui, text="Login to Instagram", bg="navy", fg="white", font=font,command=instalog)
            logbtn.pack(anchor=E)
            iodgui.update() #Update Window 
            descon = False
        else:
            pass

    #getting the image as a url fomr ioda.py
    urllib.request.urlretrieve(url1, "image.png")
    #Image Opening, Resizing, and Converting to TkImage
    img = Image.open("image.png")
    img = img.resize((500,500))
    img = ImageTk.PhotoImage(img)
    #Button and Label creation
    can = Button(iodgui, image=img, font=font,bg="midnight blue",command=iodtxt)
    titletxt = Label(iodgui,text=title, font=font,bg="midnight blue", fg="white")
    titletxt.pack()
    can.pack()
    iodgui.mainloop() #Runs Window


#Added un update 1.0.3

#Def Statement for Logging Into Instagram
def instalog():
    #Removes File from Past Run
    if os.path.exists('image.png.REMOVE_ME'):
        os.remove('image.png.REMOVE_ME')
    bot.login(username = usern, password = passw) #Login To Insta
    #Button Placement
    instaloadbtn = Button(iodgui, text='Upload to instagram', bg="forest green", fg="white",font=font,command=instaload )
    instaloadbtn.pack(anchor=E)

#Def Statement for Uploading to Instagram
def instaload():
    from day import date, title, desc
    #Description for Post
    instadesc = f''' 
{date}
{title} 
{desc}'''
    #Upload for Post
    bot.upload_photo("image.png", caption=instadesc)
