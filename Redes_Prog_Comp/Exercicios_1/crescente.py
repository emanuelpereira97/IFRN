msg_entrada = "Digite um número: "
msg_saida = "Em ordem crecente: "

a = int(input(msg_entrada))
b = int(input(msg_entrada))
c = int(input(msg_entrada))

if a < b:
    p1 = a
elif a < c:
    p2 = a
else:
    p3 = a

if b < c:
    p1=b
elif b < a:
    p2=b
else:
    p3=b

if c < a:
    p1=c
elif c < b:
    p2=c
else:
    p3=c

print(msg_saida,p1,",",p2,",",p3)
