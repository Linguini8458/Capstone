#Def file for Calling 
#By Patrick O'Hara
#Version 1.0.3


from tkinter import *
import urllib
from PIL import ImageTk, Image
import os
from login import usern, passw
import tkinter.font as tkFont

descon = True

if os.path.exists('config\python_apod_uuid_and_cookie.json'):
    os.remove('config\python_apod_uuid_and_cookie.json')

from instabot import Bot
bot = Bot()



def iod():
    global descon
    global iodgui
    global font
    from ioda import fetchAPOD,desc,title,url1
    font = tkFont.Font(family="Helvetica",size=16,weight="bold")
    font = tkFont.Font(family="Helvetica",size=16,weight="bold")
    iodgui = Toplevel()
    iodgui.config(bg="midnight blue")
    iodgui.title("Nasa Image of the day")
    print("Image of the Day!")
    fetchAPOD()
    width= iodgui.winfo_screenwidth()
    height= iodgui.winfo_screenheight()
    iodgui.geometry("%dx%d" % (width, height))
    def iodtxt():
        global descon
        if descon == True:
            txt = Label(iodgui, text=desc, wraplength=775)
            txt.pack()
            logbtn = Button(iodgui, text="Login to Instagram", bg="navy", fg="white", font=font,command=instalog)
            logbtn.pack(anchor=E)
            iodgui.update()
            descon = False
        else:
            pass

    urllib.request.urlretrieve(url1, "image.png")
    img = Image.open("image.png")
    img = img.resize((500,500))
    img = ImageTk.PhotoImage(img)
    can = Button(iodgui, image=img, font=font,bg="midnight blue",command=iodtxt)
    titletxt = Label(iodgui,text=title)
    titletxt.pack()
    can.pack()
    iodgui.mainloop()

def instalog():
    if os.path.exists('image.png.REMOVE_ME'):
        os.remove('image.png.REMOVE_ME')
    bot.login(username = usern, password = passw)
    instaloadbtn = Button(iodgui, text='Upload to instagram', bg="forest green", fg="white",font=font,command=instaload )
    instaloadbtn.pack(anchor=E)

def instaload():
    from ioda import desc, title, date
    instadesc = f''' 
{date}
{title} 
{desc}'''
    bot.upload_photo("image.png",font=font, caption =instadesc)
