# usuario informa dois números ao usuário
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

# condicao para determinar qual dos dois números é maior
if num1 > num2:
    maior_numero = num1
else:
    maior_numero = num2

# Imprime o maior dos dois números
print("O maior número é:", maior_numero)