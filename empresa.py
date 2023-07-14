class Funcionario:
    def trabalhar(self):
        print("trabalhando")
        

class FrontEnd(Funcionario):
    pass
    """def trabalhar(self):
        print("FrontEnd")"""


class BackEnd(Funcionario):
    pass
    """def trabalhar(self):
        print("BackEnd")"""



class FullStack(FrontEnd, BackEnd):
    pass
    """def trabalhar(self):
        print("FullStac")"""


Jose = FrontEnd()
Marcos = BackEnd()
Pedro = FullStack()
Jose.trabalhar()
Marcos.trabalhar()
Pedro.trabalhar()
