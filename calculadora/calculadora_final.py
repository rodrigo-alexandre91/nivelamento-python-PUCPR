# Calculadora em Python
# calculadora funcional antes do TDD
# no arquivo calculadora_nova ela está refatorada mas sem função

import sys

print("\nxxxxxxxxxxxxxxx Calculadora Python xxxxxxxxxxxxxxx\n")
print("Selecione a operação desejada: \n")
print(" 1- Soma\n 2- Subtração\n 3- Multiplicação\n 4- Divisão\n")
print("OU 5 PARA SAIR\n")

'''Criar funções para as operações'''


def somar(arg1, arg2):
    return arg1 + arg2


def subtracao(arg1, arg2):
    return arg1 - arg2


def multpli(arg1, arg2):
    return arg1 * arg2


def divisao(arg1, arg2):
    return arg1 / arg2



while True:
    try:
        operacao = str(input("Digite sua opção (1 / 2 / 3 / 4 / 5): "))

        if int(operacao) in (1, 2, 3, 4):
            num1 = float(input("Digite o primeiro número: "))

            num2 = float(input("Digite o segundo número: "))

            if int(operacao) == 1:
                print(num1, "+", num2, "=", somar(num1, num2))
            elif int(operacao) == 2:
                print(num1, "-", num2, "=", subtracao(num1, num2))
            elif int(operacao) == 3:
                print(num1, "*", num2, "=", multpli(num1, num2))
            elif int(operacao) == 4:
                print(num1, "/", num2, "=", divisao(num1, num2))
            continue
    except:
        print("Opção Inválida, tente novamente!")
        continue
    else:
        if int(operacao) not in (1, 2, 3, 4):
            print("Opção Invalida! Digite uma opção valida dentre as abaixo: ")
            continue
        else:
            break