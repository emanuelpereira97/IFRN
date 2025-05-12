numero_digitado = int(input("Digite um numero com 3 digitos distintos: "))

#captuando o ultimo digito, atualizando variavel
terceira_casa=numero_digitado%10
numero_digitado=numero_digitado//10

#capturando o segundo digito, atualizando variavel
segunda_casa=numero_digitado%10
numero_digitado=numero_digitado//10

#capturando primeiro digito, atualizando variavel
primeira_casa=numero_digitado%10
numero_digitado=numero_digitado//10

numero_digitado = numero_digitado*10+terceira_casa
numero_digitado = numero_digitado*10+segunda_casa
numero_digitado = numero_digitado*10+primeira_casa

print(numero_digitado)