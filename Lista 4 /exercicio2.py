# funcao para fazer o reverso do numero
def reverso_numero(num):
    return int(str(num)[::-1])

# usuario insere um numero inteiro
num = int(input('Digite um número inteiro: '))

# chama a funcao
reversao = reverso_numero(num)

# mostra o numero invertido
print(f'O número revertido é: {reversao}' )