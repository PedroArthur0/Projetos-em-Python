# Exemplo 1
def fatorial_interativo(n):
    f = 1
    for i in range(1, n+1):
        f =f*i
        return f
 # Exemplo 2
def fatorial_recursivo(n):
    if ((n == 0)) or ((n ==1)):
        return 1
    return n*fatorial_recursivo(n -1)
numero = int(input())
print(f"O fatorial de {numero} é: {fatorial_interativo(numero)}")
print(f"O fatorial de {numero} é: {fatorial_recursivo(numero)}")