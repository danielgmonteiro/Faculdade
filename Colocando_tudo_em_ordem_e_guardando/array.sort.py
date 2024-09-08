import random

# Crie um array de 15 posições com números inteiros e valores aleatórios, não ordenados
array_inteiros = [random.randint(1, 100) for _ in range(15)]
print("Array original:", array_inteiros)

# Realize a ordenação dos dados do array utilizando o método “sort”
array_inteiros.sort()
print("Array ordenado (crescente):", array_inteiros)

# Ordene, de forma decrescente, os valores constantes no array
array_inteiros.sort(reverse=True)
print("Array ordenado (decrescente):", array_inteiros)

# Crie um array de strings
array_strings = ["nome", "dataNascimento", "cpf", "rg"]
print("\nArray de strings original:", array_strings)

# Ordene o array de strings de forma crescente
array_strings.sort()
print("Array de strings ordenado (crescente):", array_strings)

# Ordene o array de strings de forma decrescente
array_strings.sort(reverse=True)
print("Array de strings ordenado (decrescente):", array_strings)
