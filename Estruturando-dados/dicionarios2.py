pessoas =  {
    1: {"nome": "Maria", "idade": 26, "nacionalidade": "brasileira"}
}

pessoas.update({2: {"nome": "Adirana", "idade": 29, "nacionalidade": "brasileira"}})
print(f"Pessoas:\n{pessoas}")

novas_pessoas = pessoas.copy()
print(f"Novas pessoas:\n{novas_pessoas}")

pessoas.pop(1)
print(f"Pessoas:\n{pessoas}")

novas_pessoas.popitem()
print(f"Novas Pessoas:\n{novas_pessoas}")

pessoas.clear()
novas_pessoas.clear()
print(f"Pessoas:\n{pessoas}")
print(f"Novas Pessoas:\n{novas_pessoas}")

novo_dicionario = dict.fromkeys([10, 20, 30], "valor padrao")
print(f"Novo dicionário:\n{novo_dicionario}")
print(f"Novo dicionário/Itens:\n{novo_dicionario.items()}")
print(f"Novo dicionário/Chaves:\n{novo_dicionario.keys()}")
print(f"Novo dicionário/Valores:\n{novo_dicionario.values()}")