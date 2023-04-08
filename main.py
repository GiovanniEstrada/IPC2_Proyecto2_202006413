import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import xml.etree.ElementTree as ET
import xml.dom.minidom
import graphviz as gv
from Analizador import Analizador
from NuevoElemento import NuevoElemento
import os

root = tk.Tk()
ListaElementos = []
ListaMaquinas = []
ListaCompuestos = []
archivoInput = ""
compuesto = ["", ""]
ListaMovimientos = []

root.geometry("700x600")

label = tk.Label(
    root, text="Sistema de Gestión de Elementos Químicos y Compuestos", font=("Arial", 18))
label.grid(row=0, column=0, columnspan=3, padx=20, pady=20)


def inicializar():
    pass


def cargar_xml():
    global archivoInput
    archivoInput = filedialog.askopenfilename(initialdir='/', title='Seleccionar archivo XML', filetypes=(
        ('Archivos XML', '*.xml'), ('Todos los archivos', '*.*')))
    Analizador(ListaElementos, ListaMaquinas, ListaCompuestos, archivoInput)


def generar_xml():
    global ListaMovimientos
    ListaMejoresMovimientos = []
    count = 0
    moveLength = 0
    move = []
    for i in ListaCompuestos:
        for j in ListaMaquinas:
            ListaMovimientos.append(j._analizar(i._valores()))

    cantidadMaquinas = len(ListaMaquinas)
    for movimiento in ListaMovimientos:
        count += 1
        print(movimiento[0][0])
        print(movimiento[0][1])
        if moveLength == 0:
            moveLength = len(movimiento[0])
            move = []
            move.append(movimiento)
        elif moveLength > len(movimiento[0]):
            moveLength = len(movimiento[0])
            move = []
            move.append(movimiento)

        if count == len(ListaMaquinas):
            ListaMejoresMovimientos.append(move)
            moveLength = 0
            count = 0

    for i in ListaMejoresMovimientos:
        print(i)
        print("-------------------------------")

    root = ET.Element("RESPUESTA")

    listaCompuestos = ET.SubElement(root, "listaCompuestos")

    for i in ListaMejoresMovimientos:
        contadorSegundos = 0
        for j in i:
            compuesto = ET.SubElement(listaCompuestos, "compuesto")
            nombre = ET.SubElement(compuesto, "nombre")
            nombre.text = j[0][1]
            maquina = ET.SubElement(compuesto, "maquina")
            maquina.text = j[0][0]
            tiempoOptimo = ET.SubElement(compuesto, "tiempoOptimo")
            tiempoOptimo.text = str(len(j[0]) - 3)
            instrucciones = ET.SubElement(compuesto, "instrucciones")
            print(j[0][0])
            valInicial = 3
            for k in range(len(j[0])-3):
                contadorSegundos += 1
                tiempo = ET.SubElement(instrucciones, "tiempo")
                numeroSegundo = ET.SubElement(tiempo, "numeroSegundo")
                numeroSegundo.text = str(contadorSegundos)
                acciones = ET.SubElement(tiempo, "acciones")
                for l in j:
                    try:
                        print(l[valInicial])
                        accionPin = ET.SubElement(acciones, "accionPin")
                        numeroPin = ET.SubElement(accionPin, "numeroPin")
                        numeroPin.text = str(l[2])
                        accion = ET.SubElement(accionPin, "accion")
                        accion.text = str(l[valInicial])
                        print(f"pruebas {l[valInicial]}")
                    except:
                        print("fin ciclo...")
                print(f"contador segundos: {contadorSegundos}")
                print(f"total segundos {len(j[0]) - 3}")
                valInicial += 1
                if contadorSegundos == (len(j[0]) - 3):
                    break
            print("end")

        tree = ET.ElementTree(root)

        with open("Output.xml", "wb") as f:
            tree.write(f, encoding="UTF-8", xml_declaration=True)

        with open("Output.xml", "r") as f:
            xml_string = f.read()

        dom = xml.dom.minidom.parseString(xml_string)
        pretty_xml = dom.toprettyxml()

        with open("Salida.xml", "w") as f:
            f.write(pretty_xml)


elementos_quimicos = []


def crear_tabla():

    tabla_window = tk.Toplevel(root)
    tabla_window.title("Tabla de elementos químicos")

    tabla = ttk.Treeview(tabla_window, columns=(
        "numero_atomico", "simbolo", "nombre"), show="headings")
    tabla.pack()

    tabla.heading("numero_atomico", text="Número Atómico")
    tabla.heading("simbolo", text="Símbolo")
    tabla.heading("nombre", text="Nombre")

    for elemento in ListaElementos:
        tabla.insert("", tk.END, values=(elemento.numero_atomico,
                     elemento.simbolo, elemento.nombre))


def agregar_elemento():
    rootAgregar = tk.Tk()
    rootAgregar.withdraw()
    Agregar = NuevoElemento(rootAgregar, archivoInput)
    rootAgregar.mainloop()


def gestionar_elementos_quimicos():

    n = len(ListaElementos)
    # Recorrer todos los elementos de la lista
    for i in range(n):
        # Últimos i elementos ya están en su lugar
        for j in range(n-i-1):
            # Intercambiar si el elemento encontrado es mayor que el siguiente elemento
            if ListaElementos[j].numero_atomico > ListaElementos[j+1].numero_atomico:
                ListaElementos[j], ListaElementos[j +
                                                  1] = ListaElementos[j+1], ListaElementos[j]
    for i in ListaElementos:
        print(i._lista())
    elem_window = tk.Toplevel(root)
    elem_window.geometry("600x400")
    elem_window.title("Gestión de Elementos Químicos")

    label1 = tk.Label(
        elem_window, text="Elementos Químicos", font=("Arial", 14))
    label1.pack(pady=10)

    button1 = tk.Button(
        elem_window, text="Listado de elementos quimicos", width=30, height=3, command=crear_tabla)
    button1.pack(pady=10)

    button2 = tk.Button(
        elem_window, text="Agregar elemento químico", width=30, height=3, command=agregar_elemento)
    button2.pack(pady=10)


def gestionar_compuestos():
    comp_window = tk.Toplevel(root)
    comp_window.geometry("600x400")
    comp_window.title("Gestión de Compuestos")

    label1 = tk.Label(
        comp_window, text="Lista de Compuestos y sus Fórmulas", font=("Arial", 14))
    label1.pack(pady=10)

    button1 = tk.Button(comp_window, text="Listado de compuestos", width=30, height=3,
                        command=listado_compuestos)
    button1.pack(pady=10)
    button2 = tk.Button(comp_window, text="Analizar compuesto", width=30, height=3,
                        command=analizar_compuesto)
    button2.pack(pady=10)


def listado_compuestos():
    tabla_compuestos = tk.Toplevel(root)
    tabla_compuestos.title("Tabla de compuestos")

    tabla = ttk.Treeview(tabla_compuestos, columns=(
        "Nombre", "Elemento"), show="headings")
    tabla.pack()

    tabla.heading("Nombre", text="Nombre")
    tabla.heading("Elemento", text="Elemento")

    for c in ListaCompuestos:
        print(c.nombre)
        tabla.insert("", tk.END, values=(c.nombre, c.elemento))


def analizar_compuesto():
    analizar_c = tk.Toplevel(root)
    analizar_c.geometry("600x400")
    analizar_c.title("Analizar compuesto")

    label1 = tk.Label(
        analizar_c, text="Analizar compuesto", font=("Arial", 14))
    label1.pack(pady=10)

    button1 = tk.Button(
        analizar_c, text="Seleccionar un compuesto", width=30, height=3, command=seleccionar_compuesto)
    button1.pack(pady=10)

    button2 = tk.Button(
        analizar_c, text="Ver maquinas y tiempos", width=30, height=3, command=maquinas_y_tiempo)
    button2.pack(pady=10)

    button3 = tk.Button(
        analizar_c, text="Ver instrucciones graficamente", width=30, height=3, command=agregar_elemento)
    button3.pack(pady=10)


def seleccionar_compuesto():
    tabla_compuestos = tk.Toplevel(root)
    tabla_compuestos.title("Tabla de compuestos")

    tabla = ttk.Treeview(tabla_compuestos, columns=(
        "Nombre", "Elemento"), show="headings")
    tabla.pack()

    tabla.heading("Nombre", text="Nombre")
    tabla.heading("Elemento", text="Elemento")

    for c in ListaCompuestos:
        print(c.nombre)
        tabla.insert("", tk.END, values=(c.nombre, c.elemento))

    tabla.bind('<ButtonRelease-1>',
               lambda event: click_elemento(event, tabla, tabla_compuestos))


def click_elemento(event, tabla, window):

    global compuesto
    item = tabla.focus()

    values = tabla.item(item)['values']
    print(values)
    compuesto[0] = values[0]
    compuesto[1] = values[1]

    print(compuesto)

    window.destroy()


def gestionar_maquinas():
    maq_window = tk.Toplevel(root)
    maq_window.geometry("600x400")
    maq_window.title("Gestión de Máquinas")

    label1 = tk.Label(maq_window, text="Lista de Máquinas", font=("Arial", 14))
    label1.grid(row=0, column=0, columnspan=3, padx=20, pady=20)


def maquinas_y_tiempo():
    global ListaMovimientos
    global compuesto

    ventana = tk.Toplevel()
    ventana.title(f"Ver máquinas y tiempo, Compuesto: {compuesto[0]}")

    tabla = ttk.Treeview(ventana, columns=(
        "nombre", "tiempo_optimo"), show="headings")
    tabla.pack()

    tabla.heading("nombre", text="Nombre de máquina")
    tabla.heading("tiempo_optimo", text="Tiempo óptimo")

    for i in ListaMovimientos:
        for j in i:
            if j[1] == compuesto[0]:
                tabla.insert("", tk.END, values=(
                    j[0], len(j) - 3))
                break


def graficar_maquinas():
    try:

        archivoDOT = open("grafico.dot", "w")
        archivoDOT.write("digraph { \n")
        archivoDOT.write('rankdir = LR \n')
        archivoDOT.write(
            'node[shape=record, fontname="Arial Black", fontsize=16] \n')

        for i in listaPeliculas:
            print(i)
            archivoDOT.write(
                i["indice"]+'[label="{' + i["pelicula"] + '}' + '| {' + i["anio"] + '|' + i["genero"] + '}"]\n')

        archivoDOT.write("} \n")
        archivoDOT.close()
        os.system("dot.exe -Tpng grafico.dot -o  ReporteGrafico.png")
    except:
        print("*********")
    finally:
        archivoDOT.close()


def ayuda():
    ventana_usuario = tk.Tk()
    ventana_usuario.title("Temas de ayuda")

    nombre = tk.Label(
        ventana_usuario, text="Nombre: Cristian Giovanni Estrada Ramirez")
    carnet = tk.Label(ventana_usuario, text="Carnet: 202006413")
    gmail = tk.Label(
        ventana_usuario, text="Correo: 2991897830101@ingenieria.usac.edu.gt")
    curso = tk.Label(
        ventana_usuario, text="Introduccion a la Programacion y Computacion 2")

    nombre.pack()
    carnet.pack()
    gmail.pack()
    curso.pack()


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
