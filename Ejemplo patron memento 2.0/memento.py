"""memento.py - Contiene la clase Memento que contiene el estado del texto en un momento dado"""


class Memento:
    """Clase Memento que contiene el estado del texto en un momento dado"""

    def __init__(self, contenido):
        self._contenido = contenido

    def obtener_contenido(self):
        """Obtener el contenido del memento"""
        return self._contenido

    def __eq__(self, otro):
        """Comparar si dos mementos son iguales"""
        return isinstance(otro, Memento) and self._contenido == otro.obtener_contenido()

    def __hash__(self):
        """Obtener el hash del memento"""
        return hash(self._contenido)
