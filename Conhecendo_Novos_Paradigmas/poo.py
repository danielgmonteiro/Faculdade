class pessoa:
    def __init__(self, nome, ender):
        self.set_nome(nome)
        self.set_ender(ender)

    def set_nome(self, nome):
        self.nome = nome

    def set_ender(self, ender):
        self.ender = ender

    def get_nome(self):
        return self.nome

    def get_ender(self):
        return self.ender

pessoa1 = pessoa("Maria", "Rua 01234")
pessoa2 = pessoa("João", "Rua 56789")

print(f'Nome: {pessoa1.get_nome()} \nEndereço: {pessoa1.get_ender()}')
print("=" * 40)
print(f'Nome: {pessoa2.get_nome()} \nEndereço: {pessoa2.get_ender()}')


