import os
import time
import readchar  # Importar la biblioteca readchar

# Función para convertir el mapa del laberinto en una matriz de caracteres
def convertir_mapa(mapa_str):
    mapa_lista = mapa_str.strip().split('\n')
    mapa = [list(fila) for fila in mapa_lista]
    return mapa

# Función para limpiar la pantalla y mostrar el mapa
def mostrar_mapa(mapa):
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar la pantalla

    for fila in mapa:
        print(''.join(fila))

# Función principal del juego
def main_loop(mapa, inicio, final):
    px, py = inicio  # Coordenadas iniciales del jugador
    mapa[px][py] = 'P'  # Colocar al jugador en la posición inicial

    while (px, py) != final:
        mostrar_mapa(mapa)
        tecla = readchar.readkey()  # Leer una tecla con readchar

        # Salir del juego si se presiona '\x1b'
        if tecla == '\x1b':
            break

        nueva_px, nueva_py = px, py  # Inicializar nuevas coordenadas tentativas

        # Actualizar las coordenadas tentativas según la tecla presionada
        if tecla == '\x00H' and px > 0 and mapa[px - 1][py] != '#':
            nueva_px = px - 1
        elif tecla == '\x00P' and px < len(mapa) - 1 and mapa[px + 1][py] != '#':
            nueva_px = px + 1
        elif tecla == '\x00K' and py > 0 and mapa[px][py - 1] != '#':
            nueva_py = py - 1
        elif tecla == '\x00M' and py < len(mapa[0]) - 1 and mapa[px][py + 1] != '#':
            nueva_py = py + 1

        # Actualizar el mapa con las coordenadas tentativas
        mapa[px][py] = '.'
        mapa[nueva_px][nueva_py] = 'P'

        # Actualizar las coordenadas actuales
        px, py = nueva_px, nueva_py

        time.sleep(0.5)  # Pausa para una mejor visualización

    mostrar_mapa(mapa)
    if (px, py) == final:
        print("¡Has llegado al final del laberinto!")

# Mapa del laberinto en forma de cadena
mapa_str = """
P.####
#.#..#
#...##
###..#
####.#
"""

# Convertir el mapa en una matriz de caracteres
mapa = convertir_mapa(mapa_str)

# Posición inicial y final
inicio = (0, 0)
final = (4, 4)

# Iniciar el bucle principal del juego
main_loop(mapa, inicio, final)
