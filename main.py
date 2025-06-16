import tkinter as tk
from tkinter import font as tkfont
import math

# Configuración de la ventana principal
var = tk.Tk()
var.title("Calculadora Científica Avanzada")
var.resizable(False, False)
var.configure(bg='#2c3e50')

# Estilo de fuente
font_buttons = tkfont.Font(family='Helvetica', size=12, weight='bold')
font_display = tkfont.Font(family='Courier', size=16, weight='bold')

# Pantalla de resultados
e = tk.Entry(var, width=18, borderwidth=0, font=font_display,
             bg='#ecf0f1', fg='#2c3e50', justify='right', insertbackground='#2c3e50')
e.grid(row=0, column=0, columnspan=4, padx=10, pady=(20, 10), ipady=15)

# Variables globales
functionnum = 0
mathematics = ""

# Paleta de colores
color_nums = '#34495e'
color_ops = '#3498db'
color_func = '#9b59b6'
color_equals = '#2ecc71'
color_clear = '#e74c3c'


# Backend - Funciones
def thebutton(numone):
    thecurrent = e.get()
    e.delete(0, tk.END)
    e.insert(0, str(thecurrent) + str(numone))


def botonlimpiar():
    e.delete(0, tk.END)


def create_operation_func(op):
    def func():
        try:
            num1 = e.get()
            global functionnum, mathematics
            mathematics = op
            functionnum = float(num1)
            e.delete(0, tk.END)
        except ValueError:
            e.delete(0, tk.END)
            e.insert(0, "Error")

    return func


def botonigual():
    try:
        num2 = e.get()
        e.delete(0, tk.END)
        if num2 == "":
            return

        num2 = float(num2)

        if mathematics == "adicion":
            result = functionnum + num2
        elif mathematics == "sustraccion":
            result = functionnum - num2
        elif mathematics == "multiplicacion":
            result = functionnum * num2
        elif mathematics == "division":
            result = functionnum / num2
        elif mathematics == "elevado":
            result = functionnum ** num2
        elif mathematics == "ave":
            result = (functionnum + num2) / 2

        e.insert(0, str(round(result, 10)).rstrip('0').rstrip('.') if '.' in str(result) else result)
    except ValueError:
        e.insert(0, "Error")
    except ZeroDivisionError:
        e.insert(0, "Error: Div/0")
    except Exception as ex:
        e.insert(0, f"Error: {str(ex)}")


def create_func_button(text, command, row, col, color=color_func, colspan=1):
    btn = tk.Button(var, text=text, padx=20, pady=15, font=font_buttons,
                    bg=color, fg='white', activebackground='#bdc3c7',
                    activeforeground='#2c3e50', relief='flat',
                    borderwidth=0, highlightthickness=0,
                    command=command)
    btn.grid(row=row, column=col, columnspan=colspan, padx=3, pady=3, sticky="nsew")
    return btn


# Creación de botones numéricos
for i in range(1, 10):
    row = (9 - i) // 3 + 2
    col = (i - 1) % 3
    create_func_button(str(i), lambda num=i: thebutton(num), row, col, color_nums)

create_func_button("0", lambda: thebutton(0), 5, 1, color_nums)
create_func_button(".", lambda: thebutton("."), 5, 2, color_nums)
create_func_button("π", lambda: thebutton(math.pi), 5, 0, color_func)

# Botones de operaciones
create_func_button("+", create_operation_func("adicion"), 2, 3, color_ops)
create_func_button("-", create_operation_func("sustraccion"), 3, 3, color_ops)
create_func_button("×", create_operation_func("multiplicacion"), 4, 3, color_ops)
create_func_button("÷", create_operation_func("division"), 5, 3, color_ops)

# Botones especiales
create_func_button("C", botonlimpiar, 1, 0, color_clear)
create_func_button("√", lambda: [e.insert(0, math.sqrt(float(e.get()))) if e.get() else None], 1, 1, color_func)
create_func_button("^", create_operation_func("elevado"), 1, 2, color_func)
create_func_button("=", botonigual, 6, 3, color_equals)

# Botones científicos
create_func_button("sin", lambda: e.insert(0, math.sin(math.radians(float(e.get()))) if e.get() else None), 6, 0)
create_func_button("cos", lambda: e.insert(0, math.cos(math.radians(float(e.get()))) if e.get() else None), 6, 1)
create_func_button("tan", lambda: e.insert(0, math.tan(math.radians(float(e.get()))) if e.get() else None), 6, 2)

# Configuración de grid para mejor escalado
for i in range(7):
    var.grid_rowconfigure(i, weight=1)
for i in range(4):
    var.grid_columnconfigure(i, weight=1)


# Efecto hover para botones
def on_enter(e):
    e.widget['bg'] = '#95a5a6'


def on_leave(e):
    if e.widget['text'] in '0123456789':
        e.widget['bg'] = color_nums
    elif e.widget['text'] in '+-×÷':
        e.widget['bg'] = color_ops
    elif e.widget['text'] == '=':
        e.widget['bg'] = color_equals
    elif e.widget['text'] == 'C':
        e.widget['bg'] = color_clear
    else:
        e.widget['bg'] = color_func


for child in var.winfo_children():
    if isinstance(child, tk.Button):
        child.bind("<Enter>", on_enter)
        child.bind("<Leave>", on_leave)

var.mainloop()