# o usuário informa o peso em kg
peso = float(input('Digite o seu peso em kilos: '))

# o usuario informa a altura em metros
altura = float(input('Digite a sua altura em metros: '))

# Calcula o Indice de Massa Corporal (IMC)
imc = peso / (altura * altura)

# Exibe o resultado do IMC
print( f'Seu Indice de Massa Corporal (IMC) é: {imc:,.2f}') 