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
        messagebox.showinfo(title = "Я не понял...", message = "Ты либо нужные цифры вводи, либо не получишь шутки")
    except requests.exceptions.JSONDecodeError:
        messagebox.showinfo(title = "Я накезился...", message = "Прикол сломался, запустите заново...")
    

base = Tk()
base['bg'] = "#8A2BE2"
base.title("АнекДотер")
base.geometry("800x600")
base.resizable(width=False, height=False)

# frame_top - отвечает за ввод данных по поиску анекдота.
frame_top = Frame(base, bg = '#40E0D0', bd=5)
frame_top.place(relx=0.10, rely=0.10, relwidth=0.8, relheight=0.25)

title = Label(frame_top, text='Введите тип желаемого прикола: ', bg = '#40E0D0', font = 'Times 30')
title.pack()

title_desc = Label(frame_top, text='1 - Анекдот; 2 - Рассказ; 3 - Анекдот 18+', bg = '#40E0D0', font = 'Times 20')
title_desc.pack()

anek_search = Entry(frame_top, bg = 'white', font=30)
anek_search.pack()

btn = Button(frame_top, text='Тыкай, гений', bg='pink', command = btn_getdata)
btn.pack()


frame_bot = Frame(base, bg = '#FFFDD0', bd=5)
frame_bot.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.5)

info = Label(frame_bot, text='Тут будут анекдоты, поверьте...', bg = '#FFFDD0', font = 'Times 10')
info.pack()


base.mainloop()