from clientes import Cliente
from contas2 import Conta

cliente1 = Cliente("123.456.789-00","João", "Rua 1")
cliente2 = Cliente("789.456.123-00", "Maria", "Rua 2")
conta1 = Conta([cliente1, cliente2], 1, 0)
conta1.gerarSaldo([cliente1.nome, cliente2.nome])
conta1.depositar(1500)
conta1.sacar(500)
print("\n")
conta1.gerarSaldo([cliente1.nome, cliente2.nome])
cliente3 = Cliente("801.931.286.15", "Daniel Monteiro", "Calçada das Quintãs, 251B")
cliente4 = Cliente("753.258.454-05", "Adriana Monteiro", "Calçada das Quintãs, 251B")
conta2 = Conta([cliente3, cliente4], 2, 245000000.00)
print("\n")
conta2.gerarSaldo([cliente3.nome, cliente4.nome])
conta1.trasfereValor(conta2, 320.50)
conta1.extrato.extrato(1)
conta2.extrato.extrato(2)