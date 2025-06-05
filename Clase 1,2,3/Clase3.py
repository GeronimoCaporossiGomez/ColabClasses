# Clase 3

# Clases
class Personaje:
    pass

harry_potter = Personaje()

class Dinosaurio:
    pass

velociraptor = Dinosaurio()
tiranosaurio_rex = Dinosaurio()
braquiosaurio = Dinosaurio()

class PlataformaStreaming:
    pass

netflix = PlataformaStreaming()
hbo_max = PlataformaStreaming()
amazon_prime_video = PlataformaStreaming()

# Atributos
class Casa:
    def __init__(self, color, cantidad_pisos):
        self.color = color
        self.cantidad_pisos = cantidad_pisos

casa_blanca = Casa("blanco", 4)

class Cubo:
    caras = 6
    def __init__(self, color):
        self.color = color

cubo_rojo = Cubo("rojo")

class Personaje2:
    real = False
    def __init__(self, especie, magico, edad):
        self.especie = especie
        self.magico = magico
        self.edad = edad

harry_potter2 = Personaje2("Humano", True, 17)

# Métodos
class Perro:
    def ladrar(self):
        print("Guau!")

class Mago:
    def lanzar_hechizo(self):
        print("¡Abracadabra!")

Merlin = Mago()
Merlin.lanzar_hechizo()

class Alarma:
    def postergar(self, cantidad_minutos):
        print(f"La alarma ha sido pospuesta {cantidad_minutos} minutos")

# Tipos de métodos
class Mascota:
    @staticmethod
    def respirar():
        print("Inhalar... Exhalar")

class Jugador:
    vivo = False
    @classmethod
    def revivir(cls):
        cls.vivo = True

class Personaje3:
    def __init__(self, cantidad_flechas):
        self.cantidad_flechas = cantidad_flechas
    def lanzar_flecha(self):
        self.cantidad_flechas -= 1

# Herencia
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Alumno(Persona):
    pass

class MascotaBase:
    def __init__(self, edad, nombre, cantidad_patas):
        self.edad = edad
        self.nombre = nombre
        self.cantidad_patas = cantidad_patas

class Perro2(MascotaBase):
    pass

class Vehiculo:
    def acelerar(self): pass
    def frenar(self): pass

class Automovil(Vehiculo):
    pass

# Herencia Múltiple
class Padre:
    def trabajar(self):
        print("Trabajando en el Hospital")
    def reir(self):
        print("Ja ja ja!")

class Madre:
    def trabajar(self):
        print("Trabajando en la Fiscalía")

class Hija(Padre, Madre):
    def trabajar(self):
        Madre.trabajar(self)

# Ornitorrinco
class Vertebrado:
    vertebrado = True

class Pez:
    def nadar(self): print("Nadando")

class Reptil:
    venenoso = True

class Ave:
    def poner_huevos(self): print("Poniendo huevos")

class Mamifero:
    def amamantar(self): print("Amamantando")

class Ornitorrinco(Vertebrado, Pez, Reptil, Ave, Mamifero):
    tiene_pico = True
    def caminar(self): print("Caminando")

# Sobreescritura método
class Padre2:
    def hobby(self):
        return "Leer libros"

class Hijo(Padre2):
    def hobby(self):
        return "Juego videojuegos en mi tiempo libre"
