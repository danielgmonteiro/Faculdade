meu_dicionario = {
    1 : "Python",
    2 : "Java",
    3 : "PHP"
}
print(meu_dicionario)
print(type(meu_dicionario))
valor_linguagem = meu_dicionario.get(1)
print(f"Valor da chave 'Linguagem': {valor_linguagem}")

dicionario_frutas = dict()
print("\n")
dicionario_frutas = {
    1: {"nome": "limão", "tipo": "ácida"},
    2: {"nome": "laranja", "tipo": "ácida"},
    3: {"nome": "manga", "tipo": "semiácida"},
    4: {"nome": "maça", "tipo": "semiácida"},
    5: {"nome": "banana", "tipo": "doce"},
    6: {"nome": "mamão", "tipo": "doce"}
}
print(f"Chave 1:\nNome: {dicionario_frutas[1]['nome']}\nTipo: {dicionario_frutas[1]['tipo']}\n")

print(f"Chave 2:\nNome: {dicionario_frutas[2]['nome']}\nTipo: {dicionario_frutas[2]['tipo']}\n")
