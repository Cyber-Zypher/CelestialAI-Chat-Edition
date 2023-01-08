from tkinter import *
import keyboard
import datetime
import requests
import random
from bs4 import BeautifulSoup
import bs4
import time
import pyjokes
root = Tk()
root.configure(background="black")

hour = int(datetime.datetime.now().hour)

def ti():
    time.sleep(1)

def sendWithKey(event):
    send = "You ➾ " + e.get()
    txt.insert(END, "\n"+send)
    if(e.get() == 'hi'):
        txt.insert(END,"\n"+"Celestial ❱❱ Hello there, what can I do for you?")
    elif (e.get() == 'hi bot'):
        txt.insert(END,"\n"+"Celestial ❱❱ Yeah I am there!")
    elif (e.get() == 'who are you'):
        txt.insert(END,"\n"+f"Celestial ❱❱ Hi there, I am Celestial AI (Chat Edition) [beta] I am the official chat version of the voice assistant Celestial AI.")
    elif (e.get() == 'what can you do'):
        txt.insert(END,"\n"+f"Celestial ❱❱ I can do all sorts of things a normal AI can do! Try it yourself")
    elif (e.get() == 'who created you'):
        txt.insert(END,"\n"+f"Celestial ❱❱ I was created by Sidharth Everett P.L Yes you heard me right, he created me.")
    elif (e.get() == 'who is your father'):
        txt.insert(END,"\n"+f"Celestial ❱❱ It is Sidharth Everett P.L")
    elif (e.get() == 'do you know Frissco'):
        txt.insert(END,"\n"+f"Celestial ❱❱ Yes ofcourse! it is the company powering me from the backend.")
    elif (e.get() == 'what is Frissco'):
        txt.insert(END,"\n"+f"Celestial ❱❱ Frissco Groups is an incorporated company made by four teenagers in india. Frissco Groups comes under two divisions. Frissco Creative Labs and Frissco Media Productions. Frissco Creative labs does all the IT Works and Frissco Media Productions does all the Media works.")
    elif (e.get() == 'do you know frissco'):
        txt.insert(END,"\n"+f"Celestial ❱❱ Yes ofcourse! it is the company powering me from the backend.")
    elif (e.get() == 'what is frissco'):
        txt.insert(END,"\n"+f"Celestial ❱❱ Frissco Groups is an incorporated company made by four teenagers in india. Frissco Groups comes under two divisions. Frissco Creative Labs and Frissco Media Productions. Frissco Creative labs does all the IT Works and Frissco Media Productions does all the Media works.")
    elif (e.get() == 'tell me a joke'):
        txt.insert(END,"\n"+f"Celestial ❱❱ {pyjokes.get_joke()}")
    elif (e.get() == 'toss a coin'):
        txt.insert(END,"\n"+f"Celestial ❱❱ {random.choice(['Heads', 'Tails'])}")
    elif (e.get() == 'roll a dice'):
        txt.insert(END,"\n"+f"Celestial ❱❱ {random.choice(['one', 'two', 'three', 'four', 'five', 'six'])}")
    elif (e.get() == 'exit'):
        exit()
    elif (e.get() == 'clear chat'):
        txt.delete("1.0", "end")
    else:
        try:
            googlesearch = e.get()
            url = f"https://www.google.com/search?q={googlesearch}"
            request_results = requests.get(url)
            soup = bs4.BeautifulSoup(request_results.text,"html.parser")
            result = soup.find("div", class_="BNeawe").text
            print(result)
            txt.insert(END,"\n"+f"Celestial ❱❱ "+result)
        except Exception as a:
            print(a)
            txt.insert(END,"\n"+f"Celestial ❱❱ Oops an error occured ")
    
    e.delete(0,END)

def send():
    send = "You ➾ " + e.get()
    txt.insert(END, "\n"+send)
    if(e.get() == 'hi'):
        txt.insert(END,"\n"+"Celestial ❱❱ Hello there, what can I do for you?")
    elif (e.get() == 'hi bot'):
        txt.insert(END,"\n"+"Celestial ❱❱ Yeah I am there!")
    elif (e.get() == 'who are you'):
        txt.insert(END,"\n"+f"Celestial ❱❱ Hi there, I am Celestial AI (Chat Edition) [beta] I am the official chat version of the voice assistant Celestial AI.")
    elif (e.get() == 'what can you do'):
        txt.insert(END,"\n"+f"Celestial ❱❱ I can do all sorts of things a normal AI can do! Try it yourself")
    elif (e.get() == 'who created you'):
        txt.insert(END,"\n"+f"Celestial ❱❱ I was created by Sidharth Everett P.L Yes you heard me right, he created me.")
    elif (e.get() == 'who is your father'):
        txt.insert(END,"\n"+f"Celestial ❱❱ It is Sidharth Everett P.L")
    elif (e.get() == 'do you know Frissco'):
        txt.insert(END,"\n"+f"Celestial ❱❱ Yes ofcourse! it is the company powering me from the backend.")
    elif (e.get() == 'what is Frissco'):
        txt.insert(END,"\n"+f"Celestial ❱❱ Frissco Groups is an incorporated company made by four teenagers in india. Frissco Groups comes under two divisions. Frissco Creative Labs and Frissco Media Productions. Frissco Creative labs does all the IT Works and Frissco Media Productions does all the Media works.")
    elif (e.get() == 'do you know frissco'):
        txt.insert(END,"\n"+f"Celestial ❱❱ Yes ofcourse! it is the company powering me from the backend.")
    elif (e.get() == 'what is frissco'):
        txt.insert(END,"\n"+f"Celestial ❱❱ Frissco Groups is an incorporated company made by four teenagers in india. Frissco Groups comes under two divisions. Frissco Creative Labs and Frissco Media Productions. Frissco Creative labs does all the IT Works and Frissco Media Productions does all the Media works.")
    elif (e.get() == 'tell me a joke'):
        txt.insert(END,"\n"+f"Celestial ❱❱ {pyjokes.get_joke()}")
    elif (e.get() == 'toss a coin'):
        txt.insert(END,"\n"+f"Celestial ❱❱ {random.choice(['Heads', 'Tails'])}")
    elif (e.get() == 'roll a dice'):
        txt.insert(END,"\n"+f"Celestial ❱❱ {random.choice(['one', 'two', 'three', 'four', 'five', 'six'])}")
    elif (e.get() == 'exit'):
        exit()
    elif (e.get() == 'clear chat'):
        txt.delete("1.0", "end")
    else:
        try:
            googlesearch = e.get()
            url = f"https://www.google.com/search?q={googlesearch}"
            request_results = requests.get(url)
            soup = bs4.BeautifulSoup(request_results.text,"html.parser")
            result = soup.find("div", class_="BNeawe").text
            print(result)
            txt.insert(END,"\n"+f"Celestial ❱❱ "+result)
        except Exception as a:
            print(a)
            txt.insert(END,"\n"+f"Celestial ❱❱ Oops an error occured ")
    
    e.delete(0,END)


txt = Text(root, bg='black', fg='white')
txt.grid(row=0, column=0, columnspan=2)
e = Entry(root,width=75)
sendBtn = Button(root,text="SEND",command=send).grid(row=1,column=1)
e.grid(row=1,column=0)
root.bind("<Return>", sendWithKey)
root.title("Celestial AI (Text Chat Bot)")
root.mainloop()