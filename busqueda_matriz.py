def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return i, j
    return None
matriz = [
    [1, 4, 5],
    [2, 4, 8],
    [9, 5, 7]
]
print("Matriz original:")
for fila in matriz:
    print(fila)
valor = 4
resultado = buscar_valor(matriz, valor)
if resultado:
    fila, columna = resultado
    print(f"El valor {valor} se encontró en la posición ({fila}, {columna})")
else:
    print(f"El valor {valor} no se encontró en la matriz")