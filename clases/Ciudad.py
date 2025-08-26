class Ciudad:
    def __init__(self, nombre, provincia, pais):
        self._nombre = nombre
        self._provincia = provincia
        self._pais=pais

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def provincia(self):
        return self._provincia

    @provincia.setter
    def provincia(self, value):
        self._provincia = value

    @property
    def pais(self):
        return self._pais

    @pais.setter
    def pais(self, value):
        self._pais = value


    
