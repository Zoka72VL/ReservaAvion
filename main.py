from clases.Cliente import Cliente
from clases.Ciudad import Ciudad
from clases.Avion import Avion
from clases.Vuelo import Vuelo
from clases.AsientoImp import AsientoImp
from clases.Pasaje import Pasaje

# Crear ciudades
origen  = Ciudad("La Plata", "Buenos Aires", "Argentina")
destino = Ciudad("Córdoba", "Córdoba", "Argentina")

# Crear avión y vuelo
avion = Avion("Airbus A320", "LATAM")
vuelo = Vuelo(origen, destino, avion)

# Crear asientos implementados para ese vuelo
asientos = [
    AsientoImp(i, avion, "libre", vuelo, True)
    for i in range(1, 11)
]
avion.asientos = asientos

# Crear cliente
cliente = Cliente("González", "María", "maria.gonzalez@mail.com")

# Listar antes de reservar
print("Asientos disponibles antes:")
print([a.numero for a in vuelo.obtener_asientos_disponibles()])

# Cliente reserva 3 pasajes
pasaje = Pasaje.reservar(cliente, vuelo, 3)

# Mostrar el pasaje y su reserva
pasaje.mostrar_info()

# Listar después de reservar
print("\nAsientos disponibles después:")
print([a.numero for a in vuelo.obtener_asientos_disponibles()])