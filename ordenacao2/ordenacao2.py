import time

def mergeSort(lista):
    
    tamanho = len(lista)

    #retorna a lista se ela tiver tamanho 1
    if tamanho == 1: return lista

    meio = tamanho // 2

    #retorna a lista para a função merge após fazer a divisão ser feita até ter tamanho 1
    return merge(mergeSort(lista[:meio]), mergeSort(lista[meio:]))

def merge(listaEsquerda, listaDireita):

    #lista auxiliar
    lista = list()

    #enquanto uma das listas tiverem objetos
    while listaEsquerda or listaDireita:
        #se ambas as listas tiverem objetos
        if listaEsquerda and listaDireita:
            #se valor de lista esquerda é menor que valor da lista direita
            if listaEsquerda[0] < listaDireita[0]:
                #coloca na lista auxiliar
                lista.append(listaEsquerda.pop(0))
            else:
                lista.append(listaDireita.pop(0))

        elif not listaEsquerda:
            if listaDireita: lista.append(listaDireita.pop(0))
        
        elif not listaDireita:
            if listaEsquerda: lista.append(listaEsquerda.pop(0))

    return lista

  
def quickSort(lista, inicio, fim):
    
    if inicio < fim:

        meio = particao(lista, inicio, fim)

        #divide a parte esquerda
        quickSort(lista, inicio, meio - 1)
        #divide a parte direita
        quickSort(lista, meio + 1, fim)

    return lista

def particao(lista, inicio, fim): 
    i = inicio - 1
    pivo = lista[fim]

    for j in range(inicio, fim):
  
        if lista[j] <= pivo:
            i += 1
            #função swap
            lista[i], lista[j] = lista[j], lista[i]

    #função swap
    lista[i+1], lista[fim] = lista[fim], lista[i+1]

    return i + 1


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
    arquivo = open('instancias-num/' + nomeArquivo[opcao] + '.in')

    #coloca os valores do arquivo em um array
    lista = [int(numero) for numero in arquivo.readlines()]

    
    #calculo e execucao dos algoritmos
    iniExecMergeSort = time.time()
    mergeSort(lista)
    fimExecMergeSort = time.time()
    print('\nMERGE_SORT - Tempo de Execução: %.4f' %(fimExecMergeSort - iniExecMergeSort))

    iniExecQuickSort = time.time()
    quickSort(lista, 0, len(lista)-1)
    fimExecQuickSort = time.time()
    print('\nQUICK_SORT - Tempo de Execução: %.4f' %(fimExecQuickSort - iniExecQuickSort))