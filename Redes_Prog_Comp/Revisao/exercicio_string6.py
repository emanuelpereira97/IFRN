frase = input("Digite uma frase qualquer: ").replace(" ", "").lower()
caractere = input("Digite uma letra: ").lower()

posicoes = []
for indice, letra in enumerate(frase):
    if letra == caractere:
        posicoes.append(indice)
print (f'A letra {caractere} aparece {len(posicoes)} vezes.')


