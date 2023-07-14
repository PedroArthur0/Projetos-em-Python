class Pessoa:

    # (superclasse) - classe pai - classe mãe

    def __init__(self, nome=None, idade=None, data=None, cpf=None, rg=None):
        self.nome = nome
        self.idade = idade
        self.data_nascimento = data
        self.cpf = cpf
        self.rg = rg

    def imprimir_nome(self):
        return self.nome


# Classes concretas - contem instâncias  - objetos - execução de objetos
class Administrador(Pessoa):
    def trabalhar(self):
        nome_classe = self.__class__.__name__
        print(f'classe {nome_classe} organizando planilhas...')

 # Classes concretas - contem instâncias  - objetos - execução de objetos


class Aluno(Pessoa):

    # (subclasse) - classe filha(o)

    def __init__(self, nome):
        super().__init__(nome=nome)  # Chama o construtor da classe pai passando o nome
        self.matricula = None
        self.notas = []

    def estudar(self):
        return "Estudando..."


# Classes concretas - contem instâncias  - objetos - execução de objetos
class Professor(Pessoa):

    def trabalhar(self):
        nome_classe = self.__class__.__name__
        print(f'classe {nome_classe} Ensinando...')

    def __init__(self, nome):

        super().__init__(nome=nome)  # Chama o construtor da classe pai passando o nome
        self.disciplinas = []


"""aluno1 = Aluno('Pedro Arthur')
print(aluno1.imprimir_nome())
"""
professor1 = Professor('Marcelo')
Administrador1 = Administrador()
professor1.trabalhar()
Administrador1.trabalhar()

"""print(type(aluno1))
print(aluno1.estudar())
print(type(professor1))
"""
