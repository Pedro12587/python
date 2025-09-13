print("******************************************")
idade = int(input("Digite sua idade..."))

if idade < 18:
    print("***************************************")
    print("Você é menor de idade!")
    print("***************************************")
else:
    print("***************************************")
    print("Você é maior de idade!")
    print("***************************************")
    if idade >= 18 and idade <=70:
        print("Seu voto é obrigatório!")
    else:
        print("Seu voto é facultativo")