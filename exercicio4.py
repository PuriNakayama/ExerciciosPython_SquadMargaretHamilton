def calc_consumo_medio(distancia_km, combustivel_consumido):
    consumo_medio =  distancia_km / combustivel_consumido
    return consumo_medio

distancia_km = float(input('Digite a quantidade de quilômetros: '))
combustivel_consumido = float(input('Informe a quantidade de litros de combustível consumido: '))

consumo_medio = calc_consumo_medio(distancia_km, combustivel_consumido)

print(f'O consumo médio em km/l é: {consumo_medio} litros')