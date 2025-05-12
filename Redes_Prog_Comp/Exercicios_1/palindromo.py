numero_digitado = int(input("Digite um número de 3 digitos: "))
if 100 < numero_digitado < 999:
    unidade = numero_digitado%10
    numero_1 = numero_digitado//10

    dezena = numero_1%10
    numero_2 = numero_1//10

    centena = numero_2%10
    numero_3 = numero_2//10
#inverso=0
#inverso=inverso*10+unidade
#inverso=inverso*10+dezena
#inverso=inverso*10+centena

    numero_inverso = unidade*10+dezena
    numero_inverso = numero_inverso*10+centena

    if numero_inverso == numero_digitado:
        print("O número que você digitou é um palindromo")
    else:
        print("O número que você digitou não é um palindromo")
else:
    print("Você não digitou um número de 3 digitos!!")