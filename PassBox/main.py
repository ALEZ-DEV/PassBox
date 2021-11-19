from os import name
from tkinter import *
from functools import partial
import tkinter
from tkinter.filedialog import askopenfile, askopenfilename
from cryptography.fernet import Fernet
import os
import base64
import csv

userProfile = os.environ['USERPROFILE']
userDocuments = userProfile + "\\Documents\\"

"""
all command usable :
__newKey__ : generate a new key / return string   
__encrypteFile__ : encrypte any type file / parameter : data (message), encrypteKey (key), path / return None
__decrypteFile__ : decrypte any type file / parameter : data (message), decrypteKey (key), path / return None
__createList__ : create list in .pbl file / parameter : name / return the path of the file in string
__addList__ : add element in a list / parameter : path, key, name, data(the password) / return None
__getList__ : get element of a list and crypted list / parameter : path, decrypteKey (key), / return the all element in table list
__encrypteList__ : encrypte list in .pbl file / path, encrypteKey (key), passwordList(the all list of password) / return None

"""
keepedKey = ""
oneKeyKeeped = False
fileName = ""


def __newKey__():
    key = Fernet.generate_key()
    print(key)

    return key


def __encrypteFile__(filePath, encrypteKey, path):
    fKey = Fernet(bytes(encrypteKey, "utf-8"))

    readFile = open(filePath, "rb").read()
    cryptedFile = fKey.encrypt(readFile)

    with open(path, "wb") as file:
        file.write(bytes(cryptedFile))


def __decryptFile__(data, decrypteKey, path):
    fKey = Fernet(bytes(decrypteKey, "utf-8"))

    readFile = open(data, "rb").read()
    decryptedFile = fKey.decrypt(readFile)

    with open(path, "wb") as file:
        file.write(decryptedFile)


def __replaceBytes__(data):
    data.replace("b", "")
    data.replace("'", "")
    return data


def __createList__(name):
    open(f"%USERPROFILE%\\Documents\\{name}.pbl", "wb")

    return f"%USERPROFILE%\\Documents\\{name}.pbl"


def __addList__(path, key, name, data):
    password = [name, data]
    __encrypteList__(path, key, password)
    __getList__(path, key)


def __getList__(path, decrypteKey):
    fKey = Fernet(bytes(decrypteKey, "utf-8"))
    passList = []

    with open("C:\\Users\\cp-21sgr\\Documents\\text.csv", "rb") as fileData:
        csv_reader = csv.reader(fileData)

    for i in csv_reader:
        password = []
        password.append(fKey.decrypt(i[0]))
        password.append(fKey.decrypt(i[1]))
        passList.append(password)

    return passList


def __encrypteList__(path, encrypteKey, passwordList):
    fkey = Fernet(bytes(encrypteKey, "utf-8"))
    data = []

    with open(path, "rb") as fileData:
        csv_reader = csv.reader(fileData)

        for i in csv_reader:
            defaultPassword = []
            defaultPassword.append(i[0])
            defaultPassword.append(i[1])
            data.append(defaultPassword)

    name = fkey.encrypt(passwordList[0])
    password = fkey.encrypt(passwordList[1])
    dataLine = []
    dataLine.append(name)
    dataLine.append(password)
    data.append(dataLine)

    with open(path, "wb", newline="") as fileData:
        csv_writer = csv.writer(fileData, delimiter=",")

        for i in data:
            csv_writer.writerow(i)


def __crypte__():
    def __getPath__():
        path = askopenfile()
        entry_path.delete(0, END)
        entry_path.insert(0, path.name)

    def __generateKey__():
        key = __newKey__()
        entry_key.delete(0, END)
        entry_key.insert(0, key)

    def __crypte__():
        filePath = entry_path.get()
        key = entry_key.get()
        path = userDocuments + "text.txt"
        __encrypteFile__(filePath, key, path)

    crypte = Tk()

    crypte.geometry("500x300")

    crypte.title("PassBox : Crypte")

    text_path = Label(crypte, text="enter the path", width=10)
    entry_path = Entry(crypte, width=50)
    button_getFilePath = Button(crypte, text="...", width=15, command=__getPath__)

    text_path.grid(column=0, row=1)
    entry_path.grid(column=1, row=1)
    button_getFilePath.grid(column=2, row=1)

    text_key = Label(crypte, text="enter key", width=10)
    entry_key = Entry(crypte, width=50)
    button_generateKey = Button(crypte, text="generate", width=15, command=__generateKey__)

    text_key.grid(column=0, row=2)
    entry_key.grid(column=1, row=2)
    button_generateKey.grid(column=2, row=2)

    button_crypte = Button(crypte, text="crypte", width=10, command=__crypte__)

    button_crypte.grid(column=1, row=3)

    crypte.mainloop()


def __decrypte__():
    def __getPath__():
        path = askopenfile()
        entry_path.delete(0, END)
        entry_path.insert(0, path.name)

    def __decrypte__():
        filePath = entry_path.get()
        key = entry_key.get()
        path = userDocuments + "text.txt"
        __decryptFile__(filePath, key, path)

    decrypte = Tk()

    decrypte.geometry("500x300")

    decrypte.title("PassBox : Decrypte")

    text_path = Label(decrypte, text="enter the path", width=10)
    entry_path = Entry(decrypte, width=50)
    button_getFilePath = Button(decrypte, text="...", width=15, command=__getPath__)

    text_path.grid(column=0, row=1)
    entry_path.grid(column=1, row=1)
    button_getFilePath.grid(column=2, row=1)

    text_key = Label(decrypte, text="enter key", width=10)
    entry_key = Entry(decrypte, width=50)

    text_key.grid(column=0, row=2)
    entry_key.grid(column=1, row=2)

    button_decrypte = Button(decrypte, text="decrypte", width=10, command=__decrypte__)

    button_decrypte.grid(column=1, row=3)

    decrypte.mainloop()


def __passList__(list):

    
    passList = Tk()

    passList.geometry("500x300")

    passList.title("PassBox : PassList")

    def __getPath__():
        path = askopenfile()
        entry_path.delete(0, END)
        entry_path.insert(0, path.name)

    def __get__():
        list = __getList__(entry_path.get(), entry_key.get())
        n = 2
        for i in list :
            n += 1
            name = Label(text=str(i[0]))
            password = Label(text=str(i[1]))

            name.grid(column=0, row=n)
            password.grid(column=1, row=n)

    text_path = Label(passList, text="enter the path", width=10)
    entry_path = Entry(passList, width=50)
    button_getFilePath = Button(passList, text="...", width=15, command=__getPath__)

    text_path.grid(column=0, row=1)
    entry_path.grid(column=1, row=1)
    button_getFilePath.grid(column=2, row=1)
    
    text_key = Label(passList, text="enter key", width=10)
    entry_key = Entry(passList, width=50)

    text_key.grid(column=0, row=2)
    entry_key.grid(column=1, row=2)
    
    button_get = Button(passList, text="get", width=15, command=__get__)

    button_get.grid(column=2, row=2)

    passList.mainloop()

def __test__() :
    __passList__(None)

def __exit__():
    exit()


def __init__():

    menu = Tk()

    menu.geometry("500x300")

    menu.title("PassBox")

    button_crypte = Button(menu, text="crypte file", command=__crypte__, width=70)
    button_decrypte = Button(menu, text="decrypte file", command=__decrypte__, width=70)
    button_passList = Button(menu, text="password list", command=__test__, width=70)
    button_exit = Button(menu, text="Exit", command=menu.destroy, width=70)

    button_crypte.grid(column=0, row=1)
    button_decrypte.grid(column=0, row=2)
    button_passList.grid(column=0, row=3)
    button_exit.grid(column=0, row=4)

    menu.mainloop()


__init__()
# IbwP6SKQJPMAgF0922lh41NL5gnMQymB-HWnidMincM=