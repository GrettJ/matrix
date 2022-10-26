from statistics import mean

def process_list(elements):
    vacia = []
    if len(elements) == 1:
        vacia = elements
    else:
        for index, element in enumerate(elements):
            new_element = process_element(index, elements)
            vacia.append(new_element)
    return vacia


def process_element(index, elements):
    """
    Recibe un elemento de una lista y calcula su promedio con los vecinos, devuelve dicho promedio
    """
    indices = get_vecinos_index(index, elements)
    values = get_vecinos_values(indices, elements)

    return mean(values)

def get_vecinos_index(index, elements):
    indices = []
    indices.append(index + 1)
    indices.append(index - 1)
    indices.append(index)


    return indices

def get_vecinos_values(indices, elements):
    values = []
    for index in indices:
        values.append(elements[index])
    return values

#def get_average(values):
    """
    Recibe una lista de numeros y devuelve su promedio
    """
#    return reduce(lambda a,b: a+b, values) / len(values)

lista = [[1,2,1,2,3,2]]

print(process_list(lista))