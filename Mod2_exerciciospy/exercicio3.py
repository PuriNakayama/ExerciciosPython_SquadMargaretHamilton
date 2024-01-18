# Solicite ao usuário que informe uma nota entre zero e dez
nota = None
while nota is None:
    nota = float(input("Por favor, informe uma nota entre zero e dez: "))
    if nota < 0 or nota > 10:
        print("Nota inválida!")
        nota = None

# Exiba uma mensagem de sucesso
print("Nota válida informada!")