lista = [6, 14, 11, 3, 2, 1, 15, 19]

try:
    numero = int(input('Introduce una posición: '))
    lista[numero]
except ValueError:
    print("Dato erroneo")
except IndexError:
    print("Posición no encontrada")
