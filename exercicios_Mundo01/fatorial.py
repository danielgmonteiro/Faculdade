# Estratégia 01
def fatorial(num):
    result = 1
    for i in range (num, 0, -1):
        result *= i
    return result

# Estratégia 02 - Recursividade
def fatorial_resursivo(num):
    if (num == 0) or (num == 1):
        return 1
    return num*fatorial_resursivo(num - 1)

numero = int(input("Digite um valor inteiro: "))

print(f"{numero}! = {fatorial(numero)}")
print("----------------------------------------")
print(f"{numero}! = {fatorial_resursivo(numero)}")
