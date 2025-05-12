'''3) A magia (ou pesadelo) dos juros compostos é que eles crescem que uma maneira
inimaginável. Sabendo que o montante acumulado para um capital c, a uma taxa
i (em porcentagem), por um tempo t é dado por:
Montante = c . ( 1 + i / 100) t 

Faça um programa que aceite os três parâmetros citados e informe o montante
gerado pelo capital.
'''

c = float(input("digite o valor do capital inicial: "))
i = float(input("digite o valor da taxa de juros ao mês: "))
t = float(input("digite o tempo em meses: "))

m = round(c * ((1 + (i/100))**t),2)

print(f'O montante acumulado é R${m}')