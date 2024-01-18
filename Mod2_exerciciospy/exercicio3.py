# usuário informa uma nota entre zero e dez
nota = None
while nota is None: #condicao se a nota eh valida ou nao
    nota = float(input('Por favor, informe uma nota entre zero e dez: '))
    if nota < 0 or nota > 10:
        print('Nota inválida!')
        nota = None

# mensagem de sucesso
print('Nota válida informada!')