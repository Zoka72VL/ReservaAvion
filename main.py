from clases.Cliente import Cliente
from clases.Asiento import Asiento
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

# Ingresar asientos por teclado
asientos = []
capacidad = 10

for i in range(1, capacidad + 1):
    asientos.append(AsientoImp(i, avion, "libre", vuelo, True))
avion.asientos = asientos

while True:
    disponibles = vuelo.obtener_asientos_disponibles()
    if not disponibles:
        print("¡El avión está lleno! No se pueden reservar más pasajes.")
        break

    print(f"\nAsientos disponibles: {[a.numero for a in disponibles]}")
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
    pasaje.mostrar_info()

print("\nReservas finalizadas. Asientos ocupados:")
print([a.numero for a in avion.asientos if not a.disponible])