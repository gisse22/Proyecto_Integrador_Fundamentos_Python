class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

    def guardar_informacion(self):
        with open("usuario.txt", "w") as archivo:
            archivo.write(self.nombre)