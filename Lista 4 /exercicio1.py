# funcao para concatenar os tres argumentos
def concatena_tres_argumentos(str1, str2,str3):
    return str1 + " " + str2 + " " + str3

# usuario insere os tres argumentos
argumento1 = input('Informe o primeiro argumento: ')
argumento2 = input('Informe o segundo argumento: ')
argumento3 = input('Informe o terceiro argumento: ')

# Concatenate the three strings
concatenacao = concatena_tres_argumentos(argumento1, argumento2, argumento3)

# Display the concatenated string to the user
print(f'As três justificativas concatenadas são: {concatenacao}' )