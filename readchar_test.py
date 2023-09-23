import readchar

def main():
    print("El programa se ejecutará hasta que se presione la tecla ↑ (UP).")
    
    while True:
        key = readchar.readkey()
        
        if key == '\x00H':  # La tecla "↑" (UP) produce el carácter ('\x00H')
            print("Se ha presionado la tecla ↑ (UP). Saliendo del programa.")
            break
        else:
            print("Tecla presionada:", (repr(key)))

if __name__ == "__main__":
    main()