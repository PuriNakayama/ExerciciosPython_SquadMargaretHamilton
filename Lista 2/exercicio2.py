# usuario informa em qual turno ele estuda
turno = input('Qual turno você estuda? Digite M-matutino, V-vespertino ou N-noturno: ')

# condicao para determinar qual mensagem vai ser exibida
if turno.lower() == "m":
    print("Bom Dia!")
elif turno.lower() == "v":
    print("Boa Tarde!")
elif turno.lower() == "n":
    print("Boa Noite!")
else:
    print("Valor Inválido!")