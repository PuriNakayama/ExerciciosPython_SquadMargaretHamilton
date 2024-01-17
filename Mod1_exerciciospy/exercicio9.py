# usuario informa o número de horas de exercício por semana
hs_semana = float(input('Digite o número de horas de exercícios fisico por semana: '))

# Convertendo horas por semana para minutos em 4 semanas
min_semana = (hs_semana * 60) * 4


# Cálculo do total de calorias queimadas por mês
calorias_mes = min_semana  * 5

# Imprimindo o resultado
print( f'O total de calorias queimadas por mês é: {calorias_mes}')