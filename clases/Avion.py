from clases.Asiento import Asiento

class Avion:
    def __init__(self, nombre, empresa, asientos=None):
        self._nombre = nombre
        self._empresa = empresa
        self._asientos = asientos or []     #lista de asiento

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def empresa(self):
        return self._empresa

    @empresa.setter
    def empresa(self, value):
        self._empresa = value

    @property
    def asientos(self):
        return self._asientos

    @asientos.setter
    def asientos(self, lista):
        if not all(isinstance(a, Asiento) for a in lista):
            raise ValueError("Todos los elementos deben ser instancias de Asiento")
        self._asientos = lista


