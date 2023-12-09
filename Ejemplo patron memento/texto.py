"""texto.py - clase Texto que contiene el contenido del texto y el historial de estados guardados"""

from memento import Memento


class Texto:
    """Clase "Texto" que contiene el contenido del texto y el historial de estados guardados"""

    def __init__(self, contenido=''):
        self._contenido = contenido
        # Guardar el primer estado
        self._historial = [Memento(self._contenido)]
        self._indice_actual = 0  # Inicializar el atributo _indice_actual en el método __init__

    def obtener_contenido(self):
        """Obtener el contenido actual del texto"""
        return self._contenido

    def crear_memento(self):
        """Crear un memento con el estado actual del texto"""
        return Memento(self._contenido)

    def editar_contenido(self, nuevo_contenido):
        """Editar el contenido del texto"""
        self._contenido = nuevo_contenido
        memento = self.crear_memento()
        self.guardar_estado(memento)

    def guardar_estado(self, memento):
        """
        Guardar un estado en el historial.
        Se asegura de mantener los estados posteriores si se revierte y se edita nuevamente.
        """
        self._historial = self._historial[:self._indice_actual + 1]
        self._historial.append(memento)
        self._indice_actual += 1

    def restaurar_estado_desde_memento(self, indice):
        """Restaurar el estado del texto desde un memento dado un índice en el historial"""
        if 0 <= indice < len(self._historial):
            self._contenido = self._historial[indice].obtener_contenido()
            self._indice_actual = indice

    def obtener_estado_del_historial(self, indice):
        """Obtener un estado específico del historial"""
        if 0 <= indice < len(self._historial):
            return self._historial[indice]
        return None

    def mostrar_estado_texto(self):
        """Mostrar el estado actual del texto"""
        print("----Estado actual:", self.obtener_contenido(), "----")

    def mostrar_historial(self):
        """Mostrar el historial de estados guardados"""
        print("\nHistorial de estados guardados:")
        for i, memento in enumerate(self._historial):
            print(f"Version {i + 1}: {memento.obtener_contenido()}")
