import time

def max_heapify(lista, i, tam):

    global T_N_HEAP_SORT

    T_N_HEAP_SORT+=1
    maior = i

    T_N_HEAP_SORT+=1
    l = (2*i)+1 ; r = (2*i)+2

    T_N_HEAP_SORT+=1
    if l < tam and lista[l] > lista[i]: maior = l
    T_N_HEAP_SORT+=1
    if r < tam and lista[r] > lista[maior]: maior = r

    T_N_HEAP_SORT+=1
    if maior != i:
        T_N_HEAP_SORT+=1
        lista[i], lista[maior] = lista[maior], lista[i]
        max_heapify(lista, maior, tam)

    return lista


def build_max_heap(lista, tam):

    global T_N_HEAP_SORT

    for i in range(int((tam/2)-1), -1, -1):
        T_N_HEAP_SORT+=1
        heap_maximo = max_heapify(lista, i, tam)
    
    return heap_maximo

def heap_sort(lista):

    global T_N_HEAP_SORT

    tam = len(lista)

    T_N_HEAP_SORT+=1
    lista = build_max_heap(lista, tam)

    for i in range(tam-1, 0, -1):
        T_N_HEAP_SORT+=1
        lista[0], lista[i] = lista[i], lista[0]
        lista = max_heapify(lista, 0, i)

    return lista

while True:
    listas = [  [27, 17, 3, 16, 13, 10, 15, 7, 12, 4, 8, 9, 0],
                [5, 4, 3, 2, 1],
                [4, 1, 3, 2, 16, 9, 10, 14, 8, 7],
                [5, 10, 8, 2, 6, 3, 1, 7, 9, 4]]

    print('\nEscolher Opção:')
    print('    -1 - Sair')
    for opcao in range(len(listas)):
        print('    {} - {}'.format(opcao, listas[opcao]))
    
    opcao = int(input('Digite a Opção: '))

    if opcao > len(listas) - 1 or opcao < 0:
        break

    T_N_HEAP_SORT = 0

    tempo_inicial = time.time()
    print('\nArray Ordenado:', heap_sort(listas[opcao]))
    tempo_final = time.time()
    print('Função T_N:', T_N_HEAP_SORT)
    print('Tempo de Execução (s): %.4f' %(tempo_final - tempo_inicial))