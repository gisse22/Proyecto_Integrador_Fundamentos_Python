# Proyecto_Integrador_Fundamentos_Python

El proyecto de este curso consistirá en un videojuego de texto de recorrer laberintos. Este consistirá de laberintos representados por caracteres ASCII dónde **#** representará una pared, **.** un pasillo y **P** el personaje.

Podrás moverte por el mapa usando las teclas ↑ ↓ ← → de tu teclado.

### Instrucciones
Debemos aprender a usar la librería `readchar` que nos permitirá leer un caracter suelto del teclado, para ello se debe instalar la librería: https://pypi.org/project/readchar/

### Conocer la terminal
Se puede hacer uso de una terminal nativa como el CMD de windows o una instalada como Git Bash

### Funcion que reciba el mapa de un laberinto en forma de cadena y lo convierta en matriz de caracteres
1. Para generar los laberintos, usar esta página: https://www.dcode.fr/maze-generator con las configuraciones
   1. USE THIS CHARACTER FOR WALLS: #
   2. USE THIS CHARACTER FOR PATHS: .
   3. SINGLE CHARARACTER (MORE RECTANGULAR)
2. Completar los dos caracteres de paredes faltantes al final.
3. Los puntos inicial y final deben ser dados al crear el juego, usar las coordenadas (0,0) para el inicio y (end, end) para el final (Asegurarse que las coordenadas son caminos válidos)
4. Recuerdo: Para separar por filas usar split("\n") y para convertir una cadena a una lista de caracteres usar list(cadena).

### Función que limpie la pantalla y muestre la matriz (recibe el mapa en forma de matriz)
1. Recibir: mapa List[List[str]], posicion inicial Tuple[int, int], posicion final Tuple[int, int].
2. Definir dos variavles px y py que contienen las coordenadas del jugador, iniciar como los valores de la posición incial
3. Procesar mientras (px, py) no coincida con la coordenada final

### POO
Se encapsulan en clases y se empieza a dividir el codigo para mejorar su escalabilidad