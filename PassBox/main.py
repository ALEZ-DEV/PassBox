from cryptography.fernet import Fernet
import os
import base64

keepedKey = ""
oneKeyKeeped = False

def __keepKey__(key) :
    
    keepedKey = key
    print("your key is keeped")

    def __getKeepedKey__() :
        return keepedKey
    
def __menu__() :

    isChoosed = True
    turn = 0
    
    while(isChoosed) :
        
        if (turn == 0) :
                print("what do you want to do :")
                print("n : create a new key (not recommanded if is already created)")
                print("c : crypte anything file")
                print("d : decrypte txt file")
                print("np : create a new password list")
                print("op : open password list")  
                turn += 1     
        
        command = input("--")
        if (command == "n") :
            isChoosed = False
            __newKey__()
            __menu__()
            
        elif (command == "c") :
            isChoosed = False
            print("do you want to generate a new key ? | yes : y | no : n")
            newOne = input("--")
            
            if (newOne == "n") :
                print("do you want to use keeped key ? | yes : y | no : n")
                getKey = input("--")           
                if (getKey == "n") :
                    print("Enter your key :")
                    fileKey = input("--")
                else :
                    fileKey = keepedKey
            else :
                fileKey =  __newKey__()
            
            print("Enter the path of your file :")
            path = input("--")
            
            __encrypteFile__(path, fileKey)
            __menu__()
            
        elif (command == "d") :
            isChoosed = False
            
            print("do you want to use keeped key ? | yes : y | no : n")
            getKey = input("--")           
            if (getKey == "n") :
                print("Enter your key :")
                fileKey = input("--")
            else :
                fileKey = keepedKey
            
            print("Enter the path of your file :")
            path = input("--")
            
            __decryptFile__(path, fileKey)
            
        elif (command == "np") :
            isChoosed = False
            
        elif (command == "op") :
            isChoosed = False
            
        else :
            print("this command is not valid")
            isChoosed = True
            
def __newKey__() :
    
    key = Fernet.generate_key()
    print("the new key is : " + str(key))
    
    print("do you want to keep this key ? | yes : y | no : n")
    keeped = input("--")

    if (keeped == "y") :
        __keepKey__(key)
    
    return key
    
def __encrypteFile__(data, encrypteKey) :
    print("where do you want to save your encrypted file ?")
    savePath = input("--")
    
    fKey = Fernet(bytes(encrypteKey, "utf-8"))
    
    readFile = open(data, "rb").read()
    cryptedFile = fKey.encrypt(readFile)
    
    with open(savePath, "wb") as file :
        file.write(cryptedFile)

def __decryptFile__(data, decrypteKey) :
    
    print("where do you want to save your decrypted file ?")
    savePath = input("--")
    
    fKey = Fernet(bytes(decrypteKey, "utf-8"))
    
    readFile = open(data, "rb").read()
    decryptedFile = fKey.decrypt(readFile)
    
    with open(savePath, "wb") as file :
        file.write(decryptedFile)
    
__menu__()
print("Programme finished")

#b'CZ51unnhvsGfVWvtP3Xg00Y-Attv-D-OsE7MjfKnegY='
