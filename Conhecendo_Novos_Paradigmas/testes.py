from conta import Conta

# O código a baixo é válido, foi executado testes e depois foi tranformado em comentário para mais testes
'''conta1 = Conta(1, 123, "João", 0)
conta2 = Conta(3, 456, "Marta", 0)

if conta1 != conta2:
    print("Endereços diferentes na memória")

conta1 = conta2
if conta1 == conta2:
    print("Endereços iguais na memória")
print(conta1.cpf)
print(conta2.cpf)'''

conta1 = Conta(1, 123, "João", 0)
conta2 = Conta(3, 456, "Maria", 0)

print("=" * 30)
print(f'Nome do titular da conta: {conta1.nomeTitular}')
print("*" * 30)
print(f'Número da conta: {conta1.numero}')
print(f'CPF do titular da conta: {conta1.cpf}')
print("=" * 30)
print(f'Saldo da conta: {conta1.saldo}')
print("=" * 30)
print("\n")

conta1.depositar(1000)
print("=" * 30)
print(f'Nome do titular da conta: {conta1.nomeTitular}')
print("*" * 30)
print(f'Número da conta: {conta1.numero}')
print(f'CPF do titular da conta: {conta1.cpf}')
print("=" * 30)
print(f'Saldo da conta: {conta1.saldo}')
print("=" * 30)
print("\n")
conta1.tranfereValor(conta2, 500)

print("=" * 30)
print(f'Nome do titular da conta: {conta1.nomeTitular}')
print("*" * 30)
print(f'Número da conta: {conta1.numero}')
print(f'CPF do titular da conta: {conta1.cpf}')
print("=" * 30)
print(f'Saldo da conta: {conta1.saldo}')
print("=" * 30)
print("\n")
print("=" * 30)
print(f'Nome do titular da conta: {conta2.nomeTitular}')
print("*" * 30)
print(f'Número da conta: {conta2.numero}')
print(f'CPF do titular da conta: {conta2.cpf}')
print("=" * 30)
print(f'Saldo da conta: {conta2.saldo}')


