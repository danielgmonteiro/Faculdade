import time

# Função Bubble Sort
def bubbleSort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

# Função Selection Sort
def selectionSort(array):
    n = len(array)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if array[j] < array[min_idx]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]

# Crie uma variável do tipo lista
palavras = list()

# Leia o conteúdo do arquivo "loremipsum.txt" e separe cada linha em palavras
with open('loremipsum.txt', 'r') as arquivo:
    for linha in arquivo:
        palavras.extend(linha.split())

# Ordenação usando Bubble Sort
palavras_bubble = palavras.copy()
inicio = time.time()
bubbleSort(palavras_bubble)
fim = time.time()
print("Bubble Sort:", palavras_bubble)
print("Tempo de execução (Bubble Sort):", fim - inicio, "segundos")

# Ordenação usando Selection Sort
palavras_selection = palavras.copy()
inicio = time.time()
selectionSort(palavras_selection)
fim = time.time()
print("Selection Sort:", palavras_selection)
print("Tempo de execução (Selection Sort):", fim - inicio, "segundos")

# Ordenação usando o método nativo sort()
palavras_sort = palavras.copy()
inicio = time.time()
palavras_sort.sort()
fim = time.time()
print("Método sort():", palavras_sort)
print("Tempo de execução (sort()):", fim - inicio, "segundos")

# Escolha o método de melhor performance e remova os demais
# Neste exemplo, vamos assumir que o método sort() foi o mais eficiente
with open('palavras_ordenadas.txt', 'w') as arquivo:
    for palavra in palavras_sort:
        arquivo.write(palavra + '\n')
