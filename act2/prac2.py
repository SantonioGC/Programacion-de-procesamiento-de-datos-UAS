class personaje:
    def __init__(self,nombre,nivel,vida):
        self.nombre = nombre
        self.nivel = nivel
        self.vida = vida
    
    def mostrar_informacion_personaje(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nivel: {self.nivel}")
        print(f"Vida: {self.vida}")

class Guerrero(personaje):
    def __init__(self,nombre,nivel,vida,fuerza):
        super().__init__(nombre,nivel,vida)
        self.fuerza = fuerza
    
    def mostrar_informacion_personaje(self):
        base = super().mostrar_informacion_personaje()
        print(f"Fuerza: {self.fuerza}")

class Mago(personaje):
    def __init__(self,nombre,nivel,vida,magia):
        super().__init__(nombre,nivel,vida)
        self.magia = magia
    
    def mostrar_informacion_personaje(self):
        base = super().mostrar_informacion_personaje()
        print(f"Magia: {self.magia}")

print("--Bienvenido al sistema de personajes--")
tipo =input("Que quieres ser? (Guerrero/Mago): ").strip().lower() #agregue esto profe por si lo escribe con mayusculas o espacio ta perron 

nombre = input("Nombre de personaje: ")
nivel = int(input("Nivel del personaje: "))
vida = int(input("Vida del personaje: "))

if tipo == 'guerrero':
    fuerza = int(input("Fuerza del guerrero: "))
    nuevo_personaje = Guerrero(nombre, nivel, vida, fuerza)
elif tipo == 'mago':
    magia = int(input("Magia del mago: "))
    nuevo_personaje = Mago(nombre, nivel, vida, magia)
else:
    print("Tipo no valido")
    nuevo_personaje = None

if nuevo_personaje:
    print("\nPERSONAJE CREADO CON EXITO :3")
    nuevo_personaje.mostrar_informacion_personaje()