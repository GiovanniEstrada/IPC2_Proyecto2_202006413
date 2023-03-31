class Compuesto:
    def __init__(self, nombre, elemento):
        self.nombre = nombre
        self.elemento = elemento

    def _valores(self):
        return [self.nombre, self.elemento]
