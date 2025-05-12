a = int(input("Digite o valor de a: ")) 
if a == 0:
    print("O valor para 'a', não pode ser zero. ")
else:
    b = int(input("Digite o valor de b: "))
    c = int(input("Digite o valor de c: "))
    delta = b**2 - 4*a*c
    if delta < 0:
        print("Delta menor que zero, não queremos imaginar nada!")
    else:
        x_1 = (- b + (delta)**(1/2))/(2*a)
        x_2 = (- b - (delta)**(1/2))/(2*a)
        print("O valor de x_1 é: ", x_1, " e o valor de x_2 é:", x_2)