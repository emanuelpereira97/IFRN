x = 1
while x <= 100: 
    ndiv = 0
    div = 1
    while div <= x:
        if x % div == 0:
            ndiv = ndiv + 1
        div = div + 1
    if ndiv == 2:
        print(x, 'é primo')
    x = x + 1