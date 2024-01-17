from datetime import datetime
# obtem a data de nascimento do usuario
ano_nascimento = int(input('Informe o ano de nascimento: '))
mes_nascimento = int(input('Digite o mês de nascimento: '))
dia_nascimento = int(input('Digite o dia do nascimento: '))

# calcula a idade atual em anos
idade_atual = datetime.now().year - ano_nascimento

# Calcula a idade atual em meses
if datetime.now().month < mes_nascimento:
    idade_atual -= 1
    meses_atual = (datetime.now().month + 12) - mes_nascimento
else:
    meses_atual = datetime.now().month - mes_nascimento

#Resultado a idade atual e meses
print( f'A idade atual é: ', idade_atual, 'anos e', meses_atual, 'meses')