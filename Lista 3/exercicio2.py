#funcao para calcular a media das notas 
def calcular_media(notas):
    media = sum(notas) / len(notas)
    return media

#funcao para obter as notas dos cincos alunos 
def obter_notas():
    notas = []
    for i in range(1, 5):
        nota = float(input(f"Insira a nota {i} do aluno: "))
        notas.append(nota)
    return notas

notas_alunos = []
for i in range(1, 6): #condicao que mostra qual aluno esta inserindo a nota 
    print(f"Insira as notas do aluno {i} ")
    notas_alunos.append(obter_notas())

alunos_aprovados = 0

for notas in notas_alunos: #condicao para verificar quais alunos tem notas maior ou igual a 7
    media = calcular_media(notas)
    if media >= 7.0:
        alunos_aprovados += 1

print("Número de alunos aprovados: ", alunos_aprovados)