class Aluno:

    def __init__(self, nome, idade, matricula):
        self.__nome = nome
        self._idade = idade
        self.__matricula = matricula
        self.__notas = None

    @property  # Decorador em Python
    def nome(self):  # Get é o mesmo que pegar ou seja pegar o nome e alterar
        return self.__nome

    @nome.setter
    def nome(self, nome):  # Set altera um valor
        self.__nome = nome

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        self._idade = idade


aluno1 = Aluno('Pedro', 20, 123456)

print(aluno1.nome, aluno1.idade)
aluno1.nome = input('Digite o novo nome: ')
aluno1.idade = int(input('Digite a nova idade: '))
print(f'Nome: {aluno1.nome}, Idade: {aluno1.idade}')
