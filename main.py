import time
from usuario import Usuario
from juego import JuegoArchivo

# Solicitar el nombre del jugador
nombre = input("Por favor, introduce tu nombre: ")

# Crear una instancia de Usuario y guardar la información
usuario = Usuario(nombre)
usuario.guardar_informacion()

# Imprimir un mensaje de bienvenida con el nombre
print(f"¡Bienvenido, {nombre}! \nIniciando nueva partida...")

time.sleep(1.5)

# Instanciar el juego y ejecutarlo
juego = JuegoArchivo("mapas")
juego.main_loop()
