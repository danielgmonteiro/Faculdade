class Conta:
    def __init__(self, numero, cpf, nomeTitular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            return True

    def gerarExtrato(self):
        print(f'Número da conta: {self.numero}\nCPF do Titular: {self.cpf}\nSaldo: {self.saldo}')

    def tranfereValor(self, contaDestino, valor):
        if self.saldo < valor:
            return "Saldo INSUFICIENTE!"
        else:
            contaDestino.depositar(valor)
            self.saldo -= valor
            return "Transferência Realizada com SUCESSO!"

def main():
    c1 = Conta(1, 1,"João", 0) # Objeto sendo INSTANCIADO
    print("=" * 30)
    print(f'Nome do titular da conta: {c1.nomeTitular}')
    print("*" * 30)
    print(f'Número da conta: {c1.numero}')
    print(f'CPF do titular da conta: {c1.cpf}')
    print("=" * 30)
    print(f'Saldo da conta: {c1.saldo}')
    print("="*30)
    c1.depositar(300)
    c1.sacar(100)
    c1.gerarExtrato()
    print("=" * 30)
    saque = c1.sacar(400)
    c1.gerarExtrato()
    print(f'Saque foi realizado? {"SIM" if saque == True else "NÃO"}')


''' Quando um script python é executado, a variável reservada
    NAME referente a ele tem o valor igual a "__main__" .
    Nesse caso, a condição IF a seguir será TRUE. Então o que 
    está no corpo do IF será executado. No caso, é um chamado ao
    método main do script. '''

if __name__ == "__main__":
    main()