import os
import msvcrt  # Esta librería se usa para leer teclas en Windows

def borrar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    numero = 0

    while numero <= 50:
        borrar_pantalla()
        print("Número:", numero)
        print("Presiona la tecla 'n' para continuar...")
        
        # Esperar a que se presione la tecla 'n'
        while True:
            if msvcrt.kbhit():
                tecla = msvcrt.getch().decode('utf-8').lower()
                if tecla == 'n':
                    break
        
        numero += 1

if __name__ == "__main__":
    main()
