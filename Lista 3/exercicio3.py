# funcao lista de compras 
def listar_carrinho():
    for k, v in carrinho.items():
        print(f"{k}: {v}")

# funcao adicionar a qtd e o produto
def adicionar_produto(produto, quantidade):
    if produto in carrinho:
        carrinho[produto] += quantidade
    else:
        carrinho[produto] = quantidade

#funcao remover a qtd e o produto
def remover_produto(produto, quantidade):
    if produto in carrinho:
        if carrinho[produto] <= quantidade:
            del carrinho[produto]
        else:
            carrinho[produto] -= quantidade
    else:
        print('Produto nao encontrado.')

#funcao calcular o total do carrinho
def calcular_total():
    total = 0
    for k, v in carrinho.items():
        total += k * v
    return total

#funcao do menu
def menu():
    print('Selecione uma opcao:')
    print('1 - Listar carrinho')
    print('2 - Adicionar produto')
    print('3 - Remover produto')
    print('4 - Calcular total do carrinho')
    print('5 - Sair')

carrinho = {}

while True: #condicao para selecionar o que o usuario quer
    menu()
    opcao = int(input('Digite o numero da opcao desejada: '))

    if opcao == 1:
        listar_carrinho()
    elif opcao == 2:
        produto = float(input('Informe o preço do produto: '))
        quantidade = int(input('Informe a quantidade do produto: '))
        adicionar_produto(produto, quantidade)
    elif opcao == 3:
        produto = float(input('Informe o preço do produto que deseja remover: '))
        quantidade = int(input('Informe a quantidade do produto que deseja remover: '))
        remover_produto(produto, quantidade)
    elif opcao == 4:
        total = calcular_total()
        print(f'O total do carrinho é: R$ {total:.2f}')
    elif opcao == 5:
        break
    else:
        print("Opcao invalida. Tente novamente.")