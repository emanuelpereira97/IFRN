import random


#Gerando um numero aleatório e armazenando
numero_secreto = random.randint(1,100)
print(numero_secreto)
#Primeira tentativa do usuario
print("Tente adivinhar o número que sortiei...Você tem 4 tentativas")
print("Tentativa 01 - Digite um número inteiro entre 1 e 100: ")
tentativa1 = int(input())

#Checando se o numero informado pelo usuario é igual ao número aleatório armazenado, caso não seja alterando o intervalo exibido, idem para as proximas tentivas
#Tentativa 2
if tentativa1 == numero_secreto:
    print("Você acertou o número sorteado. Já pode jogar na mega sena!!")
elif tentativa1 < numero_secreto:
    print("Tentativa 02 - Digite um outro número entre",tentativa1+1,"e 100: ")
    tentativa2=int(input())
elif tentativa1 > numero_secreto:
    print("Tentativa 02 - Digite um outro número entre 1 e", tentativa1)
    tentativa2=int(input())
#verificando novamente
#Tetativa 3
    if tentativa2 == numero_secreto:
        print("Você acertou o número sorteado. Já pode jogar na mega sena!!")
    elif tentativa2 < numero_secreto:
        print("Tentativa 03 - Digite um outro número entre",tentativa2+1,"e 100: ")
        tentativa3=int(input())
    elif tentativa2 > numero_secreto:
        print("Tentativa 03 - Digite um outro número entre", tentativa1+1, "e", tentativa2)
        tentativa3=int(input())

        #verificando mais uma vez
        #tentativa 4
        if tentativa3 == numero_secreto:
            print("Você acertou o número sorteado. Já pode jogar na mega sena!!")
        elif tentativa3 < numero_secreto:
            print("Tentativa 04 - Digite um outro número entre",tentativa3+1,"e 100: ")
            tentativa4=int(input())
        elif tentativa3 > numero_secreto:
            print("Tentativa 04 - Digite um outro número entre 1 e", tentativa3)
            tentativa4=int(input())
        else:
            print("Você esgotou as tentativas, o número sorteado era",numero_secreto)