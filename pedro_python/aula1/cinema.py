print("..............................")
print("Bem-vindo ao cinema CINEPOLIS")
print("..............................")

nome = input("Qual o seu nome?")
idade = int(input("Qual a sua idade?"))
altura = float(input("Qual a sua altura?"))
print("..............................")

if idade >= 18 and altura > 1.75:
    print("pode entrar no cinema CINEPOLIS")
elif altura < 1.75:   
    print("não pode entrar")
else:    
    print("Não pode entrar no cinema CINEPOLIS")


""" 
if - SE
elif - CASE SE
else - CASO CONTRARIO

> - MAIOR
< - MENOR 
>= - MAIOR IGUAL
<= - MENOR IGUAL
== - IGUALDADE
"""