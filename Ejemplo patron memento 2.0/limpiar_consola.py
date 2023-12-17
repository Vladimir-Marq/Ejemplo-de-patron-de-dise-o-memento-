"Limpiador de consola"

import os

def limpiar_consola():
    """Limpia la consola"""
    if os.name == 'nt':  # Para Windows
        os.system('cls')
    else:  # Probablemente Linux, Unix, Mac
        os.system('clear')

# Llamas a esta función en el momento que desees limpiar la consola
#limpiar_consola()
