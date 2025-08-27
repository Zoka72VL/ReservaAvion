from clases.Ciudad import Ciudad
from clases.Avion import Avion
from clases.AsientoImp import AsientoImp

class Vuelo:
    def __init__(self, origen: Ciudad, destino: Ciudad, avion: Avion):
        self.origen = origen    #instancia de Ciudad
        self.destino = destino  #instancia de Ciudad
        self.avion = avion      #instancia de Avion

    @property
    def origen(self):
        return self._origen

    @origen.setter
    def origen(self, value):
        self._origen = value

    @property
    def destino(self):
        return self._destino

    @destino.setter
    def destino(self, value):
        self._destino = value

    @property
    def avion(self):
        return self._avion

    @avion.setter
    def avion(self, value):
        self._avion = value

    def obtener_asientos_disponibles(self) -> list[AsientoImp]:
        """
        Devuelve la lista de AsientoImplementado que están
        ligados a este vuelo y aún disponibles.
        """
        return [
            asiento for asiento in self._avion.asientos
            if isinstance(asiento, AsientoImp)
               and asiento.vuelo is self
               and asiento.disponible
        ]

