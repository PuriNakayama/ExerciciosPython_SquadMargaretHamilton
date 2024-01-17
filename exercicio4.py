#funcao calcula o consumo medio de gasolina
def calc_consumo_medio(distancia_km, combustivel_consumido):
    consumo_medio =  distancia_km / combustivel_consumido    
    return consumo_medio

#informa o km e a quantidade de litros de combustivel
distancia_km = float(input('Digite a quantidade de quilômetros: '))
combustivel_consumido = float(input('Informe a quantidade de litros de combustível consumido: '))

consumo_medio = calc_consumo_medio(distancia_km, combustivel_consumido)

#retorna o consumo medio
print(f'O consumo médio em km/l é: {consumo_medio} litros')