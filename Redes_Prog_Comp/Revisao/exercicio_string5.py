nome = input("Digite uma palavra: ").lower()
letra = input("Digite uma letra: ").lower()
contem = 0
if letra in nome:
    contem = "possui"
    print(f'A palavra {nome}, {contem} {nome.count(letra)} letra {letra}.')
else:
    contem = "não possui"
    print(f'A palavra {nome}, {contem} a letra {letra}.')