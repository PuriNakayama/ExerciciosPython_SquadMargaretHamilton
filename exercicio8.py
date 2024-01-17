# Funcao que calcula o pagamento
def calcula_pag(hs_trabalhada, hs_paga):
    total_pag = hs_trabalhada * hs_paga
    return total_pag

# usuario informa o numero de horas trabalhadas
hs_trabalhada = float(input('Digite o numero de horas trabalhadas no mes: '))

#usuario informa o valor da horas trabalhadas
hs_paga = float(input('Digite o valor / hora: '))

# Calcula o total do salario
total_sal = calcula_pag(hs_trabalhada, hs_paga)

# Resultado do salario total
print ( f'Salario total: {total_sal}' )