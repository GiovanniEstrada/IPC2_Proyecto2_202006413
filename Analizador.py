import xml.etree.ElementTree as ET
from Elemento import Elemento
from Maquina import Maquina
from Compuesto import Compuesto


def Analizador(ListaElementos, ListaMaquinas, ListaCompuestos, input):
    tree = ET.parse(input)
    root = tree.getroot()

    elementos = {}
    maquinas = []
    compuestos = []

    for elemento in root.findall('./listaElementos/elemento'):
        numero_atomico = int(elemento.find('numeroAtomico').text)
        simbolo = elemento.find('simbolo').text
        nombre = elemento.find('nombre').text
        elementos[numero_atomico] = {'simbolo': simbolo, 'nombre': nombre}

    # Leer lista de máquinas
    for maquina in root.findall('./listaMaquinas/Maquina'):
        nombre = maquina.find('nombre').text
        numero_pines = int(maquina.find('numeroPines').text)
        numero_elementos = int(maquina.find('numeroElementos').text)
        pines = []
        for pin in maquina.findall('pin'):
            elementos_pin = []
            for elemento in pin.findall('elementos/elemento'):
                elementos_pin.append(elemento.text)
            pines.append(elementos_pin)
        maquinas.append({'nombre': nombre, 'numero_pines': numero_pines,
                        'numero_elementos': numero_elementos, 'pines': pines})

    # Leer lista de compuestos
    for compuesto in root.findall('./listaCompuestos/compuesto'):
        nombre = compuesto.find('nombre').text
        elementos_compuesto = []
        for elemento in compuesto.findall('elementos/elemento'):
            elementos_compuesto.append(elemento.text)
        compuestos.append({'nombre': nombre, 'elementos': elementos_compuesto})

    # Imprimir resultados
    print('Lista de elementos---------------------------------------')
    for numero_atomico, elemento in elementos.items():

        tmp_elemento = Elemento(
            numero_atomico, elemento["simbolo"], elemento["nombre"])
        ListaElementos.append(tmp_elemento)
        print(
            f'{numero_atomico}: {elemento["simbolo"]} - {elemento["nombre"]}')

    print('\nmáquinas-----------------------------------------------')
    for maquina in maquinas:
        tmp_maquina = Maquina(maquina["nombre"], maquina["numero_pines"],
                              maquina["numero_elementos"], maquina["pines"])
        ListaMaquinas.append(tmp_maquina)
        print(
            f'{maquina["nombre"]} - {maquina["numero_pines"]} pines, {maquina["numero_elementos"]} elementos')
        for pin in maquina['pines']:
            print(f'\t{pin}')

    print('\ncompuestos-------------------------------------------')
    for compuesto in compuestos:
        tmp_compuesto = Compuesto(compuesto["nombre"], compuesto["elementos"])
        ListaCompuestos.append(tmp_compuesto)
        print(f'{compuesto["nombre"]} - {compuesto["elementos"]}')
