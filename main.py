import tkinter
from tkinter import *
import math

var = tkinter.Tk()
var.title("Calculadora compleja")
e = Entry(var, width=50, borderwidth=10)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


#Backend
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

def botonsustraccion():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "sustraccion"
    functionnum = int(num1)
    e.delete(0, END)

def botonmultiplicacion():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "multiplicacion"
    functionnum = int(num1)
    e.delete(0, END)
def botondivision():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "divisiom"
    functionnum = int(num1)
    e.delete(0, END)
def botonelevado():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "elevado"
    functionnum = int(num1)
    e.delete(0, END)

def botonraizcuadrada():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "raizcuadrada"
    functionnum = int(num1)
    e.delete(0, END)
def botonporcentaje():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "porcentaje"
    functionnum = int(num1)
    e.delete(0, END)
def botonsen():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "sen"
    functionnum = int(num1)
    e.delete(0, END)
def botoncos():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "cos"
    functionnum = int(num1)
    e.delete(0, END)
def botontan():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "tan"
    functionnum = int(num1)
    e.delete(0, END)
def botoncsc():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "csc"
    functionnum = int(num1)
    e.delete(0, END)
def botonsec():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "sec"
    functionnum = int(num1)
    e.delete(0, END)
def botoncot():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "cot"
    functionnum = int(num1)
    e.delete(0, END)
def botonave():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "ave"
    functionnum = int(num1)
    e.delete(0, END)
def botoncuadrado():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "cuadrado"
    functionnum = int(num1)
    e.delete(0, END)
def botoncubo():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "cubo"
    functionnum = int(num1)
    e.delete(0, END)
def botonlognatural():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "lognatural"
    functionnum = int(num1)
    e.delete(0, END)
def botone():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "e"
    functionnum = int(num1)
    e.delete(0, END)
def botonlog():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "log"
    functionnum = int(num1)
    e.delete(0, END)
def botonnegativo():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "negativo"
    functionnum = int(num1)
    e.delete(0, END)
def botonvalorabsoluto():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "valorabsoluto"
    functionnum = int(num1)
    e.delete(0, END)
def botonfactorial():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "factorial"
    functionnum = int(num1)
    e.delete(0, END)
def boton2elevadoa():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "2elevadoa"
    functionnum = int(num1)
    e.delete(0, END)


def botoninverso():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "inverso"
    functionnum = int(num1)
    e.delete(0, END)
def botonseninverso():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "seninverso"
    functionnum = int(num1)
    e.delete(0, END)
def botoncosinverso():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "cosinverso"
    functionnum = int(num1)
    e.delete(0, END)
def botontaninverso():
    num1 = e.get()
    global functionnum
    global mathematics
    mathematics = "taninverso"
    functionnum = int(num1)
    e.delete(0, END)

#Frontend
#Cracion de boton
boton1 = Button(var, text = "1", padx = 50, pady = 25, command = lambda: thebutton(1))
boton2 = Button(var, text = "2", padx = 50, pady = 25, command = lambda: thebutton(2))
boton3 = Button(var, text = "3", padx = 50, pady = 25, command = lambda: thebutton(3))
boton4 = Button(var, text = "4", padx = 50, pady = 25, command = lambda: thebutton(4))
boton5 = Button(var, text = "5", padx = 50, pady = 25, command = lambda: thebutton(5))
boton6 = Button(var, text = "6", padx = 50, pady = 25, command = lambda: thebutton(6))
boton7 = Button(var, text = "7", padx = 50, pady = 25, command = lambda: thebutton(7))
boton8 = Button(var, text = "8", padx = 50, pady = 25, command = lambda: thebutton(8))
boton9 = Button(var, text = "9", padx = 50, pady = 25, command = lambda: thebutton(9))
boton0 = Button(var, text = "0", padx = 50, pady = 25, command = lambda: thebutton(0))
botonpi = Button(var, text = "Pi", padx = 50, pady = 25, command = lambda: thebutton(math.pi))
botonagregar = Button(var, text = "+", padx = 50, pady = 25, command = botonagregar)
botonigual = Button(var, text = "=", padx = 50, pady = 25, command = botonigual)
botonlimpiar = Button(var, text = "Clear", padx = 50, pady = 25, command =  botonlimpiar)
botonmultiplicacion = Button(var, text = "*", padx = 50, pady = 25, command = botonmultiplicacion)
botondivision = Button(var, text = "/", padx = 50, pady = 25, command = botondivision)
botonelevado = Button(var, text = "^", padx = 50, pady = 25, command = botonelevado)
botonraizcuadrada = Button(var, text = "√", padx = 50, pady = 25, command= botonraizcuadrada)
botonporcentaje = Button(var, text = "%", padx = 50, pady = 25, command= botonporcentaje)
botonsen = Button(var, text = "sen", padx = 50, pady = 25, command= botonsen)
botoncos = Button(var, text = "sen", padx = 50, pady = 25, command= botoncos)
botontan = Button(var, text = "sen", padx = 50, pady = 25, command= botontan)
botonave = Button(var, text = "ave", padx = 50, pady = 25, command= botonave)
botoncsc = Button(var, text = "csc", padx = 50, pady = 25, command= botoncsc)
botonsec = Button(var, text = "sec", padx = 50, pady = 25, command= botonsec)
botoncot = Button(var, text = "cot", padx = 50, pady = 25, command= botoncot)
botoncuadrado = Button(var, text = "^2", padx = 50, pady = 25, command= botoncuadrado)
botoncubo = Button(var, text = "^3", padx = 50, pady = 25, command= botoncubo)
botonlognatural = Button(var, text = "ln", padx = 50, pady = 25, command= botonlognatural)
botone = Button(var, text = "e", padx = 50, pady = 25, command= botone)
botonlog = Button(var, text = "log()", padx = 50, pady = 25, command= botonlog)
botonnegativo = Button(var, text = "~", padx = 50, pady = 25, command= botonnegativo)
botonvalorabsoluto = Button(var, text = "abs()", padx = 50, pady = 25, command= botonvalorabsoluto)
botonfactorial = Button(var, text = "!", padx = 50, pady = 25, command= botonfactorial)
boton2elevadoa = Button(var, text = "2^", padx = 50, pady = 25, command= boton2elevadoa)
botoninverso = Button(var, text = "-->", padx = 50, pady = 25, command= botoninverso)
botonseninverso = Button(var, text = "asen", padx = 50, pady = 25, command= botonseninverso)
botoncosinverso = Button(var, text = "cosen", padx = 50, pady = 25, command= botoncosinverso)
botontaninverso = Button(var, text = "atan", padx = 50, pady = 25, command= botontaninverso)


#boton local
boton1.grid(row=1,column=0)
boton2.grid(row=1,column=1)
boton3.grid(row=1,column=2)
botonpi.grid(row=1,column=3)
boton4.grid(row=2,column=0)
boton5.grid(row=2,column=1)
boton6.grid(row=2,column=2)
botonagregar.grid(row=2,column=3)
boton7.grid(row=3,column=0)
boton8.grid(row=3,column=1)
boton9.grid(row=3,column=2)
botonigual.grid(row=3,column=3)
boton0.grid(row=4,column=0)
botonigual.grid(row=4,column=1)
botonlimpiar.grid(row=4,column=2)
botonmultiplicacion.grid(row=4,column=3)
botondivision.grid(row=5,column=0)
botonelevado.grid(row=5,column=1)
botonraizcuadrada.grid(row=5,column=2)
botonporcentaje.grid(row=5,column=3)
botonsen.grid(row=6,column=0)
botoncos.grid(row=6,column=1)
botontan.grid(row=6,column=2)
botonave.grid(row=6,column=3)
botoncsc.grid(row=7,column=0)
botonsec.grid(row=7,column=1)
botoncot.grid(row=7,column=2)
botoncuadrado.grid(row=7,column=3)
botoncubo.grid(row=8,column=0)
botonlognatural.grid(row=8,column=1)
botone.grid(row=8,column=2)
botonlog.grid(row=8,column=3)
botonvalorabsoluto.grid(row=9,column=0)
botonfactorial.grid(row=9,column=1)
boton2elevadoa.grid(row=9,column=2)
botoninverso.grid(row=9,column=3)
botonseninverso.grid(row=10,column=0)
botoncosinverso.grid(row=10,column=1)
botontaninverso.grid(row=10,column=2)
botonnegativo.grid(row=10,column=3)

var.mainloop()