def countSort(lista):
    A = lista ; k = max(A)
    C = [0] * k ; B = [0] * k

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

    listaOrdenada = [0] * tamanho

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

lista = [10,9,8,7,6,5,4,3,2,1]

print(countSort(lista))
print(countSortSimplificado(lista))
exit()


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
    countSort(lista)
    radixSort(lista)