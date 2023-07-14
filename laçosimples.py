while True: # Para se iniciar um laço precisa-se de uma condição verdadeira
    print('Você está no primeiro laço.')
    opcao1 = input('Deseja sair dele? Digite SIM para isso. \n')
    if opcao1 == 'SIM':
        break  # este break é do primeiro laço
    else:
        while True:
            print('Você está no segundo laço.')
            opcao2 = input('Deseja sair dele? Digite SIM para isso. \n')
            if opcao2 == 'SIM':
                break  # este break é do segundo laço
        print('Você saiu do segundo laço.')
print('Você saiu do primeiro laço')
# Exemplo 2 com continue:
for num in range(1, 11):
    if num == 5:
        continue
    else:
        print(num)
print('Laço encerrado')
# Laço 3 com pass:
for num in range(1, 11): # Verifico se está no alcance
    if num % 2 == 0: # Faço uma divisão e se a condição estiver dentro da condição passo
        pass
    else:            # Caso não tenha sido atendido a condição anterior irá me imprimir o resultado
        print(num)
print('Laço encerrado')