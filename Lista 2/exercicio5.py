#funcao para classificar o triangulo
def classificacao_triangulo():
    a = float(input('Digite o comprimento do primeiro lado: '))
    b = float(input('Digite o comprimento do segundo lado: '))
    c = float(input('Digite o comprimento do terceiro lado: '))

    #verifica se os lados formam um triângulo
    if (a + b > c) and (a + c > b) and (b + c > a):
        #verifica se os lados são iguais
        if a == b == c:
            print('O triângulo é equilatero.')
        #verifica se dois lados são iguais
        elif a == b or a == c or b == c:
            print('O triângulo é isosceles.')
        # se nenhum dos lados forem iguais
        else:
            print('O triangulo é escaleno.')
    else:
        print('Os valores inseridos não formam um triangulo.')

classificacao_triangulo()