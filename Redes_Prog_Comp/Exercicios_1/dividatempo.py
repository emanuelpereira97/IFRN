import math

dividaInicial = float(input("Digite o valor inicial da divida: "))
montante = float(input("Digite o valor da divida acumulada: "))
taxaJuros = float(input("Digite a taxa de juros ao mês: "))

montanteLog = (math.log1p((montante/dividaInicial)-1))
taxaLog = math.log1p((taxaJuros/100))

tempo = math.ceil(montanteLog/taxaLog)
    
print("Levará ",tempo," meses para a divida alcançar ",montante)