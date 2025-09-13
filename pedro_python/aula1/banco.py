print("..........................................")
print("Bem-vindo ao BANCO E.T corporation")
print(".........................................")
saldo = float(input("Digite seu saldo.....R$"))

transferencia = float(input("Qual o valor da transferência?"))

if saldo >= transferencia:
    print("Saldo suficiente para fazer a transferência")
    saldo = saldo - transferencia
    print("Seu saldo atual é de R$", saldo)
elif saldo < transferencia:
    print(".....................................................................")
    print("Seu saldo não é suficiente para fazer essa transferencia")
    print(".....................................................................")
    print("Deseja fazer um empréstimo com a gente?")
else:
    print("Você não possui saldo suficiente")


