# Realizar un algoritmo que detecte si una persona tiene diferencias genéticas basándose en su secuencia de ADN.
# El algoritmo debe recibir como parámetro un arreglo de cadenas de caracteres que representan cada fila de una
# tabla de NxN con la secuencia del ADN y devolver un verdadero en caso que se encuentre una mutación o falso
# en caso de no tener mutación. Las letras de los caracteres solo pueden ser: A, T, C, G ; las cuales representan
# cada base nitrogenada del ADN.


# A T G C G A
# C A G T G C
# T T A T G T
# A G A A G G
# C C C C T A
# T C A C T G

# solo acepta A, T, C, G
# algoritmo recibe array de cadenas de caracteres
# String[] dna = [“ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG" ];
def algoritmo(arreglo):
    # volver cada string una lista
    lista_listas = crear_listas(arreglo)
    print(lista_listas)

# method para volver la lista de strings una lista de listas
def crear_listas(lista):
    nueva_lista = []
    for i in lista: 
        nueva_lista.append([i])
    return nueva_lista


# Sabrás sí existe una mutación si se encuentra más de una secuencia de cuatro letras iguales, de forma oblicua,
# horizontal o vertical.

if __name__ == '__main__':
    dna = ["ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG" ]
    algoritmo(dna)