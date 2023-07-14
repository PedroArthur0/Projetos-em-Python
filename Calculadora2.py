# Receber um número
# Receber um operador
# Receber um outro número
# Mostrar o resultado

print("Digite um número:")
numero1 = int(input())

print("Digite um operador:")
operador = input()

print("Digite um segundo número:")
numero2 = int(input())

if operador == "+":
    resultado = numero1 + numero2
    print(resultado)
elif operador == "-":
    resultado = numero1 - numero2
    print(resultado)
elif operador == "*":
    resultado = numero1 * numero2
    print(resultado)
elif operador == "/":
    resultado = numero1 / numero2
    print(resultado)
else:
    print("Insira um operador válido.")
