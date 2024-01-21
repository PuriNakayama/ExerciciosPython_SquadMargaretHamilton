# funcao para definir o menu
def menu():
    print('Selecione uma opção:')
    print('1. Celsius para Fahrenheit')
    print('2. Fahrenheit para Celsius')
    print('3. Sair')

# funcao de celsius para fahrenheit
def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

#funcao de fahrnheit para celsius 
def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

opcao = 0 
while opcao != 3: # condicao para verificar o menu
    menu()
    opcao = float(input('Informe o número da opção desejada: '))

    if opcao == 1:
        temperatura = float(input('Digite a temperatura em graus Celsius: '))
        conversao = celsius_para_fahrenheit(temperatura)
        print(f'{temperatura} graus Celsius é igual a {conversao} graus Fahrenheit.')
    elif opcao == 2:
        temperatura = float(input('Digite a temperatura em graus Fahrenheit: '))
        conversao = fahrenheit_para_celsius(temperatura)
        print(f'{temperatura} graus Fahrenheit é igual a {conversao} graus Celsius.')
    elif opcao == 3:
        print("Saindo...")
    else:
        print('Opção inválida. Tente novamente.')