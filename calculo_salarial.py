# Faça um Programa que pergunte quanto você ganha por hora e o
# número de horas trabalhadas no mês. Calcule e mostre o total
# do seu salário no referido mês, sabendo-se que são
# descontados 11% para o Imposto de Renda, 8% para
# o INSS e 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.

def ler_dados():
    valor_hora = float(input("Digite o valor hora: "))
    qtde_horas = float(input("Digite a quantidade de horas: "))
    return valor_hora, qtde_horas


def calcular_salario_bruto(valor_hora, qtde_horas):
    salario_bruto = valor_hora * qtde_horas
    return salario_bruto


def calcular_descontos(salario_bruto):
    desconto_ir = salario_bruto * 0.11
    desconto_inss = salario_bruto * 0.08
    desconto_sindicato = salario_bruto * 0.05
    return desconto_ir, desconto_inss, desconto_sindicato


def calcular_salario_liquido(
        salario_bruto,
        ir,
        inss,
        sindicato):
    return salario_bruto - (ir + inss + sindicato)


def mostrar_relatorio(salario_bruto, desconto_ir, desconto_inss, desconto_sindicato, salario_liquido):
    print(f" + Salário Bruto : R${salario_bruto:,.2f}")
    print(f" - IR (11%) : R${desconto_ir:,.2f}")
    print(f" - INSS (8%) : R${desconto_inss:,.2f}")
    print(f" - Sindicato ( 5%) : R${desconto_sindicato:,.2f}")
    print(f" = Salário Liquido : R${salario_liquido:,.2f}")


(valor_da_hora, qtde_de_horas) = ler_dados()

bruto = calcular_salario_bruto(valor_da_hora, qtde_de_horas)

(desc_ir, desc_inss, desc_sind) = calcular_descontos(bruto)

liquido = calcular_salario_liquido(bruto, desc_ir, desc_inss, desc_sind)

mostrar_relatorio(bruto, desc_ir, desc_inss, desc_sind, liquido)


