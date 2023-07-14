"""
do while
codigo para adivinhar um número


"""
from random import randint #importando randit 
paplite = 0
numero = randint(1, 10) # randit gera números aleatórios 
while True: # execultamos sem verificar
    print("Qual o número correto?")
    paplite = int(input())
    if paplite == numero: # Verificando o código
        print("Parabéns você acertou!")
        break
    else:
        print("Você errou!")
else:
    print("Erro na aplicação")
    print(bool(paplite))