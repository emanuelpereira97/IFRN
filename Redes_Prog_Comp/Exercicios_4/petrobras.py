import csv

# Abrir o arquivo CSV e armazenar os dados em uma lista de dicionários
dados = []

with open('petr4.csv', mode='r', encoding='utf-8') as arquivo:
    leitor = csv.DictReader(arquivo)  # Lê o arquivo como dicionário (usando cabeçalho como chave)
    for linha in leitor:
        dados.append(linha)  # Adiciona cada linha como um dicionário à lista

# Exemplo: Mostrar os dados carregados
for registro in dados:
    print(registro)

# Acessar dados específicos (exemplo: primeira linha, coluna "Nome")
print(dados[0]['Nome'])
