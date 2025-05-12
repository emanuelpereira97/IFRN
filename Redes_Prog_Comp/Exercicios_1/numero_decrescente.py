numero_digitado = int(input("Digite um número de 4 digitos "))
if 1000 <= numero_digitado < 9999:
    unidade = numero_digitado%10
    n1 = numero_digitado//10

    dezena = n1%10
    n2 = n1//10

    centena = n2%10
    n3 = n2//10

    milhar = n3%10
    n4 = n3//10

    if milhar >= centena >= dezena >= unidade:
        print("O número é decrescente")

    else:
        print("O número crescente")
else:
    print("Você não digitou um número de 4 digitos!!")

#5444
#5544
#5554