print("**********************************")
print("Bem vindo ao sistema")
print("**********************************")
print("Digite se você é maior de idade")

valor = int(input("Digite 1 para maior e 0 para menor!!"))

if valor == 1:
    print("Você é maior de idade")
elif valor == 0:
    print("Você é menor de idade")
else:
    print(" é uma opção inválida")
