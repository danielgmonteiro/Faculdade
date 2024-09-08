# Crie um array e o popule com 15 números inteiros, sem nenhuma ordenação
array = [64, 25, 12, 22, 11, 90, 88, 76, 45, 23, 67, 89, 54, 32, 19]

# Método de ordenação Selection Sort
def selectionSort(array):
    # Laço externo para iterar nos elementos do array
    for i in range(len(array)):
        # Variável que recebe a variável "i"
        min_idx = i
        # Laço interno para iterar no range entre a posição "i + 1" e o tamanho total do array
        for j in range(i + 1, len(array)):
            # Verifica se o valor do elemento na posição "min_idx" é maior que o valor do elemento na posição "j"
            if array[min_idx] > array[j]:
                min_idx = j
        # Troca os valores do array
        array[i], array[min_idx] = array[min_idx], array[i]

# Aplique o método selectionSort no array
selectionSort(array)

# Imprima o array ordenado
print("Array ordenado:", array)
