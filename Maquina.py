class Maquina:
    def __init__(self, nombre, n_pines, m_elementos, elementos):
        self.nombre = nombre
        self.n_pines = n_pines
        self.m_elementos = m_elementos
        self.elementos = elementos

    def _analizar(self, compuesto):
        pines = {}
        count = {}
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
                movimientos.append([self.nombre, compuesto[0], pin])
                count[pin-1] = 0
                pin += 1

        # print(movimientos)

        print(f"Compuesto {pines}")
        for i in compuesto[1]:
            fila = pines[i][0]-1
            columna = pines[i][1]
            if count[fila] == 0:
                movimientos[fila].append("right")
                count[fila] += 1

            for j in self.elementos[fila]:
                if count[fila] < columna:
                    movimientos[fila].append("right")
                    count[fila] += 1

                elif count[fila] > columna:
                    movimientos[fila].append("left")
                    count[fila] -= 1

                elif count[fila] == columna:
                    movimientos[fila].append("Fusion")

                    break
                else:
                    movimientos[fila].append("Wait")
                    count[fila] += 1

        # Agregar espera a las fusiones que se estan ejecutando a la vez
        columnaFusion = 0
        filaFusion = 0
        for i in compuesto[1]:
            contadorColumnas = 0
            fila = pines[i][0] - 1
            for j in movimientos[fila]:
                contadorColumnas += 1
                if j == "Fusion":

                    if contadorColumnas <= columnaFusion and filaFusion != fila:
                        # print(f"contador columnas {contadorColumnas}")
                        # print(f"contador fusion {columnaFusion}")
                        movimientos[fila].insert(
                            contadorColumnas - 1, "Wait")
                    else:
                        filaFusion = fila
                        movimientos[fila][contadorColumnas -
                                          1] = "NewFusion"
                        columnaFusion = contadorColumnas
                        break

        longitud_maxima = max(map(len, movimientos))

        nuevos_movimientos = [s + ["Wait"] *
                              (longitud_maxima - len(s)) for s in movimientos]

        return nuevos_movimientos
