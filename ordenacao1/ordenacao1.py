import time

#implementacao do selection sort
def selection_sort(lista):
    #variavel da funcao de complexidade (T(n))
    T_N = 0

    #variavel de execucao inicial
    horaInicio = time.time()

    #execucao do selection sort
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
    
    #variavel de execucao final
    horaFim = time.time()

    #visualizacao da funcao de complexidade e tempo de execucao
    print('\nSELECTION_SORT - T(n):', T_N)
    print('SELECTION_SORT - Tempo de Execução: %.4f' %(horaFim - horaInicio))

#implementacao do selection sort
def insertion_sort(lista):
    #variavel da funcao de complexidade (T(n))
    T_N = 0

    #variavel de execucao inicial
    horaInicio = time.time()

    #execucao do insertion sort
    for i in range(len(lista)):
        T_N += 1

        numAtual = lista[i]
        j = i - 1
        while j >=0 and lista[j] > numAtual:
            T_N += 1
            lista[j+1] = lista[j]
            j -= 1

        lista[j+1] = numAtual

    #variavel de execucao final
    horaFim = time.time()

    #visualizacao da funcao de complexidade e tempo de execucao
    print('\nINSERTION_SORT - T(n):', T_N)
    print('INSERTION_SORT - Tempo de Execução: %.4f' %(horaFim - horaInicio))

while True:
    #dicionario com o nome de cada arquivo sem extensao
    nomeArquivo = {1:'1000-1', 2:'1000-2', 3:'1000-3', 4:'1000-4', 5:'10000-1', 6:'10000-2', 7:'10000-3', 8:'10000-4', 9:'100000-1', 10:'100000-2', 11:'100000-3', 12:'100000-4'}

    #menu de opcoes dos arquivos
    print('\nEscolher Opção:')
    for opcao in range(1,13):
        print('    {}- {}'.format(opcao, nomeArquivo[opcao]))
    opcao = int(input('Opção: '))
    while opcao < 0 or opcao > 12:
        opcao = int(input('Opção: '))

    #encerra o script
    if not opcao: break
    
    #carrega o arquivo escolhido
    arquivo = open('A:/OneDrive/Email Acadêmico/UFPB - Mestrado Informática/Estrutura de Dados e Complexidade de Algoritmos/Atividades/me-ufpb-edca/ordenacao1/instancias-num/' + nomeArquivo[opcao] + '.in')

    #coloca os valores do arquivo em um array
    lista = [int(numero) for numero in arquivo.readlines()]

    #execucao dos algoritmos de ordenacao
    selection_sort(lista)
    insertion_sort(lista)