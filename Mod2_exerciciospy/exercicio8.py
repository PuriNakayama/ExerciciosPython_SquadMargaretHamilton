#funcao para achar o maior numero
def achar_maior_num():
    num1 = int(input('Informe o primeiro número: '))
    num2 = int(input('Informe o segundo número: '))
    num3 = int(input('Informe o terceiro número: '))

#condicao para verificar qual eh o maior numero
    if num1 > num2 and num1 > num3:
        print('O maior número é: {}'.format(num1))
    elif num2 > num1 and num2 > num3:
        print('O maior número é: {}'.format(num2))
    else:
        print('O maior número é: {}'.format(num3))

achar_maior_num()