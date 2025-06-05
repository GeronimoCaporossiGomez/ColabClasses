# Clase 1

# 1
print("Hola mundo, esto es un curso de Python y Machine Learning")

# 2
print("Línea 1\nLínea 2\nLínea 3")

# 3
print("A\tB\tC\nD\tE\tF\nG\tH\tI")

# 4
def es_par(n):
    return n % 2 == 0

def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# 5
nombre = input("¿Cuál es tu nombre? ")
print(f"Buen día {nombre} bienvenido a nuestro curso de Python")

# 6
num1 = int(input("Ingresa un número: "))
num2 = int(input("Ingresa otro número: "))
if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num2 > num1:
    print(f"{num2} es mayor que {num1}")
else:
    print(f"{num1} y {num2} son iguales")

# 7
nombre = input("Escribe tu nombre: ")
apellido = input("Escribe tu apellido: ")
print(f"{nombre} {apellido}")

# 8
def saludar():
    print("¡Hola mundo!")

saludar()

# 10
def bienvenida(nombre_persona):
    print(f"¡Bienvenido {nombre_persona}!")

nombre_persona = "Carlos"
bienvenida(nombre_persona)
