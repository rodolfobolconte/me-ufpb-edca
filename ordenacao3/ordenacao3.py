import time

def countSort(lista):
    #Com defeito, não ordena o primeiro número da lista.
    #Ex.: Entrada = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    #     Saída   = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    T_N = 0

    A = lista ; k = max(A)
    C = [0] * k ; B = [0] * k

    tempo_inicial = time.time()

    for j in range(1, len(A)):
        T_N += 1
        C[A[j]] = C[A[j]] + 1
    
    for i in range(2, k):
        T_N += 1
        C[i] = C[i] + C[i-1]
    
    for j in range(len(A)-1, 0, -1):
        T_N += 1
        B[C[A[j]]] = A[j]
        C[A[j]] = C[A[j]] - 1

    tempo_final = time.time()
    print(B)
    print('\nCOUNT_SORT - T(n):', T_N)
    print('COUNT_SORT - Tempo de Execução: %.5f' %(tempo_final - tempo_inicial))

    #return B

def countSortSimplificado(lista):
    T_N = 0
    
    tamanho = len(lista)

    listaOrdenada = [0] * tamanho

    tempo_inicial = time.time()
    
    for i in range(tamanho):
        T_N += 1
        contador = tamanho - 1
        for j in range(tamanho):
            T_N += 1
            if lista[i] < lista[j]:
                T_N += 1
                contador -= 1
        listaOrdenada[contador] = lista[i]

    tempo_final = time.time()

    print('\nCOUNT_SORT_SIMPLIFICADO - T(n):', T_N)
    print('COUNT_SORT_SIMPLIFICADO - Tempo de Execução: %.5f' %(tempo_final - tempo_inicial))

    #return listaOrdenada

def radixSort(lista):
    T_N = 0
    
    mod = 10
    #enquanto o resto da divisão não for menor que 0.1
    #multiplica o mod por 10 no final para passar para a próxima casa decimal
    tempo_inicial = time.time()
    while lista[0] / mod >= 0.1:
        T_N += 1
        #utilizando o insertion sort para ordenar os valores
        for i in range(1, len(lista)):
            T_N += 1
            numAtual = lista[i]
            j = i - 1

            while j >=0 and lista[j] % mod > numAtual % mod:
                T_N += 1
                lista[j+1] = lista[j]
                j -= 1

            lista[j+1] = numAtual

        mod *= 10
    
    tempo_final = time.time()
    
    print('\nRADIX_SORT - T(n):', T_N)
    print('RADIX_SORT - Tempo de Execução: %.5f' %(tempo_final - tempo_inicial))


while True:
    #dicionario com o nome de cada arquivo sem extensao
    nomeArquivo = {1:'3digitos-1', 2:'3digitos-2', 3:'4digitos-1', 4:'4digitos-2', 5:'5digitos-1', 6:'5digitos-2'}

    #menu de opcoes dos arquivos
    print('\nEscolher Opção:')
    for opcao in range(1,len(nomeArquivo)+1):
        print('    {}- {}'.format(opcao, nomeArquivo[opcao]))
    opcao = int(input('Opção: '))
    while opcao < 0 or opcao > 12:
        opcao = int(input('Opção: '))

    #encerra o script
    if not opcao: break

    #carrega o arquivo escolhido
    arquivo = open('instancias-num/' + nomeArquivo[opcao] + '.in')

    #coloca os valores do arquivo em um array
    lista = [int(numero) for numero in arquivo.readlines()]

    #execucao dos algoritmos de ordenacao
    #counSort() ta com problema quando usa as instancias
    #countSort(lista)
    countSortSimplificado(lista)
    radixSort(lista)