import tkinter
from tkinter import *
import math

var = tkinter.Tk()
var.title("Calculadora compleja")
e = Entry(var, width=50, borderwidth=10)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

var.mainloop()


# cracion de funciones por boton
def thebutton(numone):
    thecurrent = e.get()
    e.delete(0, END)
    e.insert(0, str(thecurrent) + str(numone))


def botonlimpiar():
    e.delete(0, END)


def botonagregar():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "adicion"
    functionnum = int(num1)
    e.delete(0, END)

