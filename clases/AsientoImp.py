from clases.Asiento import Asiento

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


    def algun_metodo(self):
        from clases.Vuelo import Vuelo
        # usa Vuelo aquí

