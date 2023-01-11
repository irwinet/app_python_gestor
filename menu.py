import os

def iniciar():
    while True:
        os.system('cls')
        print("==========================")
        print("   Bienvenido al Gestor   ")
        print("==========================")
        print("[1] Listar los clientes   ")
        print("[2] Buscar un cliente     ")
        print("[3] Añadir un cliente     ")
        print("[4] Modificar un cliente  ")
        print("[5] Borrar un cliente     ")
        print("[6] Cerrar el Gestor      ")
        print("==========================")

        opcion = input("> ")
        os.system('cls')

        if opcion == '1':
            print("Listando los clientes...\n")
            # TODO 
        elif opcion == '2':
            print("Buscando un cliente...\n")
            # TODO 
        elif opcion == '3':
            print("Añadiendo un cliente...\n")
            # TODO 
        elif opcion == '4':
            print("Modificando un cliente...\n")
            # TODO 
        elif opcion == '5':
            print("Borrando un cliente...\n")
            # TODO
        elif opcion == '6':
            print("Saliendo...\n")
            break
        
        input("\nPresiona ENTER para continuar...")