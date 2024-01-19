# usuario insere tres numeros inteiros
num1 = int(input('Informe o primeiro numero: '))
num2 = int(input('Informe o segundo numero: '))
num3 = int(input('Informe o terceiro numero: '))

# organiza os numeros em ordem crescente
if num1 > num2:
    num1, num2 = num2, num1
if num1 > num3:
    num1, num3 = num3, num1
if num2 > num3:
    num2, num3 = num3, num2

# exibi os numeros em ordem crescente
print('A ordem crescente dos numeros é: {} {} {}'.format(num1, num2, num3))