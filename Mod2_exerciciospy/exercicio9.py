# Contadores
num_pares = 0
num_impares = 0

# condicao
while True:
    num = int(input('Digite um número (ou zero para sair): '))

    # Encerra o loop quando o valor for zero
    if num == 0:
        break

    # Valida se o número é positivo
    if num > 0:
        # Incrementa o contador de pares se o número for par
        if num % 2 == 0:
            num_pares += 1
        # Incrementa o contador de ímpares se o número for ímpar
        else:
            num_impares += 1
    else:
        print('Apenas números positivos são aceitos.')

# Exibe a quantidade de números pares e ímpares inseridos
print('A quantidade de números pares inseridos é: {}'.format(num_pares))
print('A quantidade de números ímpares inseridos é: {}'.format(num_impares))