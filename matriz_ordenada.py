def bubble_sort_fila(matriz, fila):
    n = len(matriz[fila])
    for i in range(n):
        for j in range(0, n-i-1):
            if matriz[j] < matriz[j+1]:
                matriz[j], matriz[j+1] = matriz[j+1], matriz[j]
matriz = [
    [1, 4, 5],
    [2, 4, 8],
    [9, 5, 7]
]
print("Matriz real:")
for fila in matriz:
    print(fila)
fila_a_ordenar = 2
bubble_sort_fila(matriz, fila_a_ordenar)
print(f"\nMatriz con la fila {fila_a_ordenar} ordenada:")
for fila in matriz:
    print(fila)