'''2) Receba como entrada os coeficientes (inteiros) de uma equação de segundo grau:
a, b e c, e apresente as raízes reais.'''

try:
    a= int(input("Digite um valor inteiro para o coeficiente a: "))
    if a == 0:
        raise ValueError("a não pode ser zero")
    b= int(input("Digite um valor inteiro para o coeficiente b: "))
    c= int(input("Digite um valor inteiro para o coeficiente c: "))    
    delta = (b*b) - (4*a*c) 
    if (delta == 0):
        x1 = (-b)/(2*a)
        print(f'Como delta é ={delta}, por isso X1 e X2 são iguais à: {x1}')
    elif (delta > 0):
        x1 = round((-b+(delta**(1/2)))/(2*a),2)
        x2 = round((-b-(delta**(1/2)))/(2*a),2)
        print(f'Como delta positivo e igual à {delta}, X1 é {x1}  e X2 é {x2}')
    elif (delta < 0):
        print(f'Como delta é negativo, não existem raizes reais.')
except ValueError:
    print("Valor inválido inserido. Por favor, insira um número inteiro.")