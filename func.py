def process_matrix(matriz):
    wide = len(matriz)
    tall = len(matriz[0])
    matrix = []
    for x, column in enumerate(matriz):
        matrix.append([])
        for y, value in enumerate(column):
            result = filter_limits(y, x, wide, tall, value, matriz)
            matrix[x].insert(y,result)
    return matrix

def filter_limits(y, x, wide, tall, value, matriz):
    suma = value
    cont = 1
    up = y - 1
    down = y + 1
    left = x - 1
    right = x + 1
    if up >= 0:
        suma += matriz[x][up]
        cont += 1
    if down < tall:
        suma += matriz[x][down]
        cont += 1
    if left >= 0:
        suma += matriz[left][y]
        cont += 1
    if right < wide:
        suma += matriz[right][y]
        cont += 1
    return (suma/cont)
