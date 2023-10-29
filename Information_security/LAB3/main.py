import random
from tkinter import *
import string
import math


def pass_gen():
    pass_text = ''
    if var_lat_big.get() != 0:
        pass_text += string.ascii_uppercase
    if var_lat_small.get() != 0:
        pass_text += string.ascii_lowercase
    if var_rus_big.get() != 0:
        pass_text += 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    if var_rus_small.get() != 0:
        pass_text += 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    if var_symb.get() != 0:
        pass_text += string.punctuation
    if var_numb.get() != 0:
        pass_text += string.digits
    password = ''.join(random.choices(pass_text, k=int(lbl_l.cget("text"))))
    lbl_pwd.configure(text=password)


def change_a():
    vars = [var_lat_big.get(), var_lat_small.get(),
            var_rus_big.get(), var_rus_small.get(), var_symb.get(), var_numb.get()]
    lbl_a.configure(text=sum(vars))
    var_s = float(ent_v.get()) * float(ent_t.get()) * 7 / float(ent_p.get())
    lbl_s.configure(text=var_s)
    if sum(vars) != 0:
        lbl_l.configure(text=math.ceil(math.log(var_s, sum(vars))))


window = Tk()
window.title("LAB3 VAR16")
window.geometry('800x350')
var_lat_big = IntVar()
var_lat_small = IntVar()
var_rus_big = IntVar()
var_rus_small = IntVar()
var_symb = IntVar()
var_numb = IntVar()

lbl_p = Label(window, text="P(вероятность)")
lbl_p.grid(column=0, row=0)
lbl_v = Label(window, text="V(скорость перебора), n/день")
lbl_v.grid(column=0, row=1)
lbl_t = Label(window, text="T(срок действия пароля), нед")
lbl_t.grid(column=0, row=2)
lbl_s_text = Label(window, text="S*(нижняя граница паролей)")
lbl_s_text.grid(column=0, row=3)
lbl_a_text = Label(window, text="A(мощность алфавита)")
lbl_a_text.grid(column=0, row=4)
lbl_l_text = Label(window, text="L(Длина пароля)")
lbl_l_text.grid(column=0, row=5)
lbl_pwd_text = Label(window, text="Пароль : ", font=("Arial", 25))
lbl_pwd_text.grid(column=0, row=6)
lbl_pwd = Label(window, text="", font=("Arial", 20))
lbl_pwd.grid(column=1, row=6)
lbl_s = Label(window, text="")
lbl_s.grid(column=1, row=3)
lbl_a = Label(window, text="")
lbl_a.grid(column=1, row=4)
lbl_l = Label(window, text="")
lbl_l.grid(column=1, row=5)

ent_p = Entry(window, width=35)
ent_p.grid(column=1, row=0)
ent_p.insert(0, "0.0000001")
ent_v = Entry(window, width=35)
ent_v.grid(column=1, row=1)
ent_v.insert(0, "10")
ent_t = Entry(window, width=35)
ent_t.grid(column=1, row=2)
ent_t.insert(0, "1")

c1 = Checkbutton(text="Латинские большие",
                 variable=var_lat_big,
                 onvalue=len(string.ascii_uppercase), offvalue=0, command=change_a)
c1.grid(column=2, row=0)
c2 = Checkbutton(text="Латинские маленькие",
                 variable=var_lat_small,
                 onvalue=len(string.ascii_lowercase), offvalue=0, command=change_a)
c2.grid(column=2, row=1)
c3 = Checkbutton(text="Русские большие",
                 variable=var_rus_big,
                 onvalue=len('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'), offvalue=0, command=change_a)
c3.grid(column=2, row=2)
c4 = Checkbutton(text="Русские маленькие",
                 variable=var_rus_small,
                 onvalue=len('абвгдеёжзийклмнопрстуфхцчшщъыьэюя'), offvalue=0, command=change_a)
c4.grid(column=2, row=3)
c5 = Checkbutton(text="Символы",
                 variable=var_symb,
                 onvalue=len(string.punctuation), offvalue=0, command=change_a)
c5.grid(column=2, row=4)
c6 = Checkbutton(text="Цифры",
                 variable=var_numb,
                 onvalue=len(string.digits), offvalue=0, command=change_a)
c6.grid(column=2, row=5)

btn = Button(window, text="Сгенерировать пароль", command=pass_gen)
btn.grid(column=6, row=6)

window.mainloop()
