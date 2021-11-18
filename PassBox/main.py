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
    
def __encrypteFile__(data, encrypteKey, path) :
    
    fKey = Fernet(bytes(encrypteKey, "utf-8"))
    
    readFile = open(data, "rb").read()
    cryptedFile = fKey.encrypt(readFile)
    
    with open(path, "wb") as file :
        file.write(cryptedFile)

def __decryptFile__(data, decrypteKey, path) :
    
    fKey = Fernet(bytes(decrypteKey, "utf-8"))
    
    readFile = open(data, "rb").read()
    decryptedFile = fKey.decrypt(readFile)
    
    with open(path, "wb") as file :
        file.write(decryptedFile)


        
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

print("Programme finished")

# the password file is in .pbl (.Pass Box List)
#b'CZ51unnhvsGfVWvtP3Xg00Y-Attv-D-OsE7MjfKnegY='
