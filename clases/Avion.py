class Avion:
    def __init__(self, nombre, empresa):
        self.nombre = nombre
        self.empresa = empresa 
        self.asientos = []


    def __str__(self):
        return f"Nombre: {self.nombre} de la empresa {self.empresa}"
