# solicite o nome, email e senha do usuario

# logo em seguida realize um PRINT com suas infos

nome = input("qual o seu nome?")
email = input("Digite seu email:")
senha = input("crie uma senha:")

if nome.strip() == "":
    print("Nome não preenchido!")
    
print("o seu cadastro é:", nome , "\n" , "o seu email é:", email, "\n" , "a sua senha é:", senha)

