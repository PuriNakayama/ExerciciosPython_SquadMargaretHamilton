#funcao para contar as vogais
def contar_vogais(texto):
    vogais = "aeiou"
    total_vogais = 0

#condicao se o usuario digitar letras maiusculas, transforma em minuscula
    for letra in texto:
        if letra.lower() in vogais:
            total_vogais += 1

    return total_vogais

#usuario digita uma frase
texto = input('Digite uma frase: ')
#chama a funcao 
total_vogais = contar_vogais(texto)
#imprime o total de vogais
print(f'O total de vogais na frase é: {total_vogais}' )