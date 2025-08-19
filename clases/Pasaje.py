from Cliente import Cliente
from AsientoImp import AsientoImp

class Pasaje:
    def __init__(self, cliente ):
        self.cliente = cliente
        self.asiento = []
    

    def __str__(self):
        return f"Pasaje: {self.cliente}"

