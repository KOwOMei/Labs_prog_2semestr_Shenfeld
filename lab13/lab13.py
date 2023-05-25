from tkinter import messagebox
from tkinter import *
import requests

def btn_getdata():
    anek = anek_search.get()
    try:
        anek = int(anek)
        if anek not in range (1,4): raise ValueError
        if anek == 3: anek = 11
        url = f"http://rzhunemogu.ru/RandJSON.aspx?CType={anek}"
        res = requests.get(url)
        prikol = res.json(strict=False)
        info["text"] = f"{prikol['content']}"
    except ValueError:
        messagebox.showinfo(title = "Bro...", message = "You should use ints, neither you won't get any jokes...")
    except requests.exceptions.JSONDecodeError:
        btn_getdata()
    

base = Tk()
base['bg'] = "#8A2BE2"
base.title("AnekDoter")
base.geometry("800x600")
base.resizable(width=False, height=False)

# frame_top - отвечает за ввод данных по поиску анекдота.
frame_top = Frame(base, bg = '#40E0D0', bd=5)
frame_top.place(relx=0.10, rely=0.05, relwidth=0.8, relheight=0.3)

title = Label(frame_top, text='Print the type of aneks: ', bg = '#40E0D0', font = 'Minecraftia 27')
title.pack()

title_desc = Label(frame_top, text='1 - Joke; 2 - Story; 3 - Joke 18+', bg = '#40E0D0', font = 'Minecraftia 15')
title_desc.pack()

anek_search = Entry(frame_top, bg = 'white', font = 'Minecraftia 10')
anek_search.pack()

btn = Button(frame_top, text='Press me, pls', bg='pink', font = 'Minecraftia 10', command = btn_getdata)
btn.pack()


frame_bot = Frame(base, bg = '#FFFDD0', bd=5)
frame_bot.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.55)

info = Label(frame_bot, text='There will be jokes, i swear...', bg = '#FFFDD0', font = 'Times 10')
info.pack()

messagebox.showinfo(title = "Hello, my dear friend!", message = "Before using this app, install minecraft.ttf, \nor this app will be broke as old car.")
base.mainloop()