#funcao reverse
def reverse():
    nome = input('Digite o seu nome: ') #usuario insere o nome
    reverse_nome = nome[::-1].upper() #faz o reverse e coloca em capslock
    print(f'O nome digitado de trás para frente é: {reverse_nome}')

reverse()