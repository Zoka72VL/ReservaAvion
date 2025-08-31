from clases.Cliente import Cliente
from clases.Asiento import Asiento
from clases.Ciudad import Ciudad
from clases.Avion import Avion
from clases.Vuelo import Vuelo
from clases.AsientoImp import AsientoImp
from clases.Pasaje import Pasaje

# Crear ciudades
ciudades = [
    Ciudad("La Plata", "Buenos Aires", "Argentina"),
    Ciudad("Córdoba", "Córdoba", "Argentina"),
    Ciudad("Mendoza", "Mendoza", "Argentina"),
    Ciudad("Rosario", "Santa Fe", "Argentina"),
]

# Crear hasta 3 aviones con sus propios origen y destino
aviones = []
vuelos = []
capacidad = 10

for idx in range(3):
    print(f"\n--- Configuración del avión {idx+1} ---")
    nombre_avion = input(f"Ingrese nombre del avión {idx+1}: ")
    empresa_avion = input(f"Ingrese empresa del avión {idx+1}: ")

    print("Seleccione ciudad de origen:")
    for i, ciudad in enumerate(ciudades):
        print(f"{i+1}. {ciudad.nombre} ({ciudad.provincia}, {ciudad.pais})")
    origen_idx = int(input("Número de ciudad de origen: ")) - 1

    print("Seleccione ciudad de destino:")
    for i, ciudad in enumerate(ciudades):
        if i != origen_idx:
            print(f"{i+1}. {ciudad.nombre} ({ciudad.provincia}, {ciudad.pais})")
    destino_idx = int(input("Número de ciudad de destino: ")) - 1

    avion = Avion(nombre_avion, empresa_avion)
    vuelo = Vuelo(ciudades[origen_idx], ciudades[destino_idx], avion)
    asientos = [AsientoImp(i+1, avion, "libre", vuelo, True) for i in range(capacidad)]
    avion.asientos = asientos

    aviones.append(avion)
    vuelos.append(vuelo)

# Reservas
while True:
    # Mostrar vuelos con asientos disponibles
    vuelos_disponibles = [v for v in vuelos if v.obtener_asientos_disponibles()]
    if not vuelos_disponibles:
        print("\n¡Todos los aviones están llenos! No se pueden reservar más pasajes.")
        break

    print("\nVuelos disponibles:")
    for i, vuelo in enumerate(vuelos_disponibles):
        print(f"{i+1}. {vuelo.origen.nombre} -> {vuelo.destino.nombre} | Avión: {vuelo.avion.nombre} ({vuelo.avion.empresa})")

    vuelo_idx = int(input("Seleccione el vuelo por número: ")) - 1
    vuelo = vuelos_disponibles[vuelo_idx]

    disponibles = vuelo.obtener_asientos_disponibles()
    print(f"\nAsientos disponibles en {vuelo.avion.nombre}: {[a.numero for a in disponibles]}")

    nombre = input("Ingrese nombre del cliente: ")
    apellido = input("Ingrese apellido del cliente: ")
    correo = input("Ingrese correo del cliente: ")
    cliente = Cliente(apellido, nombre, correo)

    while True:
        try:
            cantidad = int(input(f"Ingrese cantidad de asientos a reservar (máximo {len(disponibles)}): "))
            if cantidad < 1 or cantidad > len(disponibles):
                print("Cantidad inválida.")
                continue
            break
        except ValueError:
            print("Ingrese un número válido.")

    pasaje = Pasaje.reservar(cliente, vuelo, cantidad)
    print("\n--- Datos de la reserva ---")
    pasaje.mostrar_info()
    print(f"Avión: {vuelo.avion.nombre} ({vuelo.avion.empresa})")
    print(f"Origen: {vuelo.origen.nombre} ({vuelo.origen.provincia}, {vuelo.origen.pais})")
    print(f"Destino: {vuelo.destino.nombre} ({vuelo.destino.provincia}, {vuelo.destino.pais})")

print("\nReservas finalizadas. Asientos ocupados por avión:")
for avion in aviones:
    ocupados = [a.numero for a in avion.asientos if not a.disponible]
    print(f"{avion.nombre}: {ocupados}")