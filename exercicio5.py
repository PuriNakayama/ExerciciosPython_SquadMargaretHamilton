#funcao para calcular o salario minimo
def calcular_sal_liquido(sal_bruto):
    if sal_bruto <= 1903.98:
        desconto = 0
    elif sal_bruto <= 2826.65:
        desconto = sal_bruto * 0.075
    elif sal_bruto <= 3751.05:
        desconto = sal_bruto * 0.15
    elif sal_bruto <= 4664.68:
        desconto = sal_bruto * 0.225
    else:
        desconto = sal_bruto * 0.275
    sal_liquido = sal_bruto - desconto
    return sal_liquido

#usuario informa o salario bruto
sal_bruto = float(input('Informe o salário bruto: '))
sal_liquido = calcular_sal_liquido(sal_bruto)
print( f'O salário líquido é:{sal_liquido:,.2f} ') 