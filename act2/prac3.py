class vuelo:
    def __init__(self, numero_vuelo, numero_pasajeros, destino):
        self.numero_vuelo = numero_vuelo
        self.numero_pasajeros = numero_pasajeros
        self.destino = destino

class avion:
    def __init__(self,asientos,destinos_permitidos):
        self.capacidad_asientos = asientos
        self.lista_destinos_permitidos = destinos_permitidos

print("--Bienvenido al sistema de vuelos--")
id_vuelo = input("Ingrese el numero de vuelo: ")
num_pasajeros = int(input("Ingrese el numero de pasajeros: "))
destino_vuelo = input("Ingrese el destino: ").strip().capitalize()

mi_vuelo = vuelo(id_vuelo, num_pasajeros, destino_vuelo)

print("\n--Datos del avion--")
capacidad_asientos = int(input("Ingrese la capacidad de asientos del avion: "))
destinos_permitidos_input = input("Ingrese los destinos permitidos (separados por comas): ")
destinos_permitidos = [d.strip().capitalize() for d in destinos_permitidos_input.split(",")]

mi_avion = avion(capacidad_asientos, destinos_permitidos)


print("\n--verifacion de disponibilidad--")

check_espacio = mi_avion.capacidad_asientos >= mi_vuelo.numero_pasajeros
check_destino = mi_vuelo.destino in mi_avion.lista_destinos_permitidos

if check_espacio and check_destino:
    print("El vuelo es posible :3")
else:    
    print("El vuelo no es posible :c")
    if not check_espacio:
        print("Razon: No hay suficiente espacio en el avion.")
    if not check_destino:
        print("Razon: El destino no esta permitido para este avion.")
        