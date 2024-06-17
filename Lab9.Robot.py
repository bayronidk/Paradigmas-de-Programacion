class Robot:
    def __init__(self, rejilla):
        self.rejilla = rejilla
        self.filas = len(rejilla)
        self.columnas = len(rejilla[0])
        self.ruta = []
        self.visitado = set()

    def es_valido(self, fila, columna):
        return 0 <= fila < self.filas and 0 <= columna < self.columnas and self.rejilla[fila][columna] == 0 and (fila, columna) not in self.visitado

    def encontrar_ruta_util(self, fila, columna):
        # Si se ha logrado
        if fila == self.filas - 1 and columna == self.columnas - 1:
            self.ruta.append((fila, columna))
            return True

        # Marcar visitada
        self.visitado.add((fila, columna))
        self.ruta.append((fila, columna))

        # Mover a la derecha
        if self.es_valido(fila, columna + 1) and self.encontrar_ruta_util(fila, columna + 1):
            return True
        
        # Mover hacia abajo
        if self.es_valido(fila + 1, columna) and self.encontrar_ruta_util(fila + 1, columna):
            return True

        # Retroceder
        self.ruta.pop()
        self.visitado.remove((fila, columna))
        return False

    def encontrar_ruta(self):
        if self.encontrar_ruta_util(0, 0):
            return self.ruta
        else:
            return "No se encontró ninguna ruta"

#Rejilla

rejilla = [
    [0, 0, 1, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [1, 0, 0, 0]
]

robot = Robot(rejilla)
ruta = robot.encontrar_ruta()
print(ruta)
