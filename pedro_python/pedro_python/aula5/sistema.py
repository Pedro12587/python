import csv
import time

ARQUIVO = "produtos.csv"

# Assim que executar ele verifica se o arquivo existe e cria

try:
    with open(ARQUIVO, "x", newline="")as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["nome","quantidade",'preco'])
except:
    pass # se ja existe o arquivo ele segue em frente

while True:
    nome = input("Digite o nome do produto:")
    quantidade = int(input("Digite a quantidade:"))
    preco = float(input("Digite o preco:"))

# escrever no arquivo csv

    with open(ARQUIVO, "a", newline="") as arquivo:  
        escritor = csv.writer(arquivo)
        escritor.writerow([nome, quantidade, preco])

    print(f"produto {nome} adicionado com sucesso!")

# perguntar se deseja continuar no sistema

    continuar = input("Deseja adicionar outro? (s/n):")
    if continuar == "n":
        print("Encerrando o sistema")
        break

    print("-" * 30) #--------------------------
    time.sleep(1) # ele vai demorar um segundo para rodar de novo
