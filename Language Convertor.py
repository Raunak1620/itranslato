#bll
def hindi():
    code = var2.get()
    s = t.translate(var1.get(), dest=code)
    btncopy = ttk.Button(root, text="Copy Translated Text", command=copy, cursor='pirate')
    btncopy.place(x=220, y=240)
    var3.set(s.text)

def copy():
    pyperclip.copy(var3.get())
    tkinter.messagebox._show("Congrats", "Copied Successfully")

def exit():
    flag = tkinter.messagebox.askokcancel("Exit", "Do You Really want to Exit!")
    if flag:
        root.destroy()

def help():
    tkinter.messagebox.showinfo("Help",
                                "Step1:Enter Your Text in Entry Box\nStep2:Select Language to Translate\nStep3:Click on Translate "
                                "Button\nStep4:Copy the translated text and use it\nHurray! You did it\nEnjoy.")


def playMusic():
    winsound.PlaySound('kisma.wav', winsound.SND_ASYNC)

def stopMusic():
    winsound.PlaySound(None, winsound.SND_PURGE)


# pl
import pyperclip
from tkinter import *
from tkinter import ttk, font
from googletrans import Translator
import tkinter.messagebox
import winsound

root = Tk()
root.geometry("600x300")
root.title("iTranslato")
menubar = Menu(root)
root.config(bg="gray", menu=menubar)

"""variables_used"""
var1 = StringVar()
var2 = StringVar()
var3 = StringVar()

"""created object t of translator class"""
t = Translator()

"""used some styling and themes to make gui more attractive"""
s = ttk.Style()
myfont = font.Font(family="courier", size=10)
s.theme_use('classic')
s.configure('TButton', foreground="white", background="black")
s.configure('TLabel', foreground="White", background="grey")
rooticon = PhotoImage(file="rooticon.png")
root.iconphoto(FALSE, rooticon)

"""label_for guiding user to enter text"""
lbenter = ttk.Label(root, text="Enter text for conversion", font=myfont)
lbenter.place(x=60, y=20)

"""entry widget where user will enter text"""
ent1 = ttk.Entry(root, text=var1)
ent1.place(x=310, y=20)

lblen = ttk.Label(root, text="Select Preferred Language", font=myfont)
lblen.place(x=60, y=50)

"""used option menu to select languages"""
options = ["Hindi", "English", "French", "Japanese", "Kannada", "Punjabi", "Urdu", "Greek", "Bengali",
           "German", "Hungarian", "Chinese", "Nepali", "Arabic"]
w = ttk.OptionMenu(root, var2, *options)
var2.set(options[0])
w.place(x=310, y=50)

"""menubar for help and exit"""
menubar.add_command(label="Help", command=help)
menubar.add_command(label="Exit", command=exit)

"""translate button"""
btntrans = ttk.Button(root, text="Translate", command=hindi, width=20, cursor='pirate')
btntrans.place(x=220, y=140)

lboutput = ttk.Label(root, textvariable=var3)
lboutput.place(x=260, y=200)

lbres = ttk.Label(root, text="Result", font=myfont)
lbres.place(x=70, y=200)

"""playmusic icon,label and button"""
playpic = PhotoImage(file="playy.png")
stoppic = PhotoImage(file="stop.png")

lbmusic = ttk.Label(root, text="Play Music", font=myfont)
lbmusic.place(x=500, y=20)

"""button when clicked fires an event that execute the function playmusic"""
btnplay = ttk.Button(root, image=playpic, command=playMusic)
btnplay.place(x=490, y=40)

lbmusic = ttk.Label(root, text="Stop Music", font=myfont)
lbmusic.place(x=500, y=140)

"""button when clicked fires an event that execute the function playmusic"""
btnplay = ttk.Button(root, image=stoppic, command=stopMusic)
btnplay.place(x=490, y=160)

mainloop()
# @Developed by || RAUNAK ||
