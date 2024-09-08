from datetime import date

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    # Um método de classe para criar
    # um objeto pessoa atravé do ano de nascimento
    @classmethod
    def apartirAnoNasciment(cls, nome, ano):
        return cls(nome, date.today().year - ano)
    # Método Estático: Verificar se é maior de idade
    @staticmethod
    def ehMaiorIdade(idade):
        return idade >= 18

pessoa1 = Pessoa("Maria", 26)
pessoa2 = Pessoa.apartirAnoNasciment("Daniel", 1980)
# Imprimir o resultado
print(pessoa1.idade)
print(pessoa2.idade)
print(Pessoa.ehMaiorIdade(17))
print(Pessoa.ehMaiorIdade(pessoa2.idade))