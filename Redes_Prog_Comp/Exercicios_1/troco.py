valorConta = int(input("Digite o valor da conta: "))
valorPagar = int(input("Com quanto você vai pagar? "))
troco = valorPagar - valorConta

print("O valor do troco é de: ", troco)

nota200 = troco//200
troco = (troco - (nota200*200))
print("Quantidade de notas de 00: ", nota200)

nota100 = troco//100 
troco = (troco - (nota100*100))
print("Quantidade de notas de 100: ", nota100)

nota50 = troco // 50
troco = (troco - (nota50*50))
print("Quantidade de notas de 50: ", nota50)

nota20 = troco // 20 
troco = (troco - (nota20*20))
print("Quantidade de notas de 20: ", nota20)

nota10 = troco // 10
troco = (troco - (nota10*10))
print ("Quantidade de notas de 10: ", nota10)

nota05 = troco // 5
troco = (troco - (nota05*5))
print ("Quantidade de notas de 5: ", nota05)

nota02 = troco // 2
troco = (troco - (nota02*2))
print ("Quantidade de notas de 2: ", nota02)