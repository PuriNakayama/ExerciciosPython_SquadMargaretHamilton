# usuario informa a distância da viagem
distancia = float(input("Digite a distância da viagem em km: "))

# calculo do tempo de viagem em cada meio de transporte
tempo_aviao = distancia / 600
tempo_carro = distancia / 100
tempo_onibus = distancia / 80

# funcao para converter tempo de horas e minutos
def converter_tempo(tempo):
    horas = int(tempo)
    minutos = int((tempo - horas) * 60)
    return horas, minutos

tempo_aviao_conv = converter_tempo(tempo_aviao)
tempo_carro_conv = converter_tempo(tempo_carro)
tempo_onibus_conv = converter_tempo(tempo_onibus)

# Imprimindo os resultados
print("Tempo de viagem por avião: ", tempo_aviao_h_m[0], "horas e", tempo_aviao_h_m[1], "minutos")
print("Tempo de viagem no carro: ", tempo_carro_h_m[0], "horas e", tempo_carro_h_m[1], "minutos")
print("Tempo de viagem no ônibus: ", tempo_onibus_h_m[0], "horas e", tempo_onibus_h_m[1], "minutos")