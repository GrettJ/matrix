from tabulate import tabulate


def catcher(entrada):
    """
    Se encarga de dividir el tipo de entrada para procesar en la funcion process_matrix
    """
    if entrada == []:
        return None
    if type(entrada[0]) == int or type(entrada[0]) == float:
        for x in entrada:
            if type(x) != float and type(x) != int:
                return False
            else:
                return "List"
    elif type(entrada[0]) == list:
        for x in entrada:
            for y in x:
                if type(y) != float and type(y) != int:
                    return False
                else:
                    return "Matrix"
    else:
        return False


def process_matrix(matriz):
    """
    Genera una matriz nueva con el numero promedio de la casilla y sus casillas vecinas
    para completa funcionalidad del programa es necesario instalar tabulate.
    Trabaja junto a la funcion catcher.
    """
    # Creamos una lista vacia donde guardamos los resultados
    Matrix = []
    # llamamos al filtro. si devuelve que es una lista sencilla lo procesa de ese modo
    if catcher(matriz) == "List":
        wide = len(matriz)
        for x, value in enumerate(matriz):
            left = x - 1
            right = x + 1
            sum = value
            cont = 1
            if left >= 0:
                sum += matriz[left]
                cont += 1
            if right < wide:
                sum += matriz[right]
                cont += 1
            Matrix.append(round((sum/cont),2))
    elif catcher(matriz) == "Matrix":
        # una vez confirmado que es una lista de listas definimos los limites
        wide = len(matriz)
        tall = len(matriz[0])
        for x, colum in enumerate(matriz):
            # Añado una lista vacia para generar una matriz del mismo tamaño que la original
            Matrix.append([])
            for y, val in enumerate(colum):
                # iniciamos el contador al valor del elemento
                sum = val
                cont = 1
                # en la variables guardamos la casilla que miramos
                up = y - 1
                down = y + 1
                left = x - 1
                right = x + 1
                # preguntamos 4 veces si cumple la condicion y filtrar casos extremos
                # dentro de cada if, si cumple la condicion sumamos el elemento de la casilla vecina y sumamos al contador
                if up >= 0:
                    sum += matriz[x][up]
                    cont += 1
                if down < tall:
                    sum += matriz[x][down]
                    cont += 1
                if left >= 0:
                    sum += matriz[left][y]
                    cont += 1
                if right < wide:
                    sum += matriz[right][y]
                    cont += 1
                # despues de pasar todas las preguntas añado a la lista vacia
                # en el mismo lugar del elemento inspeccionado
                Matrix[x].insert(y, sum/cont)
        # formateamos para ver el resultado como tabla
        Matrix = tabulate(Matrix, tablefmt="plain")
    elif catcher(matriz) == None:
        # confima que sea una lista vacia, pasa para que se devuelva la lista vacia creada
        pass
    elif catcher(matriz) == False:
        # devuelve un error, hay algun elemento en lo pasado que no es un numero
        raise ValueError("Only numerical matrices")
    return Matrix



print(catcher([1,2,3,4,5,6,7,8,9]))
