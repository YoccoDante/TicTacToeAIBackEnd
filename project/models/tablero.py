class Tablero():
    def __init__(self, mapa=None) -> None:
        self.mapa = mapa if mapa != None else [
                [' ',' ',' '],#0y
                [' ',' ',' '],#1y
                [' ',' ',' '],#2y
            #['0','1','2'],-X
            ]
          
    def colocar_ficha(self, pos:tuple, turno:bool):
        simbolo = 'X' if turno else 'O'
        fila, columna = pos[0], pos[1]
        if self.mapa[fila][columna] != ' ':
            return False
        self.mapa[fila][columna] = simbolo
        return True
    
    def hay_victoria(self, turno:bool):
        valor = 'X' if turno else 'O'
        for fila in self.mapa:
            if fila[0] == valor and fila[0] == fila[1] and fila[1] == fila[2]:
                return True
        for i in range(3):
            if self.mapa[0][i] == valor and self.mapa[0][i] == self.mapa[1][i] == self.mapa[2][i]:
                return True
        if self.mapa[0][0] == valor and self.mapa[0][0] == self.mapa[1][1] == self.mapa[2][2]:
            return True
        if self.mapa[0][2] == valor and self.mapa[0][2] == self.mapa[1][1] == self.mapa[2][0]:
            return True
        return False
    
    def hay_empate(self):
        jugados_contador = 0
        for fila in self.mapa:
            for valor in fila:
                if valor != ' ':
                    jugados_contador += 1
        if jugados_contador == 9:
            return True
        return False

    def pintar_tablero(self):
        print(f"""
            tablero = [
            [{self.mapa[0][0]},{self.mapa[0][1]},{self.mapa[0][2]}],#0y
            [{self.mapa[1][0]},{self.mapa[1][1]},{self.mapa[1][2]}],#1y
            [{self.mapa[2][0]},{self.mapa[2][1]},{self.mapa[2][2]}],#2y
           #[0,1,2],-X
        ]""")