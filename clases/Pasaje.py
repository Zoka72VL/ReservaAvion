from Cliente import Cliente
from AsientoImp import AsientoImp

class Pasaje:
    def __init__(self, cliente: Cliente, asiento: list[AsientoImp]):
        self.cliente = cliente  # instancia de cliente
        self.asiento = asiento  #lista de asiento implementado
    
    @property
    def cliente(self):
        return self._cliente

    @cliente.setter
    def cliente(self, value):
        if not isinstance(value, Cliente):
            raise ValueError("Debe ser una instancia de Cliente")
        self._cliente = value

    @property
    def asientos(self):
        return self._asientos

    @asientos.setter
    def asientos(self, lista):
        if not all(isinstance(a, AsientoImp) for a in lista):
            raise ValueError("Cada elemento debe ser AsientoImplementado")
        self._asientos = lista

    def mostrar_info(self):
        print(f"Pasaje de {self._cliente.nombre} {self._cliente.apellido}")
        print(f"Correo: {self._cliente.correo}")
        print("Asientos asignados:")
        for asiento in self._asientos:
            estado = "Disponible" if asiento._disponible else "No disponible"
            print(f" - Asiento {asiento._numero}: {asiento._estado} ({estado})")

    @classmethod
    def reservar(cls, cliente: Cliente, vuelo, cantidad: int):
        """
        Reserva 'cantidad' de asientos libres para el cliente en el vuelo dado.
        Marca cada asiento como ocupado y devuelve una instancia de Pasaje.
        """
        libres = vuelo._obtener_asientos_disponibles()
        if len(libres) < cantidad:
            raise ValueError("No hay suficientes asientos disponibles")
        seleccion = libres[:cantidad]
        for asiento in seleccion:
            asiento.disponible = False
            asiento.estado = "ocupado"
        return cls(cliente, seleccion)

