import tkinter as tk
from tkinter import filedialog
import xml.etree.ElementTree as ET
import graphviz as gv
from Analizador import Analizador

root = tk.Tk()
ListaElementos = []
ListaMaquinas = []
ListaCompuestos = []

root.geometry("700x600")

label = tk.Label(
    root, text="Sistema de Gestión de Elementos Químicos y Compuestos", font=("Arial", 18))
label.grid(row=0, column=0, columnspan=3, padx=20, pady=20)


def inicializar():
    pass


def cargar_xml():
    archivoInput = filedialog.askopenfilename(initialdir='/', title='Seleccionar archivo XML', filetypes=(
        ('Archivos XML', '*.xml'), ('Todos los archivos', '*.*')))
    Analizador(ListaElementos, ListaMaquinas, ListaCompuestos, archivoInput)


def generar_xml():
    for i in ListaCompuestos:
        for j in ListaMaquinas:
            j._analizar(i._valores())


elementos_quimicos = []


def ordenar_por_num_atomico():
    pass


def agregar_elemento():
    pass


def gestionar_elementos_quimicos():
    elem_window = tk.Toplevel(root)
    elem_window.geometry("600x400")
    elem_window.title("Gestión de Elementos Químicos")

    label1 = tk.Label(
        elem_window, text="Lista de Elementos Químicos", font=("Arial", 14))
    label1.pack(pady=10)

    button1 = tk.Button(
        elem_window, text="Ordenar por número atómico", command=ordenar_por_num_atomico)
    button1.pack(pady=10)

    button2 = tk.Button(
        elem_window, text="Agregar elemento químico", command=agregar_elemento)
    button2.pack(pady=10)


def gestionar_compuestos():
    comp_window = tk.Toplevel(root)
    comp_window.geometry("600x400")
    comp_window.title("Gestión de Compuestos")

    label1 = tk.Label(
        comp_window, text="Lista de Compuestos y sus Fórmulas", font=("Arial", 14))
    label1.pack(pady=10)

    button1 = tk.Button(comp_window, text="Analizar compuesto",
                        command=analizar_compuesto)
    button1.pack(pady=10)


def analizar_compuesto():
    pass


def gestionar_maquinas():
    maq_window = tk.Toplevel(root)
    maq_window.geometry("600x400")
    maq_window.title("Gestión de Máquinas")

    label1 = tk.Label(maq_window, text="Lista de Máquinas", font=("Arial", 14))
    label1.grid(row=0, column=0, columnspan=3, padx=20, pady=20)


def ayuda():
    pass


# button1 = tk.Button(root, text="Inicializar", width=30,
#                     height=3, command=inicializar)
# button1.grid(row=1, column=0, padx=5, pady=10)

button2 = tk.Button(
    root, text="Cargar archivo XML de entrada", width=30, height=3, command=cargar_xml)
button2.grid(row=1, column=0, padx=5, pady=10)

button3 = tk.Button(
    root, text="Generar archivo XML de salida", width=30, height=3, command=generar_xml)
button3.grid(row=1, column=1, padx=5, pady=10)

button4 = tk.Button(root, text="Gestión de Elementos Químicos", width=30, height=3,
                    command=gestionar_elementos_quimicos)
button4.grid(row=1, column=2, padx=5, pady=10)

button5 = tk.Button(root, text="Gestión de Compuestos", width=30, height=3,
                    command=gestionar_compuestos)
button5.grid(row=2, column=0, padx=5, pady=10)

button6 = tk.Button(root, text="Gestión de Máquinas", width=30, height=3,
                    command=gestionar_maquinas)
button6.grid(row=2, column=1, padx=5, pady=5)

button7 = tk.Button(root, text="Ayuda", width=30, height=3, command=ayuda)
button7.grid(row=2, column=2, padx=5, pady=10)

root.mainloop()
