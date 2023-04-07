import tkinter as tk
import xml.etree.ElementTree as ET
import xml.dom.minidom


class NuevoElemento:
    def __init__(self, parent, url):
        self.url = url
        self.parent = parent
        self.top = tk.Toplevel(parent)
        self.top.title('Agregar nuevo elemento')

        tk.Label(self.top, text='Número atómico:').grid(row=0, column=0)
        self.numero_atomico = tk.Entry(self.top)
        self.numero_atomico.grid(row=0, column=1)

        tk.Label(self.top, text='Símbolo:').grid(row=1, column=0)
        self.simbolo = tk.Entry(self.top)
        self.simbolo.grid(row=1, column=1)

        tk.Label(self.top, text='Nombre:').grid(row=2, column=0)
        self.nombre_entry = tk.Entry(self.top)
        self.nombre_entry.grid(row=2, column=1)

        tk.Button(self.top, text='Agregar', command=self.add_element).grid(
            row=3, column=0, columnspan=2)

        self.top.mainloop()

    def add_element(self):
        numero_atomico = int(self.numero_atomico.get())
        simbolo = self.simbolo.get()
        nombre = self.nombre_entry.get()

        tree = ET.parse(self.url)
        root = tree.getroot()

        nuevo_elemento = ET.Element("elemento")
        ET.SubElement(nuevo_elemento, "numeroAtomico").text = str(
            numero_atomico)
        ET.SubElement(nuevo_elemento, "simbolo").text = simbolo
        ET.SubElement(nuevo_elemento, "nombre").text = nombre

        lista_elementos = root.find("listaElementos")
        lista_elementos.append(nuevo_elemento)

        tree.write(self.url)

        with open(self.url, 'r') as archivo:
            xml_str = archivo.read()

        xml_dom = xml.dom.minidom.parseString(xml_str)

        xml_indentado = xml_dom.toprettyxml(indent='  ')

        # Guardar el XML indentado en un archivo
        with open(self.url, 'w') as archivo:
            archivo.write(xml_indentado)

        self.top.destroy()
