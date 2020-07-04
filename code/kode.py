M = [
    [1, 0, 1],
    [0, 1, 0],
    [0, 0, 1]
]


def contains1(v) {
    """ Devuelve 1 si el vector v contiene algun 1; devuelve 0 en otro caso """
    for i in range(len(v))
        if v[i] == 1
            return 1
    return 0
}

# Define un vector que tiene un 1 en la posicion i si y solo si
# la matriz M tiene algun 1 en su fila i
filaIDeMTieneUn1 = []
for i in range(len(M))
    filaIDeMTieneUn1[i] = contains1(M[i]) 

for a in range(len(M))
    if (contains1(M[a]))


