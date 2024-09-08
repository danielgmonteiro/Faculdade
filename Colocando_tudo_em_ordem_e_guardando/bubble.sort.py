def bubbleSort(array):
    # Laço externo para iterar nos elementos do array
    for i in range(len(array)):
        # Laço interno para comparar elementos adjacentes
        for j in range(0, len(array) - i - 1):
            # Se o elemento atual é maior que o próximo, troque-os
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

# Declarar um array de números com 15 posições
array = [64, 34, 25, 12, 22, 11, 90, 88, 76, 45, 23, 67, 89, 54, 32]

# Aplicar o método bubbleSort no array
bubbleSort(array)

# Imprimir o array ordenado
print("Array ordenado:", array)
