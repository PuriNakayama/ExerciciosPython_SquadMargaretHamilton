#funcao para calcular o consumo de combustivel por km 
def calcular_consumo():
    while True:
        try:
            litros_combustivel = float(input('Digite a quantidade de litros de combustivel consumidos: '))
            distancia_percorrida = float(input('Digite a distancia percorrida em km: '))
            if litros_combustivel > 0 and distancia_percorrida > 0:
                consumo_medio = distancia_percorrida / litros_combustivel
                print(f"O consumo médio em km/l é: {consumo_medio}")
                break
            else:
                print("Por favor, digite numeros positivos.")
        except ValueError:
            print("Por favor, digite numeros.")

calcular_consumo()