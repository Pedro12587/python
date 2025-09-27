# sistema de tarefas

Tarefas = [] # lista vazia

while True:
    print("=== MENU TAREFAS ===")
    print("1 - Adicionar Tarefas")
    print("2 - Listar Tarefas")
    print("9 - Sair do Sistema")

    opcao = input("Escolha sua opção: ")

# adicionar tarefa

    if opcao == "1":
        tarefa = input("Digite a nova tarefa: ")

# append = Adicionar a lista

        Tarefas.append(tarefa)
        print("Tarefa adicionada com sucesso!")

# listar tarefas
    elif opcao == "2":
    # len = length = tamanho
        if len(Tarefas) == 0:
            print("Não existem tarefas cadastradas")
        else:
            for tarefa in Tarefas:
                print(tarefa)
    elif opcao == "9":
        print("Saindo do Sistema")
        break
    else:
        print("opção inexistente, tente novamente...")


    