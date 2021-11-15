from os import name
from tkinter import *
from functools import partial
from tkinter.filedialog import askopenfile, askopenfilename

def click_n():
    exit()

def click_c():

    def crypte_exit():
        crypte.destroy()

    crypte = Tk()
    crypte.title("Crypte")
    label_path = Label(crypte, text="Please select the path")
    button_path = Button(crypte, text="Click", command=crypte_path)
    label_exit = Button(crypte, text="Exit" ,command=crypte_exit)
    label_key = Label(crypte, text="Enter a key to crypte your text")
    entry_key = Entry(crypte, textvariable=text)

    label_path.grid(column=0, row=0)
    button_path.grid(column=0, row=1)
    label_exit.grid(column=0, row=2)
    label_key.grid(column=0, row=3)
    entry_key.grid(column=0, row=4)

    crypte.mainloop()


def click_d():
    exit()

def click_np():
    exit()

def click_op():
    exit()

def click_exit():
    exit()

main = Tk()

main.title("PassBox")

text = StringVar(main)
label = Label(main, text = "")
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
label.grid(column=0, row=7)

main.mainloop()
