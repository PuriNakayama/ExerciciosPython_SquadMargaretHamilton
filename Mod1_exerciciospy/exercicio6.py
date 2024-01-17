# usuario informa a distância da viagem
distancia = float(input('Digite a distância da viagem em km: '))

# Tempo de viagem em cada meio de transporte
tempo_aviao = distancia / 600
tempo_carro = distancia / 100
tempo_onibus = distancia / 80

# Converte o tempo de horas e minutos
def converte_tempo(tempo):
    horas = int(tempo)
    minutos = int((tempo - horas) * 60)
    return horas, minutos

tempo_aviao_conv = converte_tempo(tempo_aviao)
tempo_carro_conv = converte_tempo(tempo_carro)
tempo_onibus_conv = converte_tempo(tempo_onibus)

# os resultados serao
print( f'Tempo de viagem por avião: ', tempo_aviao_conv[0], 'horas e', tempo_aviao_conv[1], 'minutos')
print( f'Tempo de viagem no carro: ',  tempo_carro_conv[0], 'horas e',tempo_carro_conv[1], 'minutos')
print( f'Tempo de viagem no ônibus: ', tempo_onibus_conv[0], 'horas e', tempo_onibus_conv[1], 'minutos')