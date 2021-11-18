from os import name
from tkinter import *
from functools import partial
from tkinter.filedialog import askopenfile, askopenfilename
from cryptography.fernet import Fernet
import os
import base64
import csv

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
    
def __newKey__() :
    
    key = Fernet.generate_key()
    print(key)
    
    return key
    
def __encrypteFile__(filePath, encrypteKey, path) :
    
    fKey = Fernet(bytes(encrypteKey, "utf-8"))
    
    readFile = open(filePath, "rb").read()
    cryptedFile = fKey.encrypt(readFile)
    
    with open(path, "wb") as file :
        file.write(bytes(cryptedFile))

def __decryptFile__(data, decrypteKey, path) :
    
    fKey = Fernet(bytes(decrypteKey, "utf-8"))
    
    readFile = open(data, "rb").read()
    decryptedFile = fKey.decrypt(readFile)
    
    with open(path, "wb") as file :
        file.write(decryptedFile)

def __replaceBytes__(data) :
    data.replace("b","")
    data.replace("'","")
    return data
        
def __createList__(name) :

    open(f"%USERPROFILE%\\Documents\\PassBox\\{name}.pbl", "wb")
    
    return f"%USERPROFILE%\\Documents\\PassBox\\{name}.pbl"
    
def __addList__(path, key , name, data) :
    
    password = [name, data]
    __encrypteList__(path, key, password)
    __getList__(path, key)
    
def __getList__(path, decrypteKey):
    
    fKey = Fernet(bytes(decrypteKey, "utf-8"))
    passList = []
    
    with open(path, "rb") as fileData : 
        csv_reader = csv.reader(fileData)
        
    for i in csv_reader :
        password = []
        password.append(i[0])
        password.append(i[1])
        passList.append(password)
        
    return passList
        
def __encrypteList__(path, encrypteKey, passwordList) :
    
    fkey = Fernet(bytes(encrypteKey, "utf-8"))
    data = []
    
    
    with open(path, "rb") as fileData :
        csv_reader = csv.reader(fileData)
        
        for i in csv_reader :
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
    
    
    with open(path, "wb", newline="") as fileData :
        csv_writer = csv.writer(fileData, delimiter=",")
        
        for i in data :
            csv_writer.writerow(i)

def click_n():
    exit()

def click_c():

    
    def crypte_path():
        filenamepath = askopenfilename()
        return filenamepath

    def crypte_exit():
        crypte.destroy()

    key = ""
    def crypte_enter():
        text = entry_key.get()
        return text

    def set_text() :
        random_key = __newKey__()
        entry_key.delete(0, END)
        entry_key.insert(0, random_key)

    def __crypted_path__():
        crypted_path = entry_crypted_path.get()
        return crypted_path




    crypte = Tk()
    crypte.geometry("500x300")
    crypte.title("Crypte")
    label_path = Label(crypte, text="Please select the path")
    button_path = Button(crypte, text="Click", command=crypte_path)
    button_exit = Button(crypte, text="Exit" ,command=crypte_exit)
    label_key = Label(crypte, text="Enter a key to crypte your text")
    entry_key = Entry(crypte, width=60)
    button_enter = Button(crypte, text="Enter", command=crypte_enter)
    button_random_key = Button(crypte, text="Random", command=set_text)
    label_crypted_path = Label(crypte, text="Please enter the path of your crypted text")
    entry_crypted_path = Entry(crypte, width=60)
    entry_get_file = Entry(crypte, width=60)
    button_crypte = Button(crypte, text="crypte")
    
    label_path.grid(column=0, row=0)
    button_path.grid(column=0, row=1)
    label_key.grid(column=0, row=2)
    entry_key.grid(column=0, row=3)
    button_enter.grid(column=1, row=3)
    button_random_key.grid(column=2, row=3)
    button_crypte.grid(column=0, row=4)
    entry_get_file.grid(column=0, row=5)
    button_exit.grid(column=0, row=6)
    
    button_crypte["command"] = command=print("%USERPROFILE%\\documents\\PassBox.txt")
    #__encrypteFile__(entry_get_file.get(), entry_key.get(), "%USERPROFILE%\\documents\\PassBox.txt"
    
    crypte.mainloop()

def click_d():
    exit()

def click_np():
    exit()

def click_op():
    exit()

def click_exit():
    exit()
def menu() :
    main = Tk()

    main.geometry("500x300")

    main.title("PassBox")

    what = Label(main, text = "what do you want to do :")
    button_n = Button(main, text="n : create a new key (not recommanded if is already created)", command=click_n)
    button_c = Button(main, text="c : crypte anything file", command=click_c)
    button_d = Button(main, text="d : decrypte txt file", command=click_d)
    button_np = Button(main, text="np : create a new password list", command=click_np)
    button_op = Button(main, text="op : open password list", command=click_op)
    button_exit = Button(main, text="Exit", command=click_exit)

    what.grid(column=0, row=0)
    button_n.grid(column=0, row=1)
    button_c.grid(column=0, row=2)
    button_d.grid(column=0, row=3)
    button_np.grid(column=0, row=4)
    button_op.grid(column=0, row=5)
    button_exit.grid(column=0, row=6)

    main.mainloop()

menu()
print("Programme finished")