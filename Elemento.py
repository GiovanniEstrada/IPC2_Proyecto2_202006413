class Elemento:

    def __init__(self, numero_atomico, simbolo, nombre):
        self.numero_atomico = numero_atomico
        self.simbolo = simbolo
        self.nombre = nombre

    def _mostrar(self):
        print(f"{self.nombre} \n")
