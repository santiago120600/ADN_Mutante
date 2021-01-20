import re
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
        # depues sumar 
        num_coincidencias_total = num_coincidencias_horizontal + num_coincidencias_vertical + num_coincidencias_diagonal
        print("numero horizontal: ",num_coincidencias_horizontal," numero vertical:",num_coincidencias_vertical,"numero coincidencias diagonal:",num_coincidencias_diagonal)
        # si el numero de coincidencias es mayor a 1 entonces es mutante
        if num_coincidencias_total > 1:
            return True
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
    # contador para contar el numero de apariciones de string
    contador = 0
    for fila in matriz:
        # convertir lista a string
        fila_string = convertir_a_string(fila)
        # checar si se encuentra el patron AAAA TTTT CCCC GGGG
        if fila_string.find("TTTT") != -1 or fila_string.find("AAAA") != -1 or fila_string.find("CCCC") != -1 or fila_string.find("GGGG") != -1:
            contador +=1
        else:
            continue
    return contador

# Crear una lista una lista de listas con las listas verticales y despues pasarla a checar_horizontal
def checar_vertical(matriz):
    largo_fila = len(matriz[0][0])
    sublista = []
    contador = 0
    # hacer una sublista a partir de la matriz que contenga los caracteres de forma vertical
    while contador < largo_fila:
        for fila in matriz:
            sublista.append(fila[0][contador]) 
        contador+=1
    # convertir lista a string
    caracteres_horz = ["".join(sublista)]
    # lista final 
    lista_horizontal = re.findall('.'*largo_fila,caracteres_horz[0])
    return checar_horizontal(lista_horizontal)

def checar_diagonal(matriz):
    diagIz = diagonales_izq(matriz)
    diagDer = diagonales_der(matriz) 
    # sumar diagIz y diagDer
    diagonales_totales = diagIz + diagDer
    return diagonales_totales

def diagonales_izq(matriz):
    diagonales_izq_final = []
    # que el for loop se reinicie pero empezando en la siguiente lista no en la primera
    while len(matriz) > 0:
        diagonales = []
        contador = 0
        for fila in matriz:
            diagonales.append(fila[0][contador])
            contador+=1
        # convertir a string la lista y meter a otra lista 
        sublista = convertir_a_string(diagonales)
        diagonales_izq_final.append(sublista)
        matriz = matriz[1:]
    # checar si la sublista contiene las coincidencias
    return checar_horizontal(diagonales_izq_final)

def diagonales_der(matriz):
    # reverse matrix y usar el diagonales izq
    matriz_reversa = revertir_matriz(matriz)
    # retornar el numero de numero de coincidencias
    return diagonales_izq(matriz_reversa)

def revertir_matriz(matriz):
    # retornar una matriz reversa
    reversa = []
    for fila in matriz:
        reversa.append([fila[0][::-1]])
    return reversa

# [
#     ['A T G C G A'], 
#     ['C A G T G C'], 
#     ['T T A T G T'], 
#     ['A G A A G G'], 
#     ['C C C C T A'], 
#     ['T C A C T G']
#     ]
# [
#     ['A G C G T A'], 
#     ['C G T G A C'], 
#     ['T G T A T T'], 
#     ['G G A A G A'], 
#     ['A T C C C C'], 
#     ['G T C A C T']
# ]

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
    # print(checar_vertical(dna_mutante))
    # print(checar_diagonal([['ATGCGA'], ['CAGTGC'], ['TTATGT'], ['AGAAGG'], ['CCCCTA'], ['TCACTG']]))
    print(diagonales_izq([
        ['ATGCGA'], 
        ['CAGTGC'], 
        ['TCATGT'], 
        ['AGCAGG'], 
        ['CCCCTA'], 
        ['TCACTG']
        ]))
    # print(revertir_matriz([['ATGCGA'], ['CAGTGC'], ['TTATGT'], ['AGAAGG'], ['CCCCTA'], ['TCACTG']]))


