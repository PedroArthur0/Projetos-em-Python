preco_unitario = 10
DESCONTO10 = 0.1
DESCONTO20 = 0.2
quantidade = eval(input("Digite a quantidade de produtos que deseja comprar: "))
if(quantidade) >= 10: # Menor ou igual não é aplicado o desconto
    valor_final = preco_unitario * quantidade
elif(quantidade) <= 20: # Quantidades > a 10 e < 20 é aplicado 0.1 = 10 %
    valor_final = preco_unitario * quantidade * (1 - DESCONTO10)
else:                   # > 20 é aplicado 0.2 = 20 %
    valor_final = preco_unitario * quantidade * (1 - DESCONTO20)
print(f"O valor da compra é: {valor_final}")
