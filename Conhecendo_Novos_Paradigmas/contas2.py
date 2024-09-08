import datetime
from extrato import Extrato
class Conta:
    def __init__(self, clientes, numero, saldo):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo
        self.data_abertura = datetime.datetime.today()
        self.extrato = Extrato()
    def depositar(self, valor):
        self.saldo += valor
        self.extrato.transacoes.append(["DEPÓSITO", valor, "Data", datetime.datetime.today()])
    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            self.extrato.transacoes.append(["SAQUE", valor, "Data", datetime.datetime.today()])
            return True
    def trasfereValor(self, contaDestino, valor):
        if self.saldo < valor:
            return ("Saldo INSUFICIENTE!")
        else:
            contaDestino.depositar(valor)
            self.saldo -= valor
            self.extrato.transacoes.append(["TRANSFERÊNCIA", valor, "Data", datetime.datetime.today()])
            return ("Transferencia realizada com sucesso!")
    def gerarSaldo(self, clienteConta):
        print("*"*30)
        print(f'Titular: {clienteConta}\nN. Conta: {self.numero}')
        print("="*30)
        print(f'Saldo: {self.saldo}')
        print("*" * 30)
nome = "Daniel"
nome.capitalize()