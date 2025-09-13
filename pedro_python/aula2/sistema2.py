
# Sistema gerenciador de nomes

nomes = []

def menu( ):
    print(" === MENU ===")
    print("1 - Cadastrar nomes:")
    print("2 - listas de nomes:")
    print("3 - deletar nome especifico:")
    print("9 - Sair do sistema")

while True:

    menu()

    opcao = input("Escolha sua opção:")


    if opcao == "1":
        nome = input("Coloque um nome aqui:")
        nomes.append(nome)
        print("Nome adicionado com sucesso!!")

    elif opcao == "2":
        if len(nomes) == 0:
            print("Não existe nomes cadastrados")
        else:
            for nome in nomes:
                print(nome)
    elif opcao == "3":
        if len(nomes) == 0:
            print("nenhum nome cadastrado")
        else:
            for posicao, nome in enumerate(nomes):
                print(f"{posicao}. {nome}")

            pos = input("escolha o nome para deletar...")
            nomes.remove(nomes[pos])
            print("Nome específico deletado")

    elif opcao == "9":
        print("Saindo do sistema")
        break
    else:
        print("Opçao inexistente, tente novamente!")

    


