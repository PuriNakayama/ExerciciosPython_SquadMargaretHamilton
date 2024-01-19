# contadores
num_pares = 0
num_impares = 0

# condicao
while True:
    num = int(input('Digite um numero (ou zero para sair): '))

    # encerra o loop quando o valor for zero
    if num == 0:
        break

    # valida se o numero eh positivo
    if num > 0:
        # incrementa o contador de pares se o numero for par
        if num % 2 == 0:
            num_pares += 1
        # incrementa o contador de impares se o numero for impar
        else:
            num_impares += 1
    else:
        print('Apenas numeros positivos são aceitos.')

# exibe a quantidade de numeros pares e impares inseridos
print('A quantidade de numeros pares inseridos é: {}'.format(num_pares))
print('A quantidade de numeros impares inseridos é: {}'.format(num_impares))