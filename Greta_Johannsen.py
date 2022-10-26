from tabulate import tabulate

def process_matrix(matriz):
    """
    Genera una matriz nueva con el numero promedio de la casilla y sus casillas vecinas
    para completa funcionalidad del programa es necesario instalar tabulate.
    """
    # Definimos los limites de la matrz
    wide = len(matriz)
    tall = len(matriz[0])
    # creamos una matriz vacia donde guardamos los resultados
    Matrix = [] 
    for x, column in enumerate(matriz):
        # añadimos una lista vacia por cada columna
        Matrix.append([])
        for y, value in enumerate(column):
            # Iniciamos el contador con el valor del elemento
            suma = value
            # creamos un contador para saber cuantos elementos sumamos y por cuanto hay que dividir
            cont = 1
            # en las variables guardamos a que casilla miramos. 
            up = y - 1
            down = y + 1
            left = x - 1
            right = x + 1
            # creamos 4 if ya que tiene que preguntar 4 veces si cumple la condicion y filtrar casos extremos
            # dentro de cada if, si cumple la condicion sumamos el elemento de la casilla vecina y sumamos al contador
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
            # despues de pasar todas las preguntas añado a la lista vacia
            # en el mismo lugar del elemento inspeccionado
            # recortamos cantidad de decimales para que quede bonito
            Matrix[x].insert(y,round((suma/cont), 2))
    # formateamos lista de listas para ver como tabla.
    return tabulate(Matrix, tablefmt = "plain")

def process_list_of_lists(matriz):
    """
    Igual que process_matrix, pero devuelve lista de listas
    """
    wide = len(matriz)
    tall = len(matriz[0])
    Matrix = [] 
    for x, column in enumerate(matriz):
        Matrix.append([])
        for y, value in enumerate(column):
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
            Matrix[x].insert(y,round((suma/cont), 2))

    return Matrix