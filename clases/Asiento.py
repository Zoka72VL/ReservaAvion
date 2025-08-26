from Avion import Avion

class Asiento:
    def __init__(self, numero, estado, nombre, empresa):
        super().__init__(nombre, empresa)
        self.numero = numero 
        self.estado = estado

    #Setters y Getters
    def setNumero(self, numero):
        self.__numero=numero

    def getNumero(self):
        return(self.__numero)
    


    def setEstado(self, estado):
        self.__estado=estado

    def getEstado(self):
        return(self.__estado)
