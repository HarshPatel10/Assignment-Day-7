from pytube import YouTube
import pytube

from tkinter import *

root = Tk()

def youtube():
    a = var.get()
    ytvideo = YouTube('a').streams.filter(progressive=True, file_extension=('mp4').order_by('resolution').desc().first())
    ytvideo.download(r"F:\desktop\assignment")
    print("Entry box",a)

root.geometry("300*400")
root.title("Youtube video download")

l1 =Label(text = "Youtube video",fg='red')
l1.place(x=30,y=20)

var = stringVar()
e1 = Entry (root,textvariable =var, width=60)
e1.place(x=40,y=80)

b1 = Button (root,text="Download",command=youtube,bg="green",width=20,fg="white")
b1.place(x=80,y=120)


root.mainloop()
