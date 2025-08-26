from Asiento import Asiento
from Vuelo import Vuelo

class AsientoImp(Asiento):
    def __init__(self, numero, avion, estado, vuelo, disponible):
        super().__init__(numero, avion, estado)
        self._vuelo = vuelo            # instancia de Vuelo
        self._disponible = disponible  # booleano

    @property
    def vuelo(self):
        return self._vuelo

    @vuelo.setter
    def vuelo(self, value):
        self._vuelo = value

    @property
    def disponible(self):
        return self._disponible

    @disponible.setter
    def disponible(self, value):
        if not isinstance(value, bool):
            raise ValueError("Disponible debe ser booleano")
        self._disponible = value
    
