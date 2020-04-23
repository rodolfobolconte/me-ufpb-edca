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

def quicksort():
    pass


lista = [numero for numero in range(10,0,-1)]

print(mergeSort(lista))