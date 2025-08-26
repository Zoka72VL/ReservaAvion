
class Cliente:
    def __init__(self, apellido, nombre, correo):
        self._apellido = apellido
        self._nombre = nombre
        self._correo = correo 

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, value):
        self._apellido = value

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, value):
        if "@" not in value:
            raise ValueError("Correo inválido")
        self._correo = value

