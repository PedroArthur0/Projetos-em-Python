'''import numpy as np


def entrada_dados():
    coeficiente = quantidade = eval(input("Digite um valor do coeficiente: "))
    return coeficiente


def calc_delta(a, b, c):
    delta = b * b - 4 * c
    return delta


def calcular_raizes(a, b, c, delta):
    if delta < 0:
        resultado = "A equação não possui  raízes nos números reais."
    elif (delta == 0):
        x = -b / (2 * a)
        resultado = 'A equação possui raíz de número: {x}'
    else:
        x1 = (-b - np.sqrt(delta))/(2 * a)
        x2 = (-b - np.sqrt(delta))/(2 * a)
        resultado = f"A equação possui as raízes: {x1}, {x2}"
        return resultado'''


'''import random

def jogar():
    print("Bem-vindo ao jogo Pedra, Papel, Tesoura!")
    print("Escolha uma opção:")
    print("1 - Pedra")
    print("2 - Papel")
    print("3 - Tesoura")

    opcoes = ["Pedra", "Papel", "Tesoura"]
    escolha_usuario = int(input("Digite o número da sua escolha: "))
    escolha_maquina = random.randint(1, 3)

    print("Você escolheu:", opcoes[escolha_usuario - 1])
    print("A máquina escolheu:", opcoes[escolha_maquina - 1])

    if escolha_usuario == escolha_maquina:
        print("Empate!")
    elif (
        (escolha_usuario == 1 and escolha_maquina == 3)
        or (escolha_usuario == 2 and escolha_maquina == 1)
        or (escolha_usuario == 3 and escolha_maquina == 2)
    ):
        print("Você ganhou!")
    else:
        print("Você perdeu!")

    jogar_novamente = input("Deseja jogar novamente? (S/N): ")
    if jogar_novamente.lower() == "s":
        jogar()
    else:
        print("Obrigado por jogar!")

jogar()'''



"""import pygame
import random

# Inicialização do Pygame
pygame.init()

# Cores
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
BRANCO = (255, 255, 255)

# Configurações da tela
largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Minigame: Quadrados com Barra de Vida e Contador de Tempo")

# Variáveis do jogador
jogador_tamanho = 50
jogador_x = largura_tela // 2 - jogador_tamanho // 2
jogador_y = altura_tela - jogador_tamanho - 10
jogador_velocidade = 5

# Variáveis dos quadrados
quadrado_tamanho = 50
quadrado_x = random.randint(0, largura_tela - quadrado_tamanho)
quadrado_y = -quadrado_tamanho
quadrado_velocidade = 3

# Variáveis da barra de vida
vida_total = 100
vida_atual = vida_total

# Variáveis do contador de tempo
tempo_total = 30
tempo_restante = tempo_total * 60  # Convertendo para frames

# Relógio para controlar os frames por segundo
relogio = pygame.time.Clock()

# Função para desenhar o jogador na tela
def desenhar_jogador(x, y):
    pygame.draw.rect(tela, VERDE, (x, y, jogador_tamanho, jogador_tamanho))

# Função para desenhar o quadrado na tela
def desenhar_quadrado(x, y):
    pygame.draw.rect(tela, VERMELHO, (x, y, quadrado_tamanho, quadrado_tamanho))

# Função para desenhar a barra de vida na tela
def desenhar_barra_de_vida(vida):
    pygame.draw.rect(tela, VERMELHO, (10, 10, vida, 20))

# Função para desenhar o contador de tempo na tela
def desenhar_contador_tempo(tempo):
    fonte = pygame.font.Font(None, 36)
    texto = fonte.render("Tempo Restante: " + str(tempo // 60), True, BRANCO)
    tela.blit(texto, (largura_tela - 200, 10))

# Loop principal do jogo
terminou = False
while not terminou:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            terminou = True

    # Movimentação do jogador
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and jogador_x > 0:
        jogador_x -= jogador_velocidade
    if teclas[pygame.K_RIGHT] and jogador_x < largura_tela - jogador_tamanho:
        jogador_x += jogador_velocidade

    # Movimentação do quadrado
    quadrado_y += quadrado_velocidade
    if quadrado_y > altura_tela:
        quadrado_x = random.randint(0, largura_tela - quadrado_tamanho)
        quadrado_y = -quadrado_tamanho
        vida_atual -= 10

    # Verificação de colisão entre jogador e quadrado
    if jogador_x < quadrado_x + quadrado_tamanho and jogador_x + jogador_tamanho > quadrado_x and jogador_y < quadrado_y + quadrado_tamanho and jogador_y + jogador_tamanho > quadrado_y:
        quadrado_x = random.randint(0, largura_tela - quadrado_tamanho)
        quadrado_y = -quadrado_tamanho
        vida_atual -= 20

    # Atualização da tela
    tela.fill(PRETO)
    desenhar_jogador(jogador_x, jogador_y)
    desenhar_quadrado(quadrado_x, quadrado_y)
    desenhar_barra_de_vida(vida_atual)
    desenhar_contador_tempo(tempo_restante)
    pygame.display.update()

    # Verificação de fim de jogo
    if vida_atual <= 0 or tempo_restante <= 0:
        terminou = True

    # Contagem regressiva do contador de tempo
    tempo_restante -= 1

    # Limitação de frames por segundo
    relogio.tick(60)

# Fim do jogo
pygame.quit()
"""

