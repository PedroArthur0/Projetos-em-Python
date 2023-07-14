
'''def cubica(x):
    return x ** 3
'''


def trocaTrecho(trechoLista, palavraLista, numero):
    posicoes = []
    for i in range(len(trechoLista) - len(palavraLista) + 1):
        palavraEncontrada = True
        for j in range(len(palavraLista)):
            if palavraLista[j].lower() != trechoLista[i + j].lower():
                palavraEncontrada = False
                break
        if palavraEncontrada:
            posicoes.append(i)
    for indice in posicoes:
        for k in range(indice, indice + len(palavraLista)):
            trechoLista[k] = "@"
    trechoAlterado = "".join(trechoLista)
    trechoAlterado = trechoAlterado.replace("@" * len(palavraLista), numero)
    return trechoAlterado


