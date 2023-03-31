class Maquina:
    def __init__(self, nombre, n_pines, m_elementos, elementos):
        self.nombre = nombre
        self.n_pines = n_pines
        self.m_elementos = m_elementos
        self.elementos = elementos

    def _analizar(self, compuesto):
        pines = {}
        for i in compuesto[1]:
            pin = 1
            col = 1
            movimientos = []
            for j in self.elementos:
                for e in j:
                    if i == e:
                        pines[i] = [pin, col]
                    col += 1
                col = 1
                pin += 1
                movimientos.append([])

        print(pines)

        for i in compuesto[1]:
            fila = pines[i][0]-1
            columna = pines[i][1]-1
            count = {}
            count[fila] = 0
            # print(fila)
            if count[fila] == 0:
                movimientos[fila].append("mover adelante")
                count[fila] += 1

            for j in self.elementos[fila]:
                print(j)
                print(count[fila])
                print(columna)
                print(f"fila {fila}")
                if count[fila] < columna + 1:
                    movimientos[fila].append("mover adelante")
                    print("adelante")
                elif count[fila] > columna + 1:
                    movimientos[fila].append("mover atras")
                    print("atras")
                elif count[fila] == columna + 1:

                    for mov in movimientos:
                        print(len(mov))
                        if len(mov) >= len(movimientos[fila]) + 1:
                            if mov[columna] == "Fusionar":
                                movimientos[fila].append("Esperar")
                            else:
                                movimientos[fila].append("Fusionar")
                        else:
                            movimientos[fila].append("Fusionar")
                    break

                count[fila] += 1
        print(movimientos)
