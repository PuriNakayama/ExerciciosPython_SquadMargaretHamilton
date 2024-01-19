#funcao para identificar 
def identificar_grupo():
    idade = int(input('Digite sua idade: '))

#condicao para verificar a idade
    if idade < 13:
        print('Você é uma criança.')
    elif idade < 18:
        print('Você é um adolescente.')
    elif idade < 60:
        print('Você é um adulto.')
    else:
        print('Você é um idoso.')

identificar_grupo()