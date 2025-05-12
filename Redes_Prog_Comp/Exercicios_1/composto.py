capital = float(input("Digite seu capital incial: "))
taxa = float(input("Digite a taxa de juros por mês sob a qual o capital será aplicado: "))
tempo = int(input("Digite por quantos meses a taxa será aplicada: "))

montante = capital * ((1 + (taxa/100))**(tempo))

print (" Seu montante acumulado é de: R$", round(montante,2))