def process_matrix(matriz):
    wide = len(matriz)
    tall = len(matriz[0])
    matrix = []
    indice_y = 0
    indice_x = 0
    for x in matriz:
        matrix.append([])
        for y in x:
            
            suma = y
            cont = 1
            up = indice_y - 1
            down = indice_y + 1
            left = indice_x - 1
            right = indice_x + 1
            if up >= 0:
                suma += matrix[indice_x][up]
                cont += 1
            if down < tall:
                suma += matrix[indice_x][down]
                cont += 1
            if left >= 0:
                suma += matrix[left][indice_y]
                cont += 1
            if right < wide:
                suma += matrix[right][indice_y]
                cont += 1
            matrix[indice_x].insert(indice_y, round((suma/cont), 2))
            indice_y += 1
        indice_x += 1
    return matrix

print(process_matrix([[1,2,3,4], [1,2,2,3]]))