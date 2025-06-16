import tkinter as tk
from tkinter import font as tkfont
import math

# Configuración de la ventana principal
var = tk.Tk()
var.title("Calculadora Científica Premium")
var.resizable(False, False)
var.configure(bg='#2c3e50')

# Estilo de fuente
font_buttons = tkfont.Font(family='Helvetica', size=12, weight='bold')
font_display = tkfont.Font(family='Courier', size=16, weight='bold')

# Pantalla de resultados
e = tk.Entry(var, width=25, borderwidth=0, font=font_display,
             bg='#ecf0f1', fg='#2c3e50', justify='right', insertbackground='#2c3e50')
e.grid(row=0, column=0, columnspan=5, padx=10, pady=(20, 10), ipady=15)

# Variables globales
functionnum = 0
mathematics = ""

# Paleta de colores
color_nums = '#34495e'
color_ops = '#3498db'
color_func = '#9b59b6'
color_equals = '#2ecc71'
color_clear = '#e74c3c'
color_trig = '#1abc9c'
color_inv_trig = '#16a085'


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

        if mathematics == "raizcuadrada":
            result = math.sqrt(functionnum)
        elif mathematics == "porcentaje":
            result = functionnum / 100
        elif mathematics == "sen":
            rad = functionnum * (math.pi / 180)
            result = math.sin(rad)
        elif mathematics == "cos":
            rad = functionnum * (math.pi / 180)
            result = math.cos(rad)
        elif mathematics == "tan":
            rad = functionnum * (math.pi / 180)
            result = math.tan(rad)
        elif mathematics == "csc":
            rad = functionnum * (math.pi / 180)
            result = 1 / math.sin(rad)
        elif mathematics == "sec":
            rad = functionnum * (math.pi / 180)
            result = 1 / math.cos(rad)
        elif mathematics == "cot":
            rad = functionnum * (math.pi / 180)
            result = 1 / math.tan(rad)
        elif mathematics == "cuadrado":
            result = functionnum ** 2
        elif mathematics == "cubo":
            result = functionnum ** 3
        elif mathematics == "lognatural":
            result = math.log(functionnum)
        elif mathematics == "e":
            result = math.exp(functionnum)
        elif mathematics == "log":
            result = math.log10(functionnum)
        elif mathematics == "negativo":
            result = functionnum * -1
        elif mathematics == "valorabsoluto":
            result = abs(functionnum)
        elif mathematics == "factorial":
            result = math.factorial(int(functionnum))
        elif mathematics == "2elevadoa":
            result = 2 ** functionnum
        elif mathematics == "inverso":
            result = functionnum ** -1
        elif mathematics == "seninverso":
            result = math.degrees(math.asin(functionnum))
        elif mathematics == "cosinverso":
            result = math.degrees(math.acos(functionnum))
        elif mathematics == "taninverso":
            result = math.degrees(math.atan(functionnum))
        else:
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


def create_func_button(text, command, row, col, color=color_func, colspan=1, width=6):
    btn = tk.Button(var, text=text, padx=15, pady=10, font=font_buttons,
                    bg=color, fg='white', activebackground='#bdc3c7',
                    activeforeground='#2c3e50', relief='flat',
                    borderwidth=0, highlightthickness=0,
                    command=command, width=width)
    btn.grid(row=row, column=col, columnspan=colspan, padx=2, pady=2, sticky="nsew")
    return btn


# Creación de botones numéricos
for i in range(1, 10):
    row = (9 - i) // 3 + 2
    col = (i - 1) % 3
    create_func_button(str(i), lambda num=i: thebutton(num), row, col, color_nums, width=5)

create_func_button("0", lambda: thebutton(0), 5, 1, color_nums, width=5)
create_func_button(".", lambda: thebutton("."), 5, 2, color_nums, width=5)
create_func_button("π", lambda: thebutton(math.pi), 5, 0, color_func, width=5)

# Botones de operaciones básicas
create_func_button("+", create_operation_func("adicion"), 2, 3, color_ops, width=5)
create_func_button("-", create_operation_func("sustraccion"), 3, 3, color_ops, width=5)
create_func_button("×", create_operation_func("multiplicacion"), 4, 3, color_ops, width=5)
create_func_button("÷", create_operation_func("division"), 5, 3, color_ops, width=5)

# Botones especiales
create_func_button("C", botonlimpiar, 1, 0, color_clear, width=5)
create_func_button("√", create_operation_func("raizcuadrada"), 1, 1, color_func, width=5)
create_func_button("^", create_operation_func("elevado"), 1, 2, color_func, width=5)
create_func_button("=", botonigual, 5, 4, color_equals, colspan=2, width=11)

# Botones científicos - Fila 1
create_func_button("sin", create_operation_func("sen"), 6, 0, color_trig)
create_func_button("cos", create_operation_func("cos"), 6, 1, color_trig)
create_func_button("tan", create_operation_func("tan"), 6, 2, color_trig)
create_func_button("log", create_operation_func("log"), 6, 3, color_func)
create_func_button("ln", create_operation_func("lognatural"), 6, 4, color_func)

# Botones científicos - Fila 2
create_func_button("asin", create_operation_func("seninverso"), 7, 0, color_inv_trig)
create_func_button("acos", create_operation_func("cosinverso"), 7, 1, color_inv_trig)
create_func_button("atan", create_operation_func("taninverso"), 7, 2, color_inv_trig)
create_func_button("x²", create_operation_func("cuadrado"), 7, 3, color_func)
create_func_button("x³", create_operation_func("cubo"), 7, 4, color_func)

# Botones científicos - Fila 3
create_func_button("csc", create_operation_func("csc"), 8, 0, color_trig)
create_func_button("sec", create_operation_func("sec"), 8, 1, color_trig)
create_func_button("cot", create_operation_func("cot"), 8, 2, color_trig)
create_func_button("|x|", create_operation_func("valorabsoluto"), 8, 3, color_func)
create_func_button("x⁻¹", create_operation_func("inverso"), 8, 4, color_func)

# Botones científicos - Fila 4
create_func_button("eˣ", create_operation_func("e"), 9, 0, color_func)
create_func_button("n!", create_operation_func("factorial"), 9, 1, color_func)
create_func_button("2ˣ", create_operation_func("2elevadoa"), 9, 2, color_func)
create_func_button("%", create_operation_func("porcentaje"), 9, 3, color_func)
create_func_button("±", create_operation_func("negativo"), 9, 4, color_func)

# Configuración de grid para mejor escalado
for i in range(10):
    var.grid_rowconfigure(i, weight=1)
for i in range(5):
    var.grid_columnconfigure(i, weight=1)


# Efecto hover para botones
def on_enter(e):
    e.widget['bg'] = '#95a5a6'


def on_leave(e):
    text = e.widget['text']
    if text in '0123456789.':
        e.widget['bg'] = color_nums
    elif text in '+-×÷':
        e.widget['bg'] = color_ops
    elif text == '=':
        e.widget['bg'] = color_equals
    elif text == 'C':
        e.widget['bg'] = color_clear
    elif text in ['sin', 'cos', 'tan', 'csc', 'sec', 'cot']:
        e.widget['bg'] = color_trig
    elif text in ['asin', 'acos', 'atan']:
        e.widget['bg'] = color_inv_trig
    else:
        e.widget['bg'] = color_func


for child in var.winfo_children():
    if isinstance(child, tk.Button):
        child.bind("<Enter>", on_enter)
        child.bind("<Leave>", on_leave)

var.mainloop()