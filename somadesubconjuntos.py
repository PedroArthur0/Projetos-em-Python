def verificaMenor(lista):
    lista = sorted(lista)
    listaFinal = [0]
    menorValor = 0

    for i in range(len(lista)):

        for l in range(len(listaFinal)):
            listaFinal.append(lista[i]+listaFinal[l])
            listaFinal = list(set(listaFinal))

            while menorValor in listaFinal:
                menorValor += 1
    return menorValor


t = int(input())
for i in range(t):
    n = int(input())
    listaEntrada = list(map(int, input().split()))
    menorValor = verificaMenor(listaEntrada)
    print(menorValor)