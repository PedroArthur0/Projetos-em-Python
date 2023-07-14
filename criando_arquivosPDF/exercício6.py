import datetime


def calcular_idade(data_nascimento):
    hoje = datetime.date.today()
    data_nascimento = datetime.datetime.strptime(
        data_nascimento, '%d/%m/%Y').date()
    idade = hoje.year - data_nascimento.year
    if hoje.month < data_nascimento.month or (hoje.month == data_nascimento.month and hoje.day < data_nascimento.day):
        idade -= 1
    return idade


def salvar_paciente(nome, email, cpf, rg, telefone, data_nascimento):
    idade = calcular_idade(data_nascimento)
    grupo_risco = idade >= 65

    with open('dados_pacientes.txt', 'a') as arquivo:
        arquivo.write(f"Nome: {nome}\n")
        arquivo.write(f"E-mail: {email}\n")
        arquivo.write(f"CPF: {cpf}\n")
        arquivo.write(f"RG: {rg}\n")
        arquivo.write(f"Telefone: {telefone}\n")
        arquivo.write(f"Data de Nascimento: {data_nascimento}\n")

        if grupo_risco:
            arquivo.write("Grupo de Risco: Sim\n")
        else:
            arquivo.write("Grupo de Risco: Não\n")

        arquivo.write("\n")


def exibir_pacientes():
    with open('dados_pacientes.txt', 'r') as arquivo:
        print(arquivo.read())


def registrar_paciente():
    while True:
        nome = input("Digite o nome completo do paciente: ")
        email = input("Digite o e-mail do paciente: ")
        cpf = input("Digite o CPF do paciente: ")
        rg = input("Digite o RG do paciente: ")
        telefone = input("Digite o telefone do paciente: ")
        data_nascimento = input(
            "Digite a data de nascimento do paciente (DD/MM/AAAA): ")

        salvar_paciente(nome, email, cpf, rg, telefone, data_nascimento)

        print("Paciente registrado com sucesso!")

        opcao = input("Deseja registrar um novo paciente? (S/N): ")
        if opcao.upper() != 'S':
            break


registrar_paciente()
exibir_pacientes()
