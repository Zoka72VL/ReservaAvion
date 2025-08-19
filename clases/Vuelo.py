class Vuelo:
    def __init__(self, origen, destino, avion):
        self.origen = origen
        self.destino = destino
        self.avion = avion

    def __str__(self):
        return f"Vuelo: {self.origen} {self.destino}, Avion: {self.avion}"
