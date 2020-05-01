def countSort(A, B, k):
    C = [0] * k
    for j in range(1, len(A)):
        C[A[j]] = C[A[j]] + 1
    #
    for i in range(2, k):
        C[i] = C[i] + C[i-1]
    #
    for j in range(len(A)-1, 0, -1):
        B[C[A[j]]] = A[j]
        C[A[j]] = C[A[j]] - 1

    return B

def countSortSimplificado(lista):
    tamanho = len(lista)

    listaOrdenada = [ 0 for x in range(tamanho)]

    for i in range(tamanho):
        contador = tamanho - 1
        for j in range(tamanho):
            if lista[i] < lista[j]:
                contador -= 1
        listaOrdenada[contador] = lista[i]

    return listaOrdenada

def radixSort(lista):
    mod = 10
    while lista[0] / mod >= 0.1:
        for i in range(1, len(lista)):
            numAtual = lista[i]
            j = i - 1

            while j >=0 and lista[j] % mod > numAtual % mod:
                lista[j+1] = lista[j]
                j -= 1

            lista[j+1] = numAtual

        mod *= 10
    
    return lista


A = [10,9,8,7,6,5,4,3,2,1]
B = [10,9,8,7,6,5,4,3,2,1]
radixLista = [329,457,657,839,436,720,355]

#print(countSort(A, B, max(A)))
print(radixSort(radixLista))