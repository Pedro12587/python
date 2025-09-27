
import csv # xlsx - csv

# criando arquivo CSV

# Gerando dados
dados = [
    ["nome", "idade", "Cidade"],
    ["Arthur", "58", "Cotia"],
    ["Zago", "16", "Cotia"],
    ["Wishizack", "21", "Cotia"]
]

# criar CSV
# nomeArquivo, WRITE, novalinha,Codificação B -UTF8
with open("dados.csv", "w", newline="", encoding="utf-8") as csvarquivo:
    escritor = csv.writer(csvarquivo)
    escritor.writerows(dados)

# ler arquivo
with open("dados.csv", "r", encoding="utf-8") as csvarquivo:
    leitor = csv.reader(csvarquivo) # lendo o csv
    print("Conteudo do Arquivo")
    for linha in leitor:
        print(linha)