import time

def selection_sort(lista):
    T_N = 0

    horaInicio = time.time()

    for i in range(len(lista)):
        T_N += 1
        min = i
        
        for j in range(i+1, len(lista)):
            T_N += 1
            if lista[j] < lista[min]:
                min = j

        if lista[i] != lista[min]:
            aux = lista[i]
            lista[i] = lista[min]
            lista[min] = aux
    
    horaFim = time.time()

    print('\nSELECTION_SORT - T(n):', T_N)
    print('SELECTION_SORT - Tempo de Execução: %.4f' %(horaFim - horaInicio))

def insertion_sort(lista):
    T_N = 0

    horaInicio = time.time()

    for i in range(len(lista)):
        T_N += 1

        numAtual = lista[i]
        j = i - 1
        while j >=0 and lista[j] > numAtual:
            T_N += 1
            lista[j+1] = lista[j]
            j -= 1

        lista[j+1] = numAtual

    horaFim = time.time()

    print('\nINSERTION_SORT - T(n):', T_N)
    print('INSERTION_SORT - Tempo de Execução: %.4f' %(horaFim - horaInicio))

while True:
    nomeArquivo = {1:'1000-1', 2:'1000-2', 3:'1000-3', 4:'1000-4', 5:'10000-1', 6:'10000-2', 7:'10000-3', 8:'10000-4', 9:'100000-1', 10:'100000-2', 11:'100000-3', 12:'100000-4'}

    print('\nEscolher Opção:')
    for opcao in range(1,13):
        print('    {}- {}'.format(opcao, nomeArquivo[opcao]))
    opcao = int(input('Opção: '))

    if not opcao: break
    
    arquivo = open('A:/OneDrive/Email Acadêmico/UFPB - Mestrado Informática/Estrutura de Dados e Complexidade de Algoritmos/Atividades/me-ufpb-edca/ordenacao1/instancias-num/' + nomeArquivo[opcao] + '.in')

    lista = [int(numero) for numero in arquivo.readlines()]

    selection_sort(lista)
    insertion_sort(lista)