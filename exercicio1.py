def menu(): # vai ser chamado na condicao while
    print('Operacoes basicas matematicas: ')
    print('1 - Soma')
    print('2 - Subtracao')
    print('3 - Multiplicacao')
    print('4 - Divisao')
    
    
def soma(num1,num2): # funcao soma
    return num1+num2
    
def subtracao(num1,num2): # funcao subtracao
    return num1-num2

def multiplicacao(num1,num2): #funcao multiplicacao
    return num1*num2

def divisao(num1,num2): #funcao divisao
    return num1/num2
    
 #usuario insere os valores 
number1 = float(input('Digite o primeiro numero: '))
number2 = float(input('Digite o segundo numero: '))


while True: #condicao, enquanto o usuario digitar um numero, o codigo roda
    menu()
    opcao = int(input('Escolha apenas uma opção de 1 a 4 (ou 0 para sair): ')) #condicao para sair do codigo
    if opcao == 0: #se o usuario digitar 0, encerra o codigo
        break
    elif opcao == 1: #senao continua rodando
        print('Resultado da soma:', soma(number1, number2)) #resultado da soma
    elif opcao == 2:
        print('Resultado da subtração:', subtracao(number1, number2)) #resultado da subtracao
    elif opcao == 3:
        print('Resultado da multiplicação:', multiplicacao(number1, number2)) # resultado da multiplicacao
    elif opcao == 4:
        if number2 == 0: # #verificacao se o usuario digita 0 
            print('Não é possível realizar a divisão por zero.') 
        else:
            print('Resultado da divisão:', divisao(number1, number2)) #resultado da divisao
    else:
        print('Opção inválida. Tente novamente.') #Mensagem de opcao invalida