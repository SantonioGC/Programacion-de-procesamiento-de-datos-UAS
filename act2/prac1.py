class Usuario:
    def __init__(self,nombre,amigos,publicaciones):
        self.nombre = nombre
        self.lista_amigos = amigos
        self.lista_publicaciones = publicaciones

    def mostrar_perfil(self):
        print(f"Nombre: {self.nombre}")
        print(f"Amigos ({len(self.lista_amigos)}): {', '.join(self.lista_amigos)}")
        print(f"Publicaciones recientes: ")
        for i, pub in enumerate(self.lista_publicaciones, 1):
            print(f"{i}. {pub}")

print("--Bienvenido al sistema de registro--")
nombre_input = input("Ingrese su nombre de usuario: ")

amigos_input = []
for i in range(3):
    amigo = input("Ingrese el nombre de su amigo ")
    amigos_input.append(amigo)

publicaciones_input = []
for i in range(3):
    pub = input(f"Titulo de su publicacion {i+1}: ")
    publicaciones_input.append(pub)

nuevo_usuario = Usuario(nombre_input, amigos_input, publicaciones_input)
nuevo_usuario.mostrar_perfil()