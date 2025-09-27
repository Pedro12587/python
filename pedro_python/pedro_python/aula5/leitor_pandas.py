
import pandas as pd
import matplotlib.pyplot as plt

# pip install matplotlib

# pip install pandas

# ler o arquivo csv

df_csv = pd.read_csv("dados_pandas.csv")

df_filtrado = df_csv[df_csv["quantidade"] > 5]
print(df_filtrado)

df_ordenado = df_csv.sort_values(by="quantidade", ascending=False)
print(df_ordenado) # do maior para o menos (Decrescente)

# exibir estatisticas 
print(df_csv.describe())

# criar coluna faturamento
df_csv["faturamento"] = df_csv["quantidade"] * df_csv["preco"]

print(df_csv)

# vendas
# camiseta, 70
# camiseta, 30
# calculando a media de preco do produto

media_produto = df_csv.groupby("nome")["preco"].mean()
print(media_produto)

# grafico boxplot
# grid -> linhas

df_csv.boxplot(column="preco", by="nome", grid=True)

plt.title("Distrubição de preco por produto")
plt.xlabel("nome")
plt.ylabel("preco")

plt.show()