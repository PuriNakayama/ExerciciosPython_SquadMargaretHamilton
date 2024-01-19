# funcao para listar os contatos 
def listar_contatos():
    for k, v in dicionario_contatos.items():
        print(f"{k}: {v}")

# funcao para adicionar os contatos 
def adicionar_contato(nome, telefone):
    dicionario_contatos[nome] = telefone

#funcao para procurar os contatos 
def procurar_contato(nome):
    if nome in dicionario_contatos:
        print(f'Nome: {nome}, Telefone: {dicionario_contatos[nome]}')
    else:
        print('Contato não encontrado.')

# funcao menu
def menu():
    print('Selecione uma opcao:')
    print('1 - Listar contatos')
    print('2 - Adicionar contato')
    print('3 - Procurar contato')
    print('4 - Sair')

dicionario_contatos = {}

#condicao para o menu
while True:
    menu()
    opcao = int(input('Informe o numero da opcao desejada: '))

    if opcao == 1:
        listar_contatos()
    elif opcao == 2:
        nome = input('Informe o nome do contato: ')
        telefone = input('Informe o telefone do contato: ')
        adicionar_contato(nome, telefone)
    elif opcao == 3:
        nome = input('Informe o nome do contato que deseja procurar: ')
        procurar_contato(nome)
    elif opcao == 4:
        break
    else:
        print('Opcao invalida. Tente novamente.')