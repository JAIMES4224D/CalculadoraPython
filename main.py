import tkinter
from tkinter import *
import math

var = tkinter.Tk()
var.title("Calculadora compleja")
e = Entry(var, width=50, borderwidth=10)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Variables globales
functionnum = 0
mathematics = ""


# Backend - Funciones
def thebutton(numone):
    thecurrent = e.get()
    e.delete(0, END)
    e.insert(0, str(thecurrent) + str(numone))


def botonlimpiar():
    e.delete(0, END)


def botonagregar():
    try:
        num1 = e.get()
        global functionnum
        global mathematics
        mathematics = "adicion"
        functionnum = float(num1)
        e.delete(0, END)
    except ValueError:
        e.delete(0, END)
        e.insert(0, "Error")


def botonsustraccion():
    try:
        num1 = e.get()
        global functionnum
        global mathematics
        mathematics = "sustraccion"
        functionnum = float(num1)
        e.delete(0, END)
    except ValueError:
        e.delete(0, END)
        e.insert(0, "Error")


def botonmultiplicacion():
    try:
        num1 = e.get()
        global functionnum
        global mathematics
        mathematics = "multiplicacion"
        functionnum = float(num1)
        e.delete(0, END)
    except ValueError:
        e.delete(0, END)
        e.insert(0, "Error")


def botondivision():
    try:
        num1 = e.get()
        global functionnum
        global mathematics
        mathematics = "division"
        functionnum = float(num1)
        e.delete(0, END)
    except ValueError:
        e.delete(0, END)
        e.insert(0, "Error")


def botonelevado():
    try:
        num1 = e.get()
        global functionnum
        global mathematics
        mathematics = "elevado"
        functionnum = float(num1)
        e.delete(0, END)
    except ValueError:
        e.delete(0, END)
        e.insert(0, "Error")


def botonraizcuadrada():
    try:
        num1 = e.get()
        global functionnum
        global mathematics
        mathematics = "raizcuadrada"
        functionnum = float(num1)
        e.delete(0, END)
        e.insert(0, math.sqrt(functionnum))
    except ValueError:
        e.delete(0, END)
        e.insert(0, "Error")


def botonporcentaje():
    try:
        num1 = e.get()
        global functionnum
        global mathematics
        mathematics = "porcentaje"
        functionnum = float(num1)
        e.delete(0, END)
        e.insert(0, functionnum / 100)
    except ValueError:
        e.delete(0, END)
        e.insert(0, "Error")


def botonsen():
    try:
        num1 = e.get()
        global functionnum
        global mathematics
        mathematics = "sen"
        functionnum = float(num1)
        e.delete(0, END)
        rad = functionnum * (math.pi / 180)
        e.insert(0, math.sin(rad))
    except ValueError:
        e.delete(0, END)
        e.insert(0, "Error")


def botoncos():
    try:
        num1 = e.get()
        global functionnum
        global mathematics
        mathematics = "cos"
        functionnum = float(num1)
        e.delete(0, END)
        rad = functionnum * (math.pi / 180)
        e.insert(0, math.cos(rad))
    except ValueError:
        e.delete(0, END)
        e.insert(0, "Error")


def botontan():
    try:
        num1 = e.get()
        global functionnum
        global mathematics
        mathematics = "tan"
        functionnum = float(num1)
        e.delete(0, END)
        rad = functionnum * (math.pi / 180)
        e.insert(0, math.tan(rad))
    except ValueError:
        e.delete(0, END)
        e.insert(0, "Error")


def botonigual():
    try:
        num2 = e.get()
        e.delete(0, END)
        if num2 == "":
            return

        num2 = float(num2)

        if mathematics == "adicion":
            e.insert(0, functionnum + num2)
        elif mathematics == "sustraccion":
            e.insert(0, functionnum - num2)
        elif mathematics == "multiplicacion":
            e.insert(0, functionnum * num2)
        elif mathematics == "division":
            e.insert(0, functionnum / num2)
        elif mathematics == "elevado":
            e.insert(0, functionnum ** num2)
        elif mathematics == "ave":
            e.insert(0, (functionnum + num2) / 2)
    except ValueError:
        e.insert(0, "Error")
    except ZeroDivisionError:
        e.insert(0, "Error: Div/0")
    except Exception as ex:
        e.insert(0, f"Error: {str(ex)}")


# Frontend - Creación de botones
boton1 = Button(var, text="1", padx=50, pady=25, command=lambda: thebutton(1))
boton2 = Button(var, text="2", padx=50, pady=25, command=lambda: thebutton(2))
boton3 = Button(var, text="3", padx=50, pady=25, command=lambda: thebutton(3))
boton4 = Button(var, text="4", padx=50, pady=25, command=lambda: thebutton(4))
boton5 = Button(var, text="5", padx=50, pady=25, command=lambda: thebutton(5))
boton6 = Button(var, text="6", padx=50, pady=25, command=lambda: thebutton(6))
boton7 = Button(var, text="7", padx=50, pady=25, command=lambda: thebutton(7))
boton8 = Button(var, text="8", padx=50, pady=25, command=lambda: thebutton(8))
boton9 = Button(var, text="9", padx=50, pady=25, command=lambda: thebutton(9))
boton0 = Button(var, text="0", padx=50, pady=25, command=lambda: thebutton(0))
botonpi = Button(var, text="π", padx=50, pady=25, command=lambda: thebutton(math.pi))
botonpunto = Button(var, text=".", padx=52, pady=25, command=lambda: thebutton("."))

botonagregar = Button(var, text="+", padx=50, pady=25, command=botonagregar)
botonsustraccion = Button(var, text="-", padx=50, pady=25, command=botonsustraccion)
botonmultiplicacion = Button(var, text="×", padx=50, pady=25, command=botonmultiplicacion)
botondivision = Button(var, text="÷", padx=50, pady=25, command=botondivision)
botonelevado = Button(var, text="^", padx=50, pady=25, command=botonelevado)
botonraizcuadrada = Button(var, text="√", padx=50, pady=25, command=botonraizcuadrada)
botonporcentaje = Button(var, text="%", padx=50, pady=25, command=botonporcentaje)
botonsen = Button(var, text="sin", padx=50, pady=25, command=botonsen)
botoncos = Button(var, text="cos", padx=50, pady=25, command=botoncos)
botontan = Button(var, text="tan", padx=50, pady=25, command=botontan)
botonigual = Button(var, text="=", padx=50, pady=25, command=botonigual)
botonlimpiar = Button(var, text="C", padx=50, pady=25, command=botonlimpiar)

# Posicionamiento de botones
boton7.grid(row=1, column=0)
boton8.grid(row=1, column=1)
boton9.grid(row=1, column=2)
botondivision.grid(row=1, column=3)

boton4.grid(row=2, column=0)
boton5.grid(row=2, column=1)
boton6.grid(row=2, column=2)
botonmultiplicacion.grid(row=2, column=3)

boton1.grid(row=3, column=0)
boton2.grid(row=3, column=1)
boton3.grid(row=3, column=2)
botonsustraccion.grid(row=3, column=3)

boton0.grid(row=4, column=0)
botonpunto.grid(row=4, column=1)
botonpi.grid(row=4, column=2)
botonagregar.grid(row=4, column=3)

botonlimpiar.grid(row=5, column=0)
botonigual.grid(row=5, column=1)
botonelevado.grid(row=5, column=2)
botonraizcuadrada.grid(row=5, column=3)

botonsen.grid(row=6, column=0)
botoncos.grid(row=6, column=1)
botontan.grid(row=6, column=2)
botonporcentaje.grid(row=6, column=3)

var.mainloop()