# leitura de arquivos

"""arquivo = open('./receitas/brigadeiro.txt')
print(arquivo.read())
print(arquivo.readline()) # Leitura de linhas
print(arquivo.closed)
arquivo.close()
print(arquivo.closed)
"""

# leitura de arquivos de forma pythoniana

"""with open('./receitas/brigadeiro.txt') as a:
    print(a.read())
    print(a.closed) #verificando se está realmente fechado
print(a.closed) # Está realmente fechado
"""
# escrita

"""with open('./receitas/brigadeiro.txt', 'w') as arquivo:
       arquivo.write("imaginação")
   """
"""arquivo = open(".\\receitas/brigadeiro.txt", "w")
arquivo.write("Padaria")
arquivo.close()"""

texto = """Loja
ola ola ola
compras:
pão
leite
suco
frutas
a
 b
 c
"""

with open('./receitas/brigadeiro.txt', 'w') as arquivo:
       arquivo.write(texto)