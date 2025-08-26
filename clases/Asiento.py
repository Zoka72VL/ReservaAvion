
class Asiento:
    def __init__(self, numero, avion, estado):
        self._numero = numero
        self._avion = avion      # instancia de Avion
        self._estado = estado    # "libre" o "ocupado"

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, value):
        self._numero = value

    @property
    def avion(self):
        return self._avion

    @avion.setter
    def avion(self, value):
        self._avion = value

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, value):
        if value not in ("libre", "ocupado"):
            raise ValueError("Estado debe ser 'libre' o 'ocupado'")
        self._estado = value
