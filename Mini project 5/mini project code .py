import pytesseract
import os
import pyttsx3
from tkinter import filedialog
from tkinter import *

def image_to_text():
    root = Tk()
    root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    text = pytesseract.image_to_string(root.filename)
    print("Image to Text: ", text)

def text_to_voice():
    text = input("Enter the text: ")
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def image_to_text_to_voice():
    root = Tk()
    root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    text = pytesseract.image_to_string(root.filename)
    print("Image to Text: ", text)
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

while True:
    print("Select one of the following options:")
    print("1. Image to Text")
    print("2. Text to Voice")
    print("3. Image to Text and Text to Voice")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        image_to_text()
    elif choice == 2:
        text_to_voice()
    elif choice == 3:
        image_to_text_to_voice()
    else:
        print("Invalid option. Please try again.")

    response = input("Do you want to continue (y/n)? ")
    if response.lower() == "n":
        break
