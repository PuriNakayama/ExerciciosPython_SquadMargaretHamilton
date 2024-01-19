# usuario informa dois numeros ao usuario
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

# condicao para determinar qual dos dois numeros eh maior
if num1 > num2:
    maior_numero = num1
else:
    maior_numero = num2

# imprime o maior dos dois numeros
print("O maior numero é:", maior_numero)