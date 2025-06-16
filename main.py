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

def botonigual():
    num2 = e.get()
    e.delete(0,END)
    if mathematics == "adicion":
        e.insert(0, functionnum + int(num2))
    if mathematics == "sustraccion":
        e.insert(0, functionnum - int(num2))
    if mathematics == "multiplicacion":
        e.insert(0, functionnum * int(num2))
    if mathematics == "divisiom":
        e.insert(0, functionnum / int(num2))
    if mathematics == "elevado":
        e.insert(0, functionnum ** int(num2))
    if mathematics == "raizcuadrada":
        e.insert(0, math.sqrt(functionnum))
    if mathematics == "porcentaje":
        e.insert(0, functionnum/100)
    if mathematics == "sen":
        rad = functionnum * (math.pi/180)
        e.insert(0, math.sin(rad))
    if mathematics == "cos":
        rad = functionnum * (math.pi/180)
        e.insert(0, math.cos(rad))
    if mathematics == "tan":
        rad = functionnum * (math.pi/180)
        e.insert(0, math.tan(rad))
    if mathematics == "csc":
        rad = functionnum * (math.pi/180)
        e.insert(0, 1/math.sin(rad))
    if mathematics == "sec":
        rad = functionnum * (math.pi/180)
        e.insert(0, 1/math.cos(rad))
    if mathematics == "cot":
        rad = functionnum * (math.pi/180)
        e.insert(0, 1/math.tan(rad))
    if mathematics == "ave":
        e.insert((functionnum + int(num2))/2)
    if mathematics == "cuadrado":
        e.insert(0, functionnum**2)
    if mathematics == "cubo":
        e.insert(0, functionnum**3)
    if mathematics == "lognatural":
        e.insert(0, math.log(functionnum))
    if mathematics == "e":
        e.insert(0, math.exp(functionnum))
    if mathematics == "log":
        e.insert(0, math.log10(functionnum))
    if mathematics == "negativo":
        e.insert(0, functionnum * -1)
    if mathematics == "valorabsoluto":
        e.insert(0, abs(functionnum))
    if mathematics == "factorial":
        e.insert(0, math.factorial(functionnum))
    if mathematics == "2elevadoa":
        e.insert(0, 2**functionnum)
    if mathematics == "inverso":
        e.insert(0, functionnum ** -1)
    if mathematics == "seninverso":
        rad = functionnum * (math.pi/180)
        e.insert(0, math.asin(rad))
    if mathematics == "cosinverso":
        rad = functionnum * (math.pi / 180)
        e.insert(0, math.acos(rad))
    if mathematics == "taninverso":
        rad = functionnum * (math.pi / 180)
        e.insert(0, math.atan(rad))