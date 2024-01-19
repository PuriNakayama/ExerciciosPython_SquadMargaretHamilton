def listar_contatos():
    for k, v in dicionario_contatos.items():
        print(f"{k}: {v}")

def adicionar_contato(nome, telefone):
    dicionario_contatos[nome] = telefone

def procurar_contato(nome):
    if nome in dicionario_contatos:
        print(f"Nome: {nome}, Telefone: {dicionario_contatos[nome]}")
    else:
        print("Contato não encontrado.")

def menu():
    print("Selecione uma opção:")
    print("1 - Listar contatos")
    print("2 - Adicionar contato")
    print("3 - Procurar contato")
    print("4 - Sair")

dicionario_contatos = {}

while True:
    menu()
    opcao = int(input("Digite o número da opção desejada: "))

    if opcao == 1:
        listar_contatos()
    elif opcao == 2:
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone do contato: ")
        adicionar_contato(nome, telefone)
    elif opcao == 3:
        nome = input("Digite o nome do contato que deseja procurar: ")
        procurar_contato(nome)
    elif opcao == 4:
        break
    else:
        print("Opção inválida. Tente novamente.")