import random
from tkinter import *
import string


def pass_gen(identification):
    pas = ''.join(random.choices(string.ascii_uppercase, k=2)) \
          + str(len(identification) % 10) + ''.join(random.choice(string.digits) + random.choice(string.punctuation)
                                                    + random.choice(string.ascii_lowercase))
    return pas


def clicked():
    res = pass_gen(txt.get())
    psw.configure(text=res)
    lbl3.configure(text=len(txt.get()))


window = Tk()
window.title("LAB1 VAR1")
window.geometry('400x250')
lbl = Label(window, text="ID")
lbl.grid(column=0, row=0)
lbl2 = Label(window, text="Q")
lbl2.grid(column=0, row=1)
lbl3 = Label(window, text="")
lbl3.grid(column=1, row=1)
lbl1 = Label(window, text="Password:")
lbl1.grid(column=0, row=2)
psw = Label(window, text="")
psw.grid(column=1, row=2)
txt = Entry(window, width=30)
txt.grid(column=1, row=0)
btn = Button(window, text="Сгенерировать пароль", command=clicked)
btn.grid(column=3, row=3)
window.mainloop()
