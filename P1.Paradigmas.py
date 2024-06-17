import random
import time

def generar_arreglo(tamaño):
    arreglo = []
    for i in range(tamaño):
        numero = random.randint(1, 1000)
        arreglo.append(numero)
    return arreglo

def imprimir_arreglo(arreglo):
    texto = ", ".join(str(x) for x in arreglo)
    print(texto)

def buscar_secuencial(arreglo, elemento):
    for i, x in enumerate(arreglo):
        if x == elemento:
            return i
    return -1

def ordenar_arreglo(arreglo):
    arreglo.sort()
    return arreglo

arreglo = generar_arreglo(1000)
print("Arreglo original:")
imprimir_arreglo(arreglo)
print("-" * 50)

elemento = 500
indice = buscar_secuencial(arreglo, elemento)
if indice != -1:
    print(f"El elemento {elemento} se encontró en el índice {indice}")
else:
    print(f"El elemento {elemento} no se encontró en el arreglo")

print("-" * 50)

arreglo_ordenado = ordenar_arreglo(arreglo)
print("Arreglo ordenado:")
imprimir_arreglo(arreglo_ordenado)

indice = buscar_secuencial(arreglo_ordenado, elemento)
print("-" * 50)
if indice != -1:
    print(f"El elemento {elemento} se encontró en el índice {indice}")
else:
    print(f"El elemento {elemento} no se encontró en el arreglo")

print("-" * 50)

inicio = time.time()
arreglo = generar_arreglo(1000)
buscar_secuencial(arreglo, elemento)
arreglo_ordenado = ordenar_arreglo(arreglo)
buscar_secuencial(arreglo_ordenado, elemento)
fin = time.time()
duracion = fin - inicio
print(f"El tiempo de ejecución de los elementos 1 a 5 fue de {duracion} segundos")
