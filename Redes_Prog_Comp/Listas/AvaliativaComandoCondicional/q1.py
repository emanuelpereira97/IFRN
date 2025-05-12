
#Coletando peso e altura e armazenando
altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite seu peso em quilograma: "))

#Calculando o IMC
imc = round(peso/(altura**2),1)
print(imc)

#Verificando em que intervalo o valor calculado do IMC se encaixa e informado o status correspondente
if imc <= 18.5:
    print("Seu IMC é de: ",imc,". Esse valor é cosiderado abaixo do normal.")
elif imc >= 18.6 and imc <= 24.9:
    print("Seu IMC é de: ",imc,". Esse valor é cosiderado normal.")
elif imc >= 25 and imc <= 29.9:
    print("Seu IMC é de: ",imc,". Esse valor é cosiderado sobrepeso.")
elif imc >= 30 and imc <= 34.9:
    print("Seu IMC é de: ",imc,". Esse valor é cosiderado obsidade grau 1.")
elif imc >= 35 and imc <= 39.9:
    print("Seu IMC é de: ",imc,". Esse valor é cosiderado obsidade grau 2.")
elif imc >= 40:
    print("Seu IMC é de: ",imc,". Esse valor é cosiderado obsidade grau 3.")
