'''1-) Dados o valor de uma conta em um restaurante (valor inteiro) e o valor do
pagamento, apresente o número mínimo de cédulas e moedas que deve ser
retornado como troco.'''

valor_conta = int(input("Digite. Quanto custou a sua conta? "))
pagamento = int(input("Digite. Com quanto você vai pagar? "))

notas = {200:0,100:0,50:0,20:0,10:0,5:0,2:0,1:0}
troco = pagamento - valor_conta

print(f'Seu troco é R${troco}')
for nota in notas.keys():
    qtd_cedula = troco // nota
    troco =(troco - (qtd_cedula*nota))
    if qtd_cedula != 0:
        notas[nota] = qtd_cedula
    #print(f'Quatidade notas de ${nota} : {qtd_cedula}')
print(f'Sugestão de troco:{notas}')