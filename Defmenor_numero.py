def encontrar_minimo(lista):
    minimo = lista [0]
    for elem in lista:
        if (elem < minimo):
            minimo = elem
            return minimo

lista_teste = [2, 15, 1, 10, 27]
menor = encontrar_minimo(lista_teste)
print("O menor elemento da lista é: [{}]".format(menor))
# Função que retorna o maior valor:
