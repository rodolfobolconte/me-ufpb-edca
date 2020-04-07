def selection_sort(lista):
    CONTADOR = 0

    for i in range(len(lista)):
        CONTADOR += 1
        min = i
        
        for j in range(i+1, len(lista)):
            CONTADOR += 1
            if lista[j] < lista[min]:
                min = j

        if lista[i] != lista[min]:
            aux = lista[i]
            lista[i] = lista[min]
            lista[min] = aux

    print('\nCONTADOR SELECTION_SORT:', CONTADOR)
    print(lista)


def insertion_sort(lista):
    CONTADOR = 0

    for i in range(len(lista)):
        CONTADOR += 1

        numAtual = lista[i]
        j = i - 1
        while j >=0 and lista[j] > numAtual:
            CONTADOR += 1
            lista[j+1] = lista[j]
            j -= 1

        lista[j+1] = numAtual

    print('\nCONTADOR INSERTION_SORT:', CONTADOR)
    print(lista)    

lista = [10,9,8,7,6,5,4,3,2,1]

selection_sort(lista)
insertion_sort(lista)