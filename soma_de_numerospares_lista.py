# Exemplo 1
lista = [10, 2, 5, 7, 6, 3]
n = len(lista) # Len identifica a quantidade de elementos que começa do 0 e vai até 5 contidos na lista
soma = 0 # Crio um parâmetro para calcular os pares
for i in range(n): # Verifico se está no range de n e os pares e ímpares
    if lista[i]%2== 0: # Divido por 2 e caso seja igual a zero será par
        soma = soma + lista[i] # Somo os pares
print(f"O somatório dos elementos na lista foi: {soma}") # Formato para str e imprimo a somatória dos pares

# Exemplo 2
lista = [10, 2, 5, 7, 6, 3]
soma = 0 # Crio um parâmetro para calcular os pares
for num in range(n): # Verifico apenas os números na lista e sendo assim prog.funcional 
    if lista[num]%2== 0:  # Realizo o mesmo teste 
        soma = soma + lista[num] # Somo os pares
print(f"O somatório dos elementos na lista foi: {soma}") # Formato para str e imprimo a somatória dos pares
 