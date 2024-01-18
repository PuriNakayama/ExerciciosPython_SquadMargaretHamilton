# Le três números inteiros
num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))
num3 = int(input('Informe o terceiro número: '))

# Organiza os números em ordem crescente
if num1 > num2:
    num1, num2 = num2, num1
if num1 > num3:
    num1, num3 = num3, num1
if num2 > num3:
    num2, num3 = num3, num2

# Exibir os números em ordem crescente
print('A ordem crescente dos números é: {} {} {}'.format(num1, num2, num3))