import os
# verificar se um arquivo existe

"""print(os.path.exists('texto.py'))
print(os.path.exists('texto.txt'))"""

# verificar se um diretório existe

"""print(os.path.exists('python'))
print(os.path.exists('pastanova'))"""

# exemplo de caminhos

"""print(os.path.exists('pastanova/texto.py'))"""

# criando arquivos

'''os.mknod('olamundo.py')'''

# criando  um diretório

#os.mkdir('python')

# caminho absoluto - path da raiz

#os.mkdir('/home/py/documentos/Python/arquivos/python/olamundo.py')
#os.mkdir('/home/py/documentos/Python/arquivos/python/loja')

# caminho relativo 

#os.mkdir('.python/compras.txt')
#os.mkdir('.python/compras2.txt')
#os.mkdir('.python/documentos')

# apagando arquivos

#os.remove('teste.txt')
#print(os.path.exists('teste.txt'))
#os.remove('olamundo')

#apagando diretórios

#os.remove('pastanova') - função exclusiva para arquivos
#os.rmdir('pastanova')
#os.remove('./pastanova/texto.py')
#os.remove('./python/olamundo.py')
#os.remove('.python/compras.txt')

# utilizando o os.rename()
import os
 
#os.mknod("olamundo.py") # criando um arquivo no meu diretório atual
#os.makedirs("pastanova") # criando um diretório chamado pastanova
#os.mknod('./pastanova/teste.txt') # criando no diretório chamado pastanova um arquivo chamado teste.txt

#os.rename("olamundo.py", "olamundo.txt") # modifica apenas arquivos contidos no diretório atual
#os.rename("olamundo.txt","olamundo.psd")
#os.rename("pastanova","documentos")
#os.mknod(".documentos/teste.txt")
#os.rename("./documentos/teste.txt","compras.txt")