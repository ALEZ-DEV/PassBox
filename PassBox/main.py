from cryptography.fernet import Fernet
import os
import base64
import csv

keepedKey = ""
oneKeyKeeped = False
fileName = ""

#def __menu__() :
#
#    isChoosed = True
#    turn = 0
#    
#    while(isChoosed) :
#        
#        if (turn == 0) :
#                print("what do you want to do :")
#                print("n : create a new key (not recommanded if is already created)")
#                print("c : crypte anything file")
#                print("d : decrypte txt file")
#                print("np : create a new password list")
#                print("op : open password list")  
#                turn += 1     
#        
#        command = input("--")
#        if (command == "n") :
#            isChoosed = False
#            __newKey__()
#            __menu__()
#            
#        elif (command == "c") :
#            isChoosed = False
#            print("do you want to generate a new key ? | yes : y | no : n")
#            newOne = input("--")
#            
#            if (newOne == "n") :
#                print("do you want to use keeped key ? | yes : y | no : n")
#                getKey = input("--")           
#                if (getKey == "n") :
#                    print("Enter your key :")
#                    fileKey = input("--")
#                else :
#                    fileKey = keepedKey
#            else :
#                fileKey =  __newKey__()
#            
#            print("Enter the path of your file :")
#            path = input("--")
#            
#            __encrypteFile__(path, fileKey)
#            __menu__()
#            
#        elif (command == "d") :
#            isChoosed = False
#            
#            print("do you want to use keeped key ? | yes : y | no : n")
#            getKey = input("--")           
#            if (getKey == "n") :
#                print("Enter your key :")
#                fileKey = input("--")
#            else :
#                fileKey = keepedKey
#            
#            print("Enter the path of your file :")
#            path = input("--")
#            
#            __decryptFile__(path, fileKey)
#            
#        elif (command == "np") :
#            isChoosed = False
#            
#            print("do you want to use keeped key ? | yes : y | no : n")
#            getKey = input("--")           
#            if (getKey == "n") :
#                print("Enter your key :")
#                fileKey = input("--")
#            else :
#                fileKey = keepedKey
#            
#            print("Enter the name of your file :")
#            name = input("--")
#            
#            __createPassList__(fileKey, name)
#            __menu__()
#            
#        elif (command == "op") :
#            isChoosed = False
#            
#        else :
#            print("this command is not valid")
#            isChoosed = True
#            
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
