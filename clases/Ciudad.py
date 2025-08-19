class Ciudad:
    def __init__(self, nombre, provincia, pais):
        self.nombre = nombre
        self.provincia = provincia
        self.pais=pais

    def __str__(self):
        return f"Ciudad: {self.nombre} {self.provincia}, Correo: {self.pais}"
