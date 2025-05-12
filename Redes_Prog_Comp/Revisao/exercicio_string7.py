frase = "A BitDogLab é uma placa educacional incrível".lower()
lista = frase.split()
tamanho_palavra = 0
palavra_mais_longa=""
for indice,palavra in enumerate(lista):
    if len(palavra) > tamanho_palavra:
        tamanho_palavra = len(palavra)
        palavra_mais_longa = palavra
print(tamanho_palavra,palavra_mais_longa)