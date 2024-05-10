meu_dicionario = {
    1 : {"linguagem": "Python"},
    2 : {"linguagem": "Java"},
    3 : {"linguagem": "PHP"}
}
print(meu_dicionario)
valor_linguagem = dict()
for e in meu_dicionario:
    #valor_linguagem.update(meu_dicionario[e].get("linguagem"))
    valor = meu_dicionario[e].get("linguagem")
    valor_linguagem[e] = "linguagem"
print(valor_linguagem)
print(type(meu_dicionario))

dicionario_rutas = dict()
dicionario_frutas = {
    1: {"nome": "limão", "tipo": "ácida"},
    2: {"nome": "laranja", "tipo": "ácida"},
    3: {"nome": "manga", "tipo": "semiácida"},
    4: {"nome": "maça", "tipo": "semiácida"},
    5: {"nome": "banana", "tipo": "doce"},
    6: {"nome": "mamão", "tipo": "doce"}
}




