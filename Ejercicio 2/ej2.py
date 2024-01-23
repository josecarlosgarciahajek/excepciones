diccionario = {
    "Patata" : 3,
    "Limón" : 4,
    "Cebollas" : 3
}
try:
    clave = str(input("Dame una clave: "))
    valores = diccionario[clave]
    print(valores)
except KeyError:
    print("Clave no existente")



