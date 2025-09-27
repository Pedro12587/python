import pandas as pd
import matplotlib.pyplot as plt

# pip install pandas
# pip install matplotlib

ARQUIVO = "produtos.csv"
CAMPOS = ["nome", "quantidade", "preco"]

df = pd.read_csv(ARQUIVO, encoding="utf-8")

df["Faturamento"] = df["quantidade"] * df["preco"]

df.boxplot(column="preco", by="nome", grid=True)
plt.title("Distribuição de Preço por nome")
plt.xlabel("nome")
plt.ylabel("preco")

plt.show()



df.plot(kind="bar", x="nome", y="preco", grid=True)
plt.title("Preço dos produtor")
plt.xlabel("nome")
plt.ylabel("preco")

plt.show()

df.plot(kind="pie", x="nome", y="preco", grid=True)
plt.title("Preço dos produtor")
plt.xlabel("nome")
plt.ylabel("preco")

plt.show()
