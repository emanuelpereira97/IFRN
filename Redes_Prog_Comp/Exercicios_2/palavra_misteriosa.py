palavra_sorteada = 'visao'
tamanho_sorteada = len(palavra_sorteada)
tentativas = 2*tamanho_sorteada
atual = '_'*tamanho_sorteada
print(atual)

while tentativas < 0  and atual != palavra_sorteada:
    letra = input("Digite uma letra: ")
    nova = ''
    for pos in range (tamanho_sorteada):
        if palavra_sorteada[pos] == letra:
            nova +=palavra_sorteada[pos]
        else:
            nova +=atual[pos]
    print(nova)
    atual = nova
    tentativas -= 1
if atual == palavra_sorteada:
    print("Parabéns você acertou a palavra!!")
else:
    print("Lamento você esgotou a quantidade de tentativas. A palavra era:",palavra_sorteada)