import tkinter as tk
from tkinter import ttk
from tkinter import *
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
import random
import pyperclip

root = tk.Tk()
frm = ttk.Frame(root, padding=10)

frm.grid()
root.title("Password Generator")


def passwordLength():
    pass


def includeSymbols():
    return punctuation * includeSymbols_var.get()


def includeNumbers():
    return digits * includeNumbers_var.get()


def includeLowerCase():
    return ascii_lowercase * includeLowerCase_var.get()


def includeUpperCase():
    return ascii_uppercase * includeUpperCase_var.get()


def on_generate_password_clicked():
    pwd_len = pwd_len_var.get()
    available_chars = ""
    available_chars += includeNumbers()
    available_chars += includeLowerCase()
    available_chars += includeUpperCase()
    available_chars += includeSymbols()

    pwd = generate_password(pwd_len, available_chars)
    pwd_var.set(pwd)


def generate_password(pwd_len, available_chars):
    pwd = "".join(random.choices(available_chars, k=pwd_len))
    return pwd


def copyPassword():
    pyperclip.copy(str(pwd_var.get()))


available_chars = ""
pwd_var = tk.StringVar()
pwd_len_var = tk.IntVar()
pwd_len_var.set(8)


ttk.Label(frm, text="password length").grid(column=0, row=0, sticky="w")
ttk.Label(frm, text="include symbols").grid(column=0, row=1, sticky="w")
ttk.Label(frm, text="include numbers").grid(column=0, row=2, sticky="w")
ttk.Label(frm, text="include lower case").grid(column=0, row=3, sticky="w")
ttk.Label(frm, text="include upper case").grid(column=0, row=4, sticky="w")
ttk.Label(frm, text="Your Password is: ").grid(column=0, row=6, sticky="w")
ttk.Button(frm, text="Copy Password", command=copyPassword).grid(
    column=2, row=6, sticky="e"
)
ttk.Button(frm, text="Generate Password", command=on_generate_password_clicked).grid(
    column=2, row=7, sticky="e"
)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=2, row=8, sticky="e")

passwordLength_entry = Entry(frm, textvariable=pwd_len_var)
passwordLength_entry.grid(column=1, row=0)

includeSymbols_var = tk.IntVar()
checkbox = ttk.Checkbutton(
    frm,
    text="",
    variable=includeSymbols_var,
).grid(column=1, row=1)

includeNumbers_var = tk.IntVar()
checkbox = ttk.Checkbutton(
    frm,
    text="",
    variable=includeNumbers_var,
).grid(column=1, row=2)

includeLowerCase_var = tk.IntVar()
checkbox = ttk.Checkbutton(
    frm,
    text="",
    variable=includeLowerCase_var,
).grid(column=1, row=3)

includeUpperCase_var = tk.IntVar()
checkbox = ttk.Checkbutton(
    frm,
    text="",
    variable=includeUpperCase_var,
).grid(column=1, row=4)


result = Entry(frm, textvariable=pwd_var)
result.grid(column=1, row=6)


root.mainloop()
