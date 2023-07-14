class Conta:
    # Atributo de classe 
    taxa = 0.50  # Atributo de classe

    @staticmethod
    def retornarCodigoBanco():
        return '345'

# Atributos de Instâncias
    def __init__(self, numero, titular, saldo=2000):
        self.numero = numero# Visibilidade protegida(protected)
        self.titular = titular# Visibilidade pública(public)
        self.__saldo = saldo# Visibilidade privada(private)

    def extrato(self):
        print(f'Saldo: R${self.__saldo}')

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
        else:
            print("Saldo insuficiente.")

    def transferir(self, valor, destino):
        if self.__saldo >= valor:
            self.__saldo -= valor
            destino.depositar(valor)
        else:
            print("Saldo insuficiente.")


conta1 = Conta(123, 'Mona Lisa', 2300)
conta2 = Conta(345, 'Albert')

conta1.transferir(300, conta2)
conta1.extrato()
conta2.extrato()
