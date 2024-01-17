#funcao para exibir a mensagem
def exibir_mensagem(nome, defeito, qualidade, positividade):
    print( f'Oi {nome}, prazer em te conhecer. Voce eh mais que {defeito}, voce eh {qualidade},sinta-se abracada {positividade}. Eu vejo a perfeicao em nossas falhas' )

#usuario escreve 
nome = str(input('Se apresente: '))
defeito = str(input('Fale algo que te incomoda: '))
qualidade = str(input('Escreva uma qualidade: '))
positividade = str(input('Escreva algo bom para outra mulher: '))


exibir_mensagem(nome, defeito, qualidade, positividade)