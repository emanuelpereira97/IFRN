#Em andamento
while True: 
    print("Digite 0 para sair...")
    valor = int(input("Digite um numero inteiro: "))
    if valor == 0: break #condição de parada
    multiplicador = 1
    while multiplicador<=10: #gerando a tabuada para o valor informado
        print(valor, 'x',multiplicador,'=',valor*multiplicador)
        multiplicador += 1 #incrementando o multiplicador
print("Programa encerrado...")#mensagem de encerramento, quado a condição de parada for atendida