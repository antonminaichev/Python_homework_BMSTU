from recordclass import recordclass
import tkinter as tk


User = recordclass("User", ["username", "password", "surname", "name", "fath_name", "date", "place", "tel"])

class UserForm(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.name = tk.StringVar()
        self.surname = tk.StringVar()
        self.fath_name = tk.StringVar()
        self.date = tk.StringVar()
        self.place = tk.StringVar()
        self.tel = tk.StringVar()

        label = tk.Label(self, text="Создать пользователя ")
        entry_username = tk.Entry(self, textvariable=self.username)
        entry_pass = tk.Entry(self, textvariable=self.password, show="*")
        entry_surname = tk.Entry(self, textvariable=self.surname)
        entry_name = tk.Entry(self, textvariable=self.name)
        entry_fath_name = tk.Entry(self, textvariable=self.fath_name)
        entry_date = tk.Entry(self, textvariable=self.date)
        entry_place = tk.Entry(self, textvariable=self.place)
        entry_tel = tk.Entry(self, textvariable=self.tel)
        btn = tk.Button(self, text="Сохранить", command=self.destroy)

        label.grid(row=0, columnspan=2)
        tk.Label(self, text="Логин:").grid(row=1, column=0)
        tk.Label(self, text="Пароль:").grid(row=2, column=0)
        tk.Label(self, text="Фамилия:").grid(row=3, column=0)
        tk.Label(self, text="Имя:").grid(row=4, column=0)
        tk.Label(self, text="Отчество:").grid(row=5, column=0)
        tk.Label(self, text="Дата рождения:").grid(row=6, column=0)
        tk.Label(self, text="Место рождения:").grid(row=7, column=0)
        tk.Label(self, text="Телефон:").grid(row=8, column=0)
        entry_username.grid(row=1, column=1)
        entry_pass.grid(row=2, column=1)
        entry_surname.grid(row=3, column=1)
        entry_name.grid(row=4, column=1)
        entry_fath_name.grid(row=5, column=1)
        entry_date.grid(row=6, column=1)
        entry_place.grid(row=7, column=1)
        entry_tel.grid(row=8, column=1)
        btn.grid(row=9, columnspan=2)

    def open(self):
        self.grab_set()
        self.wait_window()
        username = self.username.get()
        password = "АБВ" + self.password.get()
        surname = self.surname.get()
        name = self.name.get()
        fath_name = self.fath_name.get()
        date = self.date.get()
        place = self.place.get()
        tel = self.tel.get()
        return User(username, password, surname, name, fath_name, date, place, tel)

class ChangeForm(tk.Toplevel):
    def __init__(self, parent, users):
        super().__init__(parent)
        self.users = users
        self.username = tk.StringVar()
        self.old_password1 = tk.StringVar()
        self.old_password2 = tk.StringVar()
        self.new_password = tk.StringVar()

        label = tk.Label(self, text="Сменить пароль ")
        entry_username = tk.Entry(self, textvariable=self.username)
        entry_pass_old1 = tk.Entry(self, textvariable=self.old_password1, show="*")
        entry_pass_old2 = tk.Entry(self, textvariable=self.old_password2, show="*")
        entry_pass_new = tk.Entry(self, textvariable=self.new_password, show="*")
        btn = tk.Button(self, text="Сохранить", command=self.destroy)

        label.grid(row=0, columnspan=2)
        tk.Label(self, text="Логин:").grid(row=1, column=0)
        tk.Label(self, text="Cтарый пароль:").grid(row=2, column=0)
        tk.Label(self, text="Введите старый пароль ещё раз:").grid(row=3, column=0)
        tk.Label(self, text="Новый пароль:").grid(row=4, column=0)
        entry_username.grid(row=1, column=1)
        entry_pass_old1.grid(row=2, column=1)
        entry_pass_old2.grid(row=3, column=1)
        entry_pass_new.grid(row=4, column=1)
        btn.grid(row=9, columnspan=2)

    def open(self):
        self.grab_set()
        self.wait_window()
        username = self.username.get()
        old_pass1 = self.old_password1.get()
        old_pass2 = self.old_password2.get()
        new_pass = self.new_password.get()
        if old_pass1 != old_pass2:
            print("Ошибка")
            return
        for i in self.users:
            if username == i.username and old_pass1 == i.password[3:]:
                return [new_pass, i.username]
            else:
                print("Ошибка")
                return

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.users = []
        self.username = tk.StringVar()
        self.password = tk.StringVar()

        label = tk.Label(self, text="Введите логин и пароль:")
        entry_username = tk.Entry(self, textvariable=self.username)
        entry_pass = tk.Entry(self, textvariable=self.password, show="*")

        label.grid(row=0, columnspan=2)
        tk.Label(self, text="Логин:").grid(row=1, column=0)
        tk.Label(self, text="Пароль:").grid(row=2, column=0)
        entry_username.grid(row=1, column=1)
        entry_pass.grid(row=2, column=1)
        btn_commit = tk.Button(self, text="Войти", command=self.auth)
        btn_create = tk.Button(self, text="Cоздать пользователя", command=self.open_window_create)
        btn_change = tk.Button(self, text="Сменить пароль", command=self.open_window_change)
        btn_commit.grid(row=3, columnspan=2)
        btn_create.grid(row=4, columnspan=2)
        btn_change.grid(row=5, columnspan=2)

    def auth(self):
        username = self.username.get()
        password = "АБВ" + self.password.get()
        for i in self.users:
            if i.username == username and i.password == password:
                with open('secrets.txt') as f:
                    lines = f.readlines()
                    print(lines)
            else:
                print("У вас нет доступа, создайте пользователя или введите корректный пароль")

    def open_window_change(self):
        window = ChangeForm(self, self.users)
        data = window.open()
        if data is not None:
            for i in self.users:
                if data[1] == i.username:
                    i.password = "АБВ" + data[0]
        print(self.users)

    def open_window_create(self):
        window = UserForm(self)
        user = window.open()
        print(user)
        if not self.users:
            self.users.append(user)
        for i in self.users:
            if user.username == i.username:
                print("Пользователь с таким ID уже создан")
                print(self.users)
                return
        self.users.append(user)

if __name__ == "__main__":
    app = App()
    app.mainloop()