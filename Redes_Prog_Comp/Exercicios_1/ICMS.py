valorCompra = float(input("Digite o valor de compra do produto: "))
valorVenda = float(input("Digite o valor de venda do produto: "))
ICMS = 17/100

valorLucro = valorVenda - valorCompra
valorRecolhido = valorLucro * ICMS

print ("O valor do ICMS recolhido é de: R$",round(valorRecolhido,2))
