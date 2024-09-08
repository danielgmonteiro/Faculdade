# Abrir o arquivo e ler seu conteúdo
arquivo = open('loremipsum.txt', 'r')
conteudo = arquivo.read()
arquivo.close()

# Imprimir todo o conteúdo do arquivo
print("Conteúdo completo do arquivo:")
print(conteudo)

# Abrir o arquivo novamente para ler a primeira linha
arquivo = open('loremipsum.txt', 'r')
primeira_linha = arquivo.readline()
arquivo.close()

# Imprimir a primeira linha do arquivo
print("\nPrimeira linha do arquivo:")
print(primeira_linha)

# Abrir o arquivo novamente para ler os 3 primeiros caracteres
arquivo = open('loremipsum.txt', 'r')
tres_primeiros_caracteres = arquivo.read(3)
arquivo.close()

# Imprimir os 3 primeiros caracteres do arquivo
print("\nTrês primeiros caracteres do arquivo:")
print(tres_primeiros_caracteres)

# Utilizar a instrução "with" para abrir o arquivo e imprimir seu conteúdo
print("\nConteúdo do arquivo usando 'with':")
with open('loremipsum.txt', 'r') as arquivo:
    conteudo_with = arquivo.read()
    print(conteudo_with)
