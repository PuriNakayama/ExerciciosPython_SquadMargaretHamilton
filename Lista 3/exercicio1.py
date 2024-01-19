# funcao para classificar a participacao
def classifica_participacao(respostas):
    contador = respostas.count(True)
    if contador == 5:
        return 'Assassino'
    elif contador == 4 or contador == 3:
        return 'Cumplice'
    elif contador == 2:
        return 'Suspeita'
    else:
        return 'Inocente'

# funcao para validar a resposta
def perg(pergunta):
    resposta = input(pergunta).lower()
    if resposta == 'sim':
        return True
    elif resposta == 'nao':
        return False
    else:
        print("Resposta invalida. Por favor, digite 'sim' ou 'não'.")
        return perg(pergunta)

#perguntas 
perguntas = [
    "Telefonou para a vitima?",
    "Esteve no local do crime?",
    "Mora perto da vitima?",
    "Devia para a vitima?",
    "Já trabalhou com a vitima?"
]

respostas = []
for pergunta in perguntas:
    respostas.append(perg(pergunta))

classificacao = classifica_participacao(respostas)
print(f'Você foi classificado como: {classificacao}')