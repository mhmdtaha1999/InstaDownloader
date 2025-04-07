from tkinter import *
import instaloader
import urllib
from urllib.request import urlopen
from PIL import Image, ImageTk
import io


def get_image():
    L = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(L.context, f"{username.get()}")
    a = urlopen(profile.get_profile_pic_url())
    data = a.read()
    a.close()
    image = Image.open(io.BytesIO(data))
    pic = ImageTk.PhotoImage(image)
    label.config(image=pic)
    label.image = pic
    label.pack()

window = Tk()
window.title("Instagram Downloader")
window.geometry("600x600")

label = Label(window, text="Enter your instagram username: ")
label.pack()

username = Entry(window , width=50)
username.pack()

button = Button(window , text = "Start Download" )
button.pack()
button.config(command=get_image)

window.mainloop()

