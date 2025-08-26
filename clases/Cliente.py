
class Cliente:
    def __init__(self, apellido, nombre, correo):
        self.__apellido = apellido
        self.__nombre = nombre
        self.__correo = correo 

    #Setters y Getters
    def setDisponible(self, numero):
        self.__numero=numero

    def getDisponible(self):
        return(self.__numero)
    
