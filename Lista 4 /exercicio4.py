#funcao para conversao reais em dolar
def converter_reais_dolar(qtd_reais):
    taxa_conversao = 4.91 # taxa d conversao real para dolar 
    dolar = round(qtd_reais * taxa_conversao, 2)
    return dolar

#funcao para conversao reais em peso
def converter_reais_peso(qtd_reais):
    taxa_conversao = 0.02 # taxa d conversao real para peso 
    peso = round(qtd_reais * taxa_conversao, 2)
    return peso

#funcao para conversao reais em dolar australiano
def converter_reais_dolar_au(qtd_reais):
    taxa_conversao = 3.18 # taxa d conversao real para dolar australiano
    dolar_au = round(qtd_reais * taxa_conversao, 2)
    return dolar_au

#funcao para conversao reais em dolar canadense
def converter_reais_dolar_can(qtd_reais):
    taxa_conversao = 3.64 # taxa d conversao real para dolar canadense
    dolar_canadense = round(qtd_reais * taxa_conversao, 2)
    return dolar_canadense

#funcao para conversao reais em franco suico
def converter_reais_franco(qtd_reais):
    taxa_conversao = 0.42 # taxa d conversao real para franco 
    franco_suico = round(qtd_reais * taxa_conversao, 2)
    return franco_suico

#funcao para conversao reais em euro
def converter_reais_euro(qtd_reais):
    taxa_conversao = 5.36 # taxa d conversao real para euro 
    euro = round(qtd_reais * taxa_conversao, 2)
    return euro

#funcao para conversao reais em libra
def converter_reais_libra(qtd_reais):
    taxa_conversao = 6.21 # taxa d conversao real para libra esterlina 
    libra = round(qtd_reais * taxa_conversao, 2)
    return libra

def main():
    qtd_reais = float(input('Digite o valor em Reais:R$'))

    dolar = converter_reais_dolar(qtd_reais)
    peso = converter_reais_peso(qtd_reais)
    dolar_au = converter_reais_dolar_au(qtd_reais)
    dolar_can = converter_reais_dolar_can(qtd_reais)
    franco_suico = converter_reais_franco(qtd_reais)
    euro = converter_reais_euro(qtd_reais)
    libra = converter_reais_libra(qtd_reais)
    

    print(f"R${qtd_reais} Reais equivale a: \nUSD {dolar} \nARS {peso} \nAUD {dolar_au} \nCAD {dolar_can} \nCHF{franco_suico} \nEUR {euro} \nGBP {libra} ")

if __name__ == "__main__":
    main()