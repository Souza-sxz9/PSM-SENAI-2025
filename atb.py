pessoas = []

def cadastrar_pessoa():
    print("\n--- Cadastro de Pessoa ---")
    nome = input("Nome(Opcional): ")
    if len(nome) == 0:
        nome = "Não informado"
    while nome.isdigit():
        nome = input("Você digitou um número. Por favor, digite um nome válido: ")


    while True:
        entrada = input("Informe seu Gênero 1.(Masculino) 2.(Feminino) 3.(Outros): ")
    
        if entrada == "1":
            genero = "Masculino"
            break
        elif entrada == "2":
            genero = "Feminino"
            break
        elif entrada == "3":
            genero = "Outros"
            break
        else:
            print("Opção inválida. Por favor, digite 1, 2 ou 3.")


    idade = (int(input("Idade: ")))
    while idade <= 0:
        idade = int(input("Idade inválida. Digite novamente: "))

    email = input("E-mail: ")
    while not "@" in email or not "." in email:
        email = input("Email inválido! Deve conter '@' e '.': ")

    cidade = input("Cidade: ")
    while cidade.strip() == "":
        cidade = input(("O campo não pode estar vazio. Tente novamente."))
    
    mensagem = input("Diga-nos o que você está passando: ")
    while len(mensagem) == 0:
        mensagem = input("A mensagem não pode estar vazia! Digite novamente: ")
    while mensagem.isdigit():
        mensagem = input("Você digitou um número. Por favor, digite uma mensagem válida: ")
    
    
    pessoa = {
        "Nome": nome,
        "Idade": idade,
        "Email": email,
        "Cidade": cidade,
        "Mensagem": mensagem,
        "Gênero": genero,
    }
    pessoas.append(pessoa)
    print("Pessoa cadastrada com sucesso!")

def listar_pessoas():
    print("\n--- Lista de Pessoas ---")
    for indice, pessoa in enumerate(pessoas):
        print(f"{indice + 1}. {pessoa}")

def editar_pessoa():
    listar_pessoas()
    indice = int(input("Digite o número da pessoa para editar: ")) - 1
    
    if 0 <= indice < len(pessoas):
        pessoa = pessoas[indice]
        
        print("\nO que você deseja editar?")
        print("1. Nome")
        print("2. Gênero")
        print("3. Idade")
        print("4. E-mail")
        print("5. Cidade")
        print("6. Mensagem")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input(f"Nome atual: {pessoa['Nome']}. Novo nome: ")
            pessoa['Nome'] = nome if nome else pessoa['Nome']
        elif opcao == '2':
            genero = input(f"Gênero atual: {pessoa['Gênero']}. Novo gênero: ")
            pessoa['Gênero'] = genero if genero else pessoa['Gênero']
        elif opcao == '3':
            idade = input(f"Idade atual: {pessoa['Idade']}. Nova idade: ")
            pessoa['Idade'] = int(idade) if idade else pessoa['Idade']
        elif opcao == '4':
            email = input(f"E-mail atual: {pessoa['Email']}. Novo e-mail: ")
            pessoa['Email'] = email if email else pessoa['Email']
        elif opcao == '5':
            cidade = input(f"Cidade atual: {pessoa['Cidade']}. Nova cidade: ")
            pessoa['Cidade'] = cidade if cidade else pessoa['Cidade']
        elif opcao == '6':
            mensagem = input(f"Mensagem atual: {pessoa['Mensagem']}. Nova mensagem: ")
            pessoa['Mensagem'] = mensagem if mensagem else pessoa['Mensagem']
        else:
            print("Opção inválida.")
    else:
        print("Índice inválido.")


def excluir_pessoa():
    listar_pessoas()
    indice = int(input("Digite o número da pessoa para excluir: ")) - 1
    pessoas.pop(indice)

def menu():
    while True:
        print("\n====== MENU PRINCIPAL ======")
        print("1. Cadastrar Pessoa")
        print("2. Listar Pessoas")
        print("3. Editar Pessoa")
        print("4. Excluir Pessoa")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_pessoa()
        elif opcao == '2':
            listar_pessoas()
        elif opcao == '3':
            editar_pessoa()
        elif opcao == '4':
            excluir_pessoa()
        elif opcao == '5':
            print("Encerrando o sistema. As coisas irão melhorar!")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()