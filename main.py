from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo

clicks = 0
ForLabel1 = 0
addWord = None
length_var = []
# ------Функция вывода сообщения в label
def show_password():
    entry_pass.insert(0, "Ваш пароль")
# -----------------------------------
# ------Функция получения длины пароля
def length():
    global length_var
    length_var = spinbox.get()
# -----------------------------------
# ------Функция ввода слова----------
def add_word():
    # Переделать очистку label
    global addWord
    addWord = entry.get()
# -----------------------------------

#------Функция подключения символов-
def checkbutton_enabledS():
    if enabledS.get() == 1:
        return True
# -----------------------------------
# ------Функция подключения цифр-----
def checkbutton_enabledN():
    if enabledN.get() == 1:
        return True
# -----------------------------------
# ------Функция подключения заглавных букв
def checkbutton_enabledCl():
    if enabledCl.get() == 1:
        return True
# -----------------------------------
# ------Функция выбора языка---------
def selected(event):
    selection = combobox.get()
    label["text"] = f"Вы выбрали: {selection}"
# -----------------------------------
# ------Функция генерирования букв---
def generate():
    if combobox.get() == "Английский":
        English_letters = ''                    # маленькие буквы
        for i in range(ord('a'), ord('z')+1):
            English_letters += chr(i)
        print(English_letters)

        if checkbutton_enabledCl() == True:
            English_letters2 = ''
            for j in range(ord('A'), ord('Z')+1):   # заглавные буквы
                English_letters2 += chr(j)
            print(English_letters2)
    elif combobox.get() == "Русский":
        Russian_letters = ''
        for k in range(ord('а'), ord('я')+1):   # маленькие буквы
            Russian_letters += chr(k)
        print(Russian_letters)

        if checkbutton_enabledCl() == True:
            Russian_letters2 = ''
            for k in range(ord('А'), ord('Я')+1):   # заглавные буквы
                Russian_letters2 += chr(k)
            print(Russian_letters2)

    if checkbutton_enabledS() == True:
        Simbols = ''
        for s in range(ord('!'), ord('/')+1):   # символы
            Simbols += chr(s)
        print(Simbols)

    if checkbutton_enabledN() == True:
        Numbers = ''
        for n in range(ord('0'), ord('9')+1):   # цифры
            Numbers += chr(n)
        print(Numbers)

    length_pass = spinbox.get()                 # берем длину пароля

    if addWord == None:
        return
    else:
        word = addWord                          # введенное слово
# -----------------------------------
# ------Очистка полей----------------
def clear():
    entry.delete(0, END)
# -----------------------------------

# ------Создание объекта-------------
root = Tk()
root.title("Генератор паролей")
icon = PhotoImage(file="bones.png")
root.iconphoto(True, icon)
root.geometry("400x400")
# -----------------------------------

# ------Кнопка Сгенерировать---------
btn = ttk.Button(text="Сгенерировать пароль", command=generate)
# btn.place(x=200, y=300, width = 150, height = 40)
btn.pack(side=RIGHT, anchor=S, padx=34, pady=77)
#------------------------------------
# ------Кнопка показать пароль-------
btn_show = ttk.Button(text="Показать пароль", command=show_password)
btn_show.pack(side=LEFT, anchor=S, padx=20, pady=50)
# ------Кнопка вставить слово--------
enter_button = ttk.Button(text="Добавить", command=add_word)
enter_button.place(x=230, y=136)
# -----------------------------------

# ------Кнопка Очистить--------------
clear_button = ttk.Button(text="Clear", command=clear)
clear_button.place(x=310, y=136)
# -----------------------------------
# ------Лого в контейнере------------
BounsLogo = PhotoImage(file="roflan.gif")
labelLogo = ttk.Label(image=BounsLogo)
labelLogo.place(x=6, y=6)
# -----------------------------------

# ------Поле ввода-------------------
entry = ttk.Entry()
entry.place(x=230, y=110)
entry.insert(0, "Введите текст")
# ------Поле получения пароля--------
entry_pass = ttk.Entry()
entry_pass.place(x=20, y=300)
# -----------------------------------
# -----------------------------------
languages_var = StringVar(value=[0])
# ------Поле выбора языка------------
languages = ["Русский", "Английский"]
combobox = ttk.Combobox(textvariable=languages_var, values=languages, state="readonly")
combobox.place(x=20, y=210)
combobox.bind("<<ComboboxSelected>>", selected)
#------------------------------------
spinbox_var = StringVar(value=[20])
# ------Поле выбора длины пароля-----
spinbox = ttk.Spinbox(from_=1, to=20, textvariable=spinbox_var, command=length)
spinbox.place(x=20, y=240)
# -----------------------------------
enabledS = IntVar()
enabledN = IntVar()
enabledCl = IntVar()
# ------Настройка параметров генерации
enabled_simbols = ttk.Checkbutton(text="Использовать %*_! символы", variable=enabledS)
enabled_simbols.place(x=20, y=110)

enabled_numbers = ttk.Checkbutton(text="Использовать цифры", variable=enabledN)
enabled_numbers.place(x=20, y=140)

enabled_Cletters = ttk.Checkbutton(text="Использовать заглавные буквы", variable=enabledCl)
enabled_Cletters.place(x=20, y=170)
# -----------------------------------

# ------Надписи----------------------
labelout = ttk.Label(text="Здесь будут генерироваться пароли")
labelout.place(x=20, y=360)

label_language = ttk.Label(text="Выбор языка")
label_language.place(x=175, y=210)

label_function = ttk.Label(text="Длина пароля")
label_function.place(x=175, y=240)

label = ttk.Label(text="Проверка функций")
label.place(x=20, y=270)
# -----------------------------------

root.mainloop()
