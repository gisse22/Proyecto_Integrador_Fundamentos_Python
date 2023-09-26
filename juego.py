import os
import time
import readchar
import random
from functools import reduce  # Importar la función reduce

class Juego:
    def __init__(self, mapa, inicio, final):
        self.mapa = mapa
        self.inicio = inicio
        self.final = final

    def convertir_mapa(self, mapa_str):
        mapa_lista = list(map(list, map(str.strip, mapa_str.strip().split('\n'))))
        return mapa_lista

    def mostrar_mapa(self):
        os.system('cls' if os.name == 'nt' else 'clear')

        for fila in self.mapa[:-2]:
            print(''.join(fila))

    def main_loop(self):
        px, py = self.inicio
        self.mapa[px][py] = 'P'

        while (px, py) != self.final:
            self.mostrar_mapa()
            tecla = readchar.readkey()

            if tecla == '\x1b':
                break

            nueva_px, nueva_py = px, py

            if tecla == '\x00H' and px > 0 and self.mapa[px - 1][py] != '#':
                nueva_px = px - 1
            elif tecla == '\x00P' and px < len(self.mapa) - 1 and self.mapa[px + 1][py] != '#':
                nueva_px = px + 1
            elif tecla == '\x00K' and py > 0 and self.mapa[px][py - 1] != '#':
                nueva_py = py - 1
            elif tecla == '\x00M' and py < len(self.mapa[0]) - 1 and self.mapa[px][py + 1] != '#':
                nueva_py = py + 1

            self.mapa[px][py] = '.'
            self.mapa[nueva_px][nueva_py] = 'P'

            px, py = nueva_px, nueva_py

            time.sleep(0.5)

        self.mostrar_mapa()
        if (px, py) == self.final:
            print("¡Has llegado al final del laberinto!")

class JuegoArchivo(Juego):
    def __init__(self, path_a_mapas):
        nombre_archivo = random.choice(os.listdir(path_a_mapas))
        path_completo = os.path.join(path_a_mapas, nombre_archivo)
        mapa_str = self.leer_mapa(path_completo)
        mapa = self.convertir_mapa(mapa_str)
        inicio, final = self.obtener_inicio_final(mapa_str)
        super().__init__(mapa, inicio, final)

    def leer_mapa(self, path):
        with open(path, 'r') as archivo:
            return archivo.read()

    def obtener_inicio_final(self, mapa_str):
        lineas = mapa_str.strip().split('\n')
        inicio = tuple(map(int, lineas[-2].split()))
        final = tuple(map(int, lineas[-1].split()))
        return inicio, final

# Instancia de JuegoArchivo, cargará un mapa aleatorio desde una carpeta llamada "mapas"
juego = JuegoArchivo("mapas")

# Iniciar el bucle principal del juego
juego.main_loop()
