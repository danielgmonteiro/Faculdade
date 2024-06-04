import os

def adicao(a, b):
    """
    Realiza a adição entre dois números.

    Args:
        a (float): O primeiro número.
        b (float): O segundo número.

    Returns:
        float: O resultado da adição.
    """
    return a + b

def subtracao(a, b):
    """
    Realiza a subtração entre dois números.

    Args:
        a (float): O primeiro número.
        b (float): O segundo número.

    Returns:
        float: O resultado da subtração.
    """
    return a - b

def multiplicacao(a, b):
    """
    Realiza a multiplicação entre dois números.

    Args:
        a (float): O primeiro número.
        b (float): O segundo número.

    Returns:
        float: O resultado da multiplicação.
    """
    return a * b

def divisao(a, b):
    """
    Realiza a divisão entre dois números.

    Args:
        a (float): O primeiro número.
        b (float): O segundo número (não pode ser zero).

    Returns:
        float: O resultado da divisão.
    """
    if b == 0:
        while b == 0:
            print("Não é possível divisão por 0.")
            b = int(input("Informe novamente o segundo valor, diferente de 0: "))
            if b != 0:
                return divisao(a, b)
    return a / b

def calculadora(n1, n2, operacao):
    """
    Calcula o resultado de uma operação matemática.

    Args:
        n1 (float): O primeiro número.
        n2 (float): O segundo número.
        operacao (str): A operação desejada ("adicao", "subtracao", "multiplicacao" ou "divisao").

    Returns:
        float: O resultado da operação.
    """
    result = 0
    global operacao1
    if operacao in ("adicao", "+"):
        operacao1 = "Adição"
        result = adicao(n1, n2)
    elif operacao in ("subtracao", "-"):
        operacao1 = "Subtração"
        result = subtracao(n1, n2)
    elif operacao in ("multiplicacao", "*"):
        operacao1 = "Multiplicação"
        result = multiplicacao(n1, n2)
    elif operacao in ("divisao", "/"):
        operacao1 = "Divisão"
        result = divisao(n1, n2)
    return result

    """
    Programa principal para interagir com a calculadora.

    Solicita os números e a operação ao usuário e imprime o resultado.
    """
while True:
    os.system("cls")
    n1 = eval(input("Informe o primeiro valor: "))
    operacao1 = input("Informe a operação (+, -, *, /): ")
    n2 = eval(input("Informe o segundo valor: "))

    resultado = calculadora(n1, n2, operacao1)
    print(f"O resultado da operação {operacao1} é: {resultado}")

    resposta = " "
    while resposta not in "SN":
        resposta = str(input("Deseja continuar no programa? [S/N]: ")).strip().upper()[0]
    if resposta == "N":
        break

print("\nObrigado por usar nosso sistema!")
print("Volte sempre.")

