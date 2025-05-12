
#Encontrar um padrão que possa ser repetido e com ele somar até quantos número se queira
#soma = 0
#i =1

#soma = soma + i
#i = i + 1

#soma = soma + i
#i = i + 1

#soma = soma + i
#i = i + 1

n = int(input("Até quanto você quer somar? (digite um número) "))
soma = 0
i = 1
while i <= n:
    soma = soma + i
    i = i + 1
    print('soma=',soma,' - ','i=', i)
