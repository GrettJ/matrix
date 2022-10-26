def process_matrix(lista):
    pass

def filter_limits(elemento):
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