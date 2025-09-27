# para a API

from flask import Flask, request, render_template, redirect

# Salvar CSV

import csv, os

app = Flask(__name__)

ARQUIVO = 'dados.csv'

# Criar o arquivo csv caso ele não exista
def inicializar_csv():
    if not os.path.exists(ARQUIVO):
        with open(ARQUIVO, 'w', newline="", encoding="utf-8") as arquivo:
            writer = csv.writer(arquivo)
            writer.writerow(["Nome", "Email", "Produto", "Quantidade"])

# ler os registros do sistema

def ler_registros():
    inicializar_csv()
    with open(ARQUIVO, 'r', newline="", encoding="utf-8") as arquivo:
        reader = csv.reader(arquivo)
        return list(reader)
    
@app.route("/", methods=["GET", "POST"])
def index():

    # se for o metodo POST a pessoa vai criar algo
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        produto = request.form["produto"]
        quantidade = request.form["quantidade"]

        with open(ARQUIVO, 'a', newline="", encoding="utf-8") as arquivo:
            writer = csv.writer(arquivo)
            writer.writerow([nome, email, produto, quantidade])

# GET
    registros = ler_registros()
    return render_template("index.html", registros=registros)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form["usuario"]
        senha = request.form["senha"]

        if usuario == "admin" and senha == "123":
            return redirect("/")
        elif usuario == "pedro" and senha == "12345":
            return redirect("/")
        else:
            return redirect("/login?error=true")
                
    return render_template("login.html")

if __name__ == "__main__":
    inicializar_csv()
    app.run(debug=True)    
