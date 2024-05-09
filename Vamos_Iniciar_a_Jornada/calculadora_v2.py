saida = ""

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
    if (operacao == "adicao") or (operacao == "+"):
        result = adicao(n1, n2)
    elif (operacao == "subtracao") or (operacao == "-"):
        result = subtracao(n1, n2)
    elif (operacao == "multiplicacao") or (operacao == "*"):
        result = multiplicacao(n1, n2)
    elif (operacao == "divisao") or (operacao == "/"):
        result = divisao(n1, n2)
    return result

resposta = ""
while resposta != "n":
    n1 = eval(input("informe o primeiro valor: "))
    operacao1 = input("Informe a operação: ")
    n2 = eval(input("Informe o segundo valor: "))

    resultado = calculadora(n1, n2, operacao1)
    print(f"O resultado da operação {operacao1} é: {resultado}")

    resposta = input("Deseja continuar no programa? S/N: ")

    if (resposta.lower() == "n") or (resposta.lower() == "nao") or (resposta.lower() == "Não"):
        print("Obrigado, por usar nosso sistema!")
        print("Volte sempre.")
        break
    elif (resposta.lower() == "s") or (resposta.lower() == "sim"):
       continue
    else:
        resposta = input(("Resposta INCORRETA. Deseja continuar no programa? S/N: "))