# Abra um arquivo de texto, ainda não existente, chamado “texto.txt” e o atribua a uma variável
arquivo = open('texto.txt', 'w')

# Crie uma lista usando a sintaxe: texto = list()
texto = list()

# Utilizando o método “append”, atribua algumas frases para a lista
texto.append("Esta é a primeira linha do arquivo.\n")
texto.append("Esta é a segunda linha do arquivo.\n")
texto.append("Esta é a terceira linha do arquivo.\n")

# Escreva, no arquivo aberto, o conteúdo da lista
for linha in texto:
    arquivo.write(linha)

# Feche o arquivo
arquivo.close()

# Imprima uma mensagem de confirmação
print("Arquivo 'texto.txt' criado e escrito com sucesso.")
