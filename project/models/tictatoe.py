import copy
from project.models.tablero import Tablero
from random import choice

class TicTacToe():
    def __init__(self) -> None:
        self.turno = False

    def obtener_espacios_libres (self, mapa):
            libres = []
            for i in range(3):
                for j in range(3):
                    if mapa[i][j] == ' ':
                        libres.append((i,j))
            return libres

    def simular_jugadas(self, mapa, turno):
        espacios_libres = self.obtener_espacios_libres(copy.deepcopy(mapa))
        tablero_simulado = Tablero(mapa=copy.deepcopy(mapa))
        puntaje = 0

        for espacio in espacios_libres:
            tablero_simulado = Tablero(mapa=copy.deepcopy(mapa))
            tablero_simulado.colocar_ficha(turno=turno, pos=espacio)
            if tablero_simulado.hay_empate():
                puntaje += 0
            elif tablero_simulado.hay_victoria(False):
                puntaje += 1
            elif tablero_simulado.hay_victoria(True):
                puntaje += -2
            else:
                puntaje += self.simular_jugadas(turno=not turno, mapa=tablero_simulado.mapa)      
        return puntaje
        
    def obtener_ficha_auto(self, mapa):
        espacios_libres = self.obtener_espacios_libres(mapa)
        if len(espacios_libres) > 6:
            #self.tablero.colocar_ficha(pos=choice(espacios_libres), turno=self.turno)
            return choice(espacios_libres)
        
        jugadas = {}
        for espacio in espacios_libres:
            mapa_copia = copy.deepcopy(mapa)
            tablero_simulado = Tablero(mapa=mapa_copia)
            tablero_simulado.colocar_ficha(pos=espacio, turno=False)
            if tablero_simulado.hay_victoria(False):
                #self.tablero.colocar_ficha(pos=espacio, turno=False)
                return espacio
            puntaje_de_jugada = self.simular_jugadas(mapa=tablero_simulado.mapa, turno=True)
            #tablero_simulado.pintar_tablero()
            jugadas[espacio] = puntaje_de_jugada

        jugada_max = list(jugadas.keys())[0]
        for jugada in jugadas:
            if jugadas[jugada] >= jugadas[jugada_max]:
                jugada_max = jugada
        # print(jugadas)
        # print('Jugó:',jugada_max)
        #self.tablero.colocar_ficha(pos=jugada_max, turno=self.turno)
        return jugada_max