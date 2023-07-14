# Exemplo 1
def primo(numero):
    if numero > 1:
        for x in range(2,numero):
            if(numero % x) == 0:
                return "Esse número é primo!"
        else:
            return "Esse número não é primo!"
    else:
        return "Esse número não é primo ou é menor do que 1."
    
# Exemplo 2

def eh_primo(p):
    if (p<2):
        return False
    i = p//2
    while(i>1):
        if (p%i==0):
            return False
        i= i-1
    return True
def imprimir_resultado(numero, resultado):
    mensagem = f'O número {numero} não é primo.'
    if resultado:
        mensagem = f'O número {numero} é primo.'
    return mensagem
numero = int(input())
resultado = eh_primo(numero)
msg = imprimir_resultado(numero, resultado)
print(msg)
