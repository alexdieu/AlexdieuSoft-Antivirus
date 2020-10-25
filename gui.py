import os.path as pt
import sys
import io
from contextlib import redirect_stdout
import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter.messagebox as mb

critical = False
missing = ''
try:
    from Modules.MaliciousBat import scanbat as sb
except:
    missing = missing + '- MaliciousBat'
    critical = True
try:
    from Modules.pythonScanner import scanpy as ps
except:
    missing = missing + '- PythonScanner'
    critical = True
try:
    from Modules.vbscan import vbscan as vs
except:
    missing = missing + '- Vbscan'
    critical = True

if critical == True:
    msg = str("Missing Modules : (try reinstall software)" + missing)
    mb.showerror(title='Module Error', message=msg)
    print("Missing modules : " + missing)


def getInputBoxValue():
    userInput = file.get()
    return userInput


if len(sys.argv) > 1:
    file = sys.argv[1]
else:
    pass


def scan():
    out = False
    v = io.StringIO()
    file = getInputBoxValue()
    if pt.isfile(file):
        if '.bat' in file:
            out = True
            with redirect_stdout(v):
                sb(file)
        if '.py' in file:
            out = True
            with redirect_stdout(v):
                ps(file)
        if '.vbs' in file:
            out = True
            with redirect_stdout(v):
                vs(file)
        else:
            if out == True:
                output = v.getvalue()
                mb.showinfo(title="result", message=output)
            else:
                mb.showerror(title="Uknown format", message="Uknown format for the file : " + file)
    else:
        mb.showwarning(title='File Import Error', message="The file "+file+" doesn't exist !")


root = Tk()

root.geometry('500x400')
root.configure(background='#F0F8FF')
root.title('AlexSoft®')

Label(root, text='AlexSoft®', bg='#F0F8FF', font=(
    'courier', 12, 'italic')).place(x=15, y=9)

root.iconbitmap('ico.ico')
ico = Canvas(root, height=86, width=53)
picture_file = PhotoImage(file='icoforgui.png')
ico.create_image(48, 0, anchor=NE, image=picture_file)
ico.place(x=117, y=10)

Label(root, text='Files accepted : .bat, .py and .vbs',bg='#F0F8FF', font=('arial', 12, 'bold')).place(x=169, y=95)

Label(root, text='This tool is a BETA version !', bg='#F0F8FF',font=('arial', 6, 'italic')).place(x=176, y=117)

file = Entry(root)
file.place(x=169, y=142)

Button(root, text='SCAN !', bg='#00FFFF', font=('helvetica', 6, 'italic'), command=scan).place(x=182, y=171)


root.mainloop()
