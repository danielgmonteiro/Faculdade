# Estratégia 01
def soma_par(lista):
    soma = 0
    for item in lista:
        if (item % 2 == 0):
            soma += item
    return soma

lista_01 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
soma = soma_par(lista_01)
print(f"A soma dos elementos pares da lista é {soma}")

# Estratégia 02

def ehpar(lista):
    r = (lista % 2 == 0)
    return r

def soma_par_02(lista):
    soma = 0
    for item in lista:
        if ehpar(item):
            soma+= item
    return soma
print("-----------------------------")
print(f"A soma do valore PARES é: {soma_par_02(lista_01)}")