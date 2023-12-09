"""main.py - Contiene el código principal del programa"""

from texto import Texto
from limpiar_consola import limpiar_consola

texto_ingresado = input("Ingrese el texto inicial: ")
texto = Texto(texto_ingresado)
texto.mostrar_estado_texto()

while True:
    print("\nAcciones disponibles:")
    print("1. Editar texto")
    print("2. Restaurar estado")
    print("3. Mostrar historial de estados")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        limpiar_consola()
        texto.mostrar_estado_texto()
        nuevo_texto = input("Ingrese el nuevo texto: ")
        texto.editar_contenido(nuevo_texto)
    elif opcion == "2":
        limpiar_consola()
        texto.mostrar_estado_texto()
        num_estado = int(
            input("Ingrese el número de estado a restaurar: ")) - 1
        texto.restaurar_estado_desde_memento(num_estado)
    elif opcion == "3":
        limpiar_consola()
        texto.mostrar_estado_texto()
        texto.mostrar_historial()
    elif opcion == "4":
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
