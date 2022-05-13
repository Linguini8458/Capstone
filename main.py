# Main File for capstone project
# By Patrick O'Hara
# Version 1.0.2
from tkinter import *
import tkinter.font as tkFont
root = Tk()


font = tkFont.Font(family="Helvetica",size=16,weight="bold")
root.geometry("500x500")

def quit():
    root.quit()
def space():
    spacegui = Tk()
    spacegui.title("Earth Image")
    print("Space")
    spacegui.mainloop()

def iodm():
    from defs import iod
    iod()

iodopen = Button(root, text="Open Image Of the Day", font=font, command=iodm)
iodopen.grid(column=2,row=1)

exitbtn = Button(root, text="Quit", bg="red",fg="white", font=font, command=quit)
exitbtn.grid(column=5,row=5)
root.mainloop()
