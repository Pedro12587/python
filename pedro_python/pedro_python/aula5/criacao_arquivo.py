
import csv

dados = [
    ["nome", "preco", "quantidade"],
    ["camiseta", "10.00", "8"],
    ["tenis", "20.00", "5"],
    ["chinelo", "60.00","1"],
    ["moletom", "170.00", "9"],
    ["jaqueta", "20.00", "2"], 
]

# criar arquivo

with open("dados_pandas.csv", "w", newline="", encoding="utf-8") as csvarquivo:
    escritor = csv.writer(csvarquivo)
    escritor.writerows(dados)