Soma = 0
cont = 0
for c in range(1, 7):
    num = int((input("Digite o {} valor: ".format(c))))
    if num % 2 == 0:
        Soma += num
        cont += 1
print("Você informou {} números pares e a soma foi {}.".format(cont, Soma))

# exemplo 2

#Função
#=========================================================================================================================================
def separar_pares(lista):
    Lista_pares = list([])
    for i in range(len(lista)):
        if (lista[i]%2==0):
            Lista_pares.append(lista[i])
    return Lista_pares
#========================================================================================================================================
#testes
#========================================================================================================================================
Lista_teste = [2, 5, 6, 8 ,3, 6, 3, 4, 1]
Lista_pares = separar_pares(Lista_teste)
print(Lista_pares)