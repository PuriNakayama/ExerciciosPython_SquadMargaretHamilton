import random
import re

palavras_chave = ['WomakersCode', 'python', 'django', 'sucesso', 'alegria']
palavra_secreta = random.choice(palavras_chave)
letras_corretas = '_' * len(palavra_secreta)
erros = 0

while '_' in letras_corretas and erros < 6:
    print('Palavra secreta:', letras_corretas)
    print('Erro:', erros)
    letra = input('Digite uma letra: ').lower()

    if letra in letras_corretas:
        print('Letra já foi digitada.')
        continue

    if letra in palavra_secreta:
        index = [i for i, letter in enumerate(palavra_secreta) if letter == letra]
        for i in index:
            letras_corretas = letras_corretas[:i] + letra + letras_corretas[i+1:]
    else:
        erros += 1

if '_' not in letras_corretas:
    print('Parabéns! Você adivinhou a palavra:', palavra_secreta)
else:
    print('Que pena! Você errou a palavra secreta:', palavra_secreta)