x = [[1,2,3,4], [1,2,0,0], [0,0,0,1], [1,2,3,4]]
tmp = []
ancho = len(x)
alto = len(x[0])

def funcion(matriz):
    for x, colum in enumerate(matriz):
        for y, val in enumerate(col):
            media = 
            up = index - 1
            down = index + 1
            left = lista[index-1] - 1
            right = lista[index-1] + 1
            if up >= 0:
                tmp.append(matriz[index][up])
            if down >= 0:
                tmp.append(matriz[down][index])
            if left < ancho:
                tmp.append(matriz[left][index])
            if right < alto:
                tmp.append(matriz[right][index])
            else:
                tmp.append(i)     
    return print(tmp)

funcion(x)

