def mutante(arreglo):
    validado = validacion(arreglo)
    if validado != False:
        num_coincidencias_horizontal = checar_horizontal(arreglo)
        num_coincidencias_vertical = checar_vertical(arreglo)
        num_coincidencias_diagonal = checar_diagonal(arreglo)
        num_coincidencias_total = num_coincidencias_horizontal + num_coincidencias_vertical + num_coincidencias_diagonal
        if num_coincidencias_total > 1:
            return True
        else:
            return False
    else:
        return False

# checar que solo contenga A, T, C, G los string
def validacion(lista):
    caracteres_validos = {'A', 'T', 'C', 'G'}
    for sublista in lista:
        for caracter in sublista:
            if caracter not in caracteres_validos:
                return False
    return True

# reciben una lista de string
# ['ATGCGA', 'CAGTGC', 'TTATGT', 'AGAAGG', 'CCCCTA', 'TCACTG']
def checar_horizontal(matriz):
    contador = 0
    for fila in matriz:
        # checar si se encuentra el patron AAAA TTTT CCCC GGGG
        if fila.find("TTTT") != -1 or fila.find("AAAA") != -1 or fila.find("CCCC") != -1 or fila.find("GGGG") != -1:
            contador +=1
        else:
            continue
    return contador

# Crear una lista de string con las verticales 
def checar_vertical(matriz):
    largo_fila = len(matriz)
    contador = 0
    columnas = []
    while contador < largo_fila:
        columna = ""
        for fila in matriz:
            for indice, valor in enumerate(fila):
                if(contador == indice):
                    columna+=valor 
        columnas.append(columna)
        contador+=1
    resultado = checar_horizontal(columnas)
    return resultado

def checar_diagonal(matriz):
    diagIz = diagonales_izq(matriz)
    diagDer = diagonales_der(matriz) 
    diagonales_totales = diagIz + diagDer
    return diagonales_totales

def diagonales_izq(matriz):
    num_diagonales_superiores = diagonales_superiores(matriz)
    num_diagonales_inferiores = diagonales_inferiores(matriz)
    diagonalies_izq_totales = num_diagonales_superiores + num_diagonales_inferiores
    return diagonalies_izq_totales

def diagonales_inferiores(matriz):
    diagonales = []
    filas = len(matriz)
    columnas = len(matriz[0])
    for i in range(1, filas):
        diagonal = ''
        j = 0  # Columna inicial
        k = i  # Fila inicial
        while j < columnas and k < filas:
            diagonal += matriz[k][j]
            j += 1
            k += 1
        diagonales.append(diagonal)
    return checar_horizontal(diagonales) #['AAAATG', 'ATACT', 'AGCA', 'ACA', 'CA', 'A']

def diagonales_superiores(matriz):
    diagonales = []
    filas = len(matriz)
    columnas = len(matriz[0])
    # Recorremos las diagonales verticales superiores
    for j in range(columnas):
        diagonal = ''
        i = 0  # Fila inicial
        k = j  # Columna inicial
        while i < filas and k < columnas:
            diagonal += matriz[i][k]
            i += 1
            k += 1
        diagonales.append(diagonal)
    return checar_horizontal(diagonales)#['AAAATG'],['TGAGA'],['GTGA'],['CAA'],['GA'],['A']

def diagonales_der(matriz):
    matriz_reversa = revertir_matriz(matriz)
    return diagonales_izq(matriz_reversa)

def revertir_matriz(matriz):
    reversa = []
    for fila in matriz:
        reversa.append(fila[::-1])
    return reversa



