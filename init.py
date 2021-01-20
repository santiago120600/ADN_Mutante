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
    # checar que solo contenga A, T, C, G los string
    validado = validacion(arreglo)
    if validado != False:
        # volver cada string una lista
        matriz = crear_listas(arreglo)
        #metodo para checar las hotizontales
        num_coincidencias_horizontal = checar_horizontal(matriz)
        #metodo para checar las verticales
        num_coincidencias_vertical = checar_vertical(matriz)
        #metodo para checar las diagonales
        num_coincidencias_diagonal = checar_diagonal(matriz)
        print(matriz)
    else:
        return False

# method para volver la lista de strings una lista de listas
def crear_listas(lista):
    nueva_lista = []
    for i in lista: 
        nueva_lista.append([i])
    return nueva_lista

def validacion(lista):
    for sublista in lista:
        for caracter in sublista:
            if caracter == 'A' or caracter == 'T'  or caracter == 'C'  or caracter == 'G':
                continue
            else: 
                return False

# reciben una lista de listas(matriz)
# [['ATGCGA'], ['CAGTGC'], ['TTATGT'], ['AGAAGG'], ['CCCCTA'], ['TCACTG']]
# que estas funciones retornen el numero de secuencias de cuatro letras iguales
# para despues sumar el numero de coincidencias y si son mas de una entonces retornar falso
def checar_horizontal(matriz):
    for fila in matriz:
        # convertir lista a string
        fila_string = convertir_a_string(fila)
        # checar si se encuentra el patron AAAA TTTT CCCC GGGG
        # if "AAAA" or "TTTT" or "CCCC" or "GGGG" in fila_string:
        #     print(fila_string)
        # else:
        #     print("False")
        print(fila_string)
        
def checar_vertical(matriz):
    pass

def checar_diagonal(matriz):
    pass

def convertir_a_string(lista):
    string = ""
    for i in lista:
        string += i
    return string


# Sabrás sí existe una mutación si se encuentra más de una secuencia de cuatro letras iguales, de forma oblicua,
# horizontal o vertical.

if __name__ == '__main__':
    dna_mutante = [ 
        "ATGCGA", 
        "CAGTGC",
        "TTATGT",
        "AGAAGG",
        "CCCCTA",
        "TCACTG" 
            ]
    dna_sin = [
        "ATGCGA", 
        "CAGTGC",
        "TTATTT",
        "AGACGG",
        "GCGTCA",
        "TCACTG" 
    ]
    # dna = ["ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTW" ]
    # algoritmo(dna_mutante)
    checar_horizontal([['TTTTGA'], ['CAGTGC'], ['TTATGT'], ['AGAAGG'], ['CCCCTA'], ['TCACTG']])
