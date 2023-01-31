from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo

clicks = 0
ForLabel1 = 0
addWord = []
# ------Функция вывода сообщения в label
def show_message():
    # label["text"] = entry.get()
    global clicks
    if clicks < 1:
        label1 = Label(text="Вы нажали клавишу")
        label1.place(x=250, y=340)
    clicks += 1
# -----------------------------------
# ------Функция получения длины пароля
def length():
    length_var = spinbox.get()
    # print(length_var)

# -----------------------------------
# ------Функция ввода слова----------
def add_word():
    # Переделать очистку label
    addWord = entry.get()
    # label_add_word = ttk.Label(text=addWord)
    # label_add_word.place(x=250, y=166)

    # clicks += 1
    # if clicks > 1 and addWord[1]<addWord[0]:
    #     addWord[0]=addWord[1]
    # if click > 0:
    #     label_add_word["text"] = "new text"
# -----------------------------------

# ------Функция выбора языка---------
def selected(event):
    selection = combobox.get()
    label["text"] = f"Вы выбрали: {selection}"
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
btn = ttk.Button(text="Сгенерировать пароль", command=show_message)
# btn.place(x=200, y=300, width = 150, height = 40)
btn.pack(side=RIGHT, anchor=S, pady=77, padx=34)
#------------------------------------

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
spinbox_var = StringVar(value=22)
# ------Поле выбора длины пароля-----
spinbox = ttk.Spinbox(from_=1, to=20, textvariable=spinbox_var, command=length)
spinbox.place(x=20, y=240)
# -----------------------------------
enabledS = IntVar()
enabledN = IntVar()
enabledCl = IntVar()
# ------Настройка параметров генерации
enabled_simbols = ttk.Checkbutton(text="Использовать %*_! символы", variable=enabledS) # , command=checkbutton_changed
enabled_simbols.place(x=20, y=110)

enabled_numbers = ttk.Checkbutton(text="Использовать цифры", variable=enabledN) # , command=checkbutton_changed
enabled_numbers.place(x=20, y=140)

enabled_Cletters = ttk.Checkbutton(text="Использовать заглавные буквы", variable=enabledCl) # , command=checkbutton_changed
enabled_Cletters.place(x=20, y=170)
# -----------------------------------

# ------Надписи----------------------
labelout = ttk.Label(text="Здесь будут генерироваться пароли")
labelout.place(x=20, y=340)

label_language = ttk.Label(text="Выбор языка")
label_language.place(x=175, y=210)

label_function = ttk.Label(text="Длина пароля")
label_function.place(x=175, y=240)

label = ttk.Label(text="Проверка функций")
label.place(x=20, y=270)
# -----------------------------------

root.mainloop()
