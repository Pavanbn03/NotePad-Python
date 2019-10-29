import pytesseract
import pyttsx3 as tt
from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image
from threading import Thread
import time



pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def select():
    root.filename=filedialog.askopenfilename(initialdir="c:/users/Desktop",title="select image",filetypes=(("png files","*.png"),("all files","*.*")))
    im=Image.open(root.filename)
    str=pytesseract.image_to_string(im,lang="eng")
    #voice(str)
    #speak(str)
    t1=Thread(target=voice,args=(str,))
    t2=Thread(target=speak,args=(str,))
    t1.start()
    t2.start()





root=Tk()
root.title("OCR")
root.geometry("300x300")
Label(root,text="OCR READER",font="Verdana 10 bold",bg="black",fg="white").pack()


root.configure(background="black")
photo=PhotoImage(file=r"icon.png")
b=tk.Button(root,command=select,text="select file",bg="black",fg="white",image=photo,compound=LEFT,highlightbackground="black",highlightthickness=0,borderwidth=0,font="Verdana 10 bold").place(x=100,y=150)


def voice(str):
   # root.withdraw()
    tw = tk.Toplevel()
    tw.geometry("1024x720")
    tw.title("text")
    tw.configure(background="black")
    Label(tw, text=str,font="Verdana 10 bold",bg="black",fg="white").pack()
   # tw.protocol("WM_DELETE_WINDOW",cb)
    tw.mainloop()


def cb():
    root.update()



def speak(str):
    print(str)
    eng=tt.init()
    eng.say(str)
   # time.sleep(5)
    eng.runAndWait()


root.mainloop()
