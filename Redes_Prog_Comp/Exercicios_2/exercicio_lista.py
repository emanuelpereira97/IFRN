lista_1 = [1,2,3,4,5,6,7,8]
lista_2 = []

for pos in range (0,len(lista_1)-1):
    lista_2.append(lista_1[pos] + lista_1[pos+1])
print(lista_2)
