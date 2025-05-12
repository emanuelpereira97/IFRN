
#solicitando ao usuário que informa um ano qualquer
ano = int(input("Digite um ano qualquer: "))

#um ano é bissexto se terminado em 00 e divisivél por 400. Se não termina em 00, ele é bissexto se divisivél por 4
unidade_ano = ano % 10
dezena_ano = ano % 100
soma_ano = unidade_ano + dezena_ano
div1 = ano % 400
div2 = ano % 4

#verificando as condições mencionadas e imprimindo se é ou não bissexto
if unidade_ano == 0 and dezena_ano == 0 and div1==0:
    print(ano,"é um ano bissexto.")
elif soma_ano != 0 and div2 == 0:
    print(ano,"é um ano bissexto.")
else:
    print(ano,"não é bissexto.")
    