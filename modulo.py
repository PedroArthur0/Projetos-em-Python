#import random
#from radom import choice
"""from random import (
    random, 
    choice, 
    uniform
)"""

"""from random import(
    random as rd
)

print(rd())"""

"""lista = ["pedra", "papel", "tesoura"]
print(choice(lista))

for x in range(1, 9):
    print(x)"""

# Observação final: Não se deve importar todo o módulo, pois pode ocupar espaço desnecessário no computador/aplicação etc...

"""from random import *
print(randint(1, 5))"""

# Módulos - Arquivos com extensão .py - ou seja o módulo é um arquivos do Python
# Pacotes - Diretórios contendo um conjunto de módulos - São pastas com vários arquivos Python

"""from pacote import principal, secundario

print(principal.soma(2, 3))
print(secundario.quadratica(5))"""

"""from pacote.sub_diretorio import outros as modulo 

print(modulo.cubica(3))"""
