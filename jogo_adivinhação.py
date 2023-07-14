import random

def palpite_numero():
    numero = random.randint(1, 100)
    tentativas = 0

    print("Bem-vindo ao Jogo de Adivinhação!")
    print("Tente adivinhar o número entre 1 e 100.")

    while True:
        palpite = int(input("Digite o seu palpite: "))
        attempts += 1

        if palpite < numero:
            print("Palpite muito baixo. Tente novamente!")
        elif palpite > numero:
            print("Palpite muito alto. Tente novamente!")
        else:
            print(f"Parabéns! Você acertou o número em {tentativas} tentativas.")
            break

palpite_numero()
