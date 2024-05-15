import os

def adicao(a,b):
    return (a + b)
def subtracao(a,b):
    return (a - b)
def multiplicacao(a,b):
    return (a * b)
def divisao(a,b):
    if b == 0:
        while b == 0:
            print("Não é possivel divisão por 0.")
            b = int(input("Informe novamente o segundo valor, deiferente de 0: "))
            if b != 0:
                divisao(a, b)
    return (a / b)

def calculadora(n1, n2, operacao):
    result = 0
    global operacao1
    if (operacao == "adicao") or (operacao == "+"):
        operacao1 = "Adição"
        result = adicao(n1, n2)
    elif (operacao == "subtracao") or (operacao == "-"):
        operacao1 = "Subtração"
        result = subtracao(n1, n2)
    elif (operacao == "multiplicacao") or (operacao == "*"):
        operacao1 = "Multiplicação"
        result = multiplicacao(n1, n2)
    elif (operacao == "divisao") or (operacao == "/"):
        operacao1 = "Divisão"
        result = divisao(n1, n2)
    return result


while True:
    os.system("cls")
    n1 = eval(input("informe o primeiro valor: "))
    operacao1 = input("Informe a operação (+, -, *, /): ")
    n2 = eval(input("Informe o segundo valor: "))

    resultado = calculadora(n1, n2, operacao1)
    print(f"O resultado da operação {operacao1} é: {resultado}")

    resposta = " "
    while resposta not in "SN":
        resposta = str(input("Deseja continuar no programa? [S/N]: ")).strip().upper()[0]
    if resposta == "N":
        break


print("\nObrigado, por usar nosso sistema!")
print("Volte sempre.")
