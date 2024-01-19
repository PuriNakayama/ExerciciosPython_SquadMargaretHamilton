# usuario informa o numero de horas de exercicio por semana
hs_semana = float(input('Digite o numero de horas de exercicios fisico por semana: '))

# convertendo horas por semana para minutos em 4 semanas
min_semana = (hs_semana * 60) * 4


# calculo do total de calorias queimadas por mes
calorias_mes = min_semana  * 5

# imprimindo o resultado
print( f'O total de calorias queimadas por mes é: {calorias_mes}')