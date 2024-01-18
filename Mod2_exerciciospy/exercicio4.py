# usuário informa uma nota entre zero e dez
nota = None
while nota is None: #condicao se a nota eh valida ou nao
    nota = float(input('Por favor, informe uma nota entre zero e dez: '))
    if nota < 0 or nota > 10:
        print('Nota inválida!')
        nota = None

# Classificacao com base em sua pontuação
if nota >= 7:
    resultado = "Aprovado"
else:
    resultado = "Reprovado"

# resultado exibido
print('O aluno foi {}.'.format(resultado))