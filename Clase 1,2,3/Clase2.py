# Clase 2

# 1
mi_lista = [1, "hola", True, 3.14, None]

# 2
medios_transporte = ["avión", "auto", "barco", "bicicleta"]
medios_transporte.append("motocicleta")

# 3
frutas = ["manzana", "banana", "mango", "cereza", "sandía"]
eliminado = frutas.pop(2)

# 4
mi_lista = list(range(2500, 2586))

# 5
mi_dic = {
    "nombre": "",
    "apellido": "",
    "edad": 0,
    "ocupacion": ""
}
mi_dic.update({
    "nombre": "Karen",
    "apellido": "Jurgens",
    "edad": 36,
    "ocupacion": "Editora",
    "pais": "Colombia"
})

# 6
def todos_positivos(lista):
    return all(x > 0 for x in lista)

lista_numeros = [5, 2, -7]
print(todos_positivos(lista_numeros))

# 7
def suma_menores(lista):
    return sum(x for x in lista if 0 < x < 1000)

lista_numeros = [10, 999, 1000, -5]
print(suma_menores(lista_numeros))
