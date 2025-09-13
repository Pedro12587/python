from models.pessoa import Pessoa

def menu():
    print("=== MENU ===")
    print("1 - Criar pessoa")
    print("2 - Listar pessoas")
    print("3 - limpar lista")
    print("9 - Sair do Sistema")

def iniciarsistema():
    print("Sistema Iniciado")

    pessoas = [] # criar lista de pessoas

    while(True):
        menu()
        opcao = input("Selecione uma opção...")
        if opcao == "1":
            nome = input("Digite o nome da pessoa...")
            email = input("Digite o email da pessoa...")
            pessoa = Pessoa(nome, email) # Manifestando a entidade pessoa
            pessoas.append(pessoa) # Adicionar pessoas na lista
            print("Nome adicionado com sucesso...")

        elif opcao == "2":
            for pessoa in pessoas:
                print(f"Nome: {pessoa.get_nome()}, \n Email: {pessoa.get_email()}")

        elif opcao == "9":
            print("saindo do sistema...")
            break


#logica para iniciar automaticamente

if __name__ == "__main__":
    iniciarsistema()

