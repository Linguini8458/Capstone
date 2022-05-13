# Main File for capstone project
# By Patrick O'Hara
# Version 1.0.2

#imports
from tkinter import *
import tkinter.font as tkFont

#Starting Variable for Tkinter Window
root = Tk()
#Setting Variables for Fonts
font = tkFont.Font(family="Helvetica",size=16,weight="bold")
root.geometry("500x500")
root.config(bg="purple1")

#Def Statements for Main Window
def quit():
    root.quit()
def iodm():
    from defs import iod
    iod()

#Button Creation and Placement
iodopen = Button(root, text="Open Image Of the Day", bg="purple3", fg="white", font=font, command=iodm)
iodopen.place(x=120,y=210)

exitbtn = Button(root, text="Quit", bg="red",fg="white", font=font, command=quit)
exitbtn.place(x=430,y=450)

#Mainloop to run window
root.mainloop()
