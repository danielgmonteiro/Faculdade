qtd = int(input("Informe a quantidade: "))
if qtd < 10:
    print(f"O valor a pagar é: {qtd} UN x R$10.00 = R${qtd*10}")
elif qtd > 20:
    print(f"Hove um desconto de 20% \nO valor a pagar é: {qtd} UN x R$10.00 = R${qtd * 10 * 0.8}")
else:
    print(f"Hove um desconto de 10% \nO valor a pagar é: {qtd} UN x R$10.00 = R${qtd * 10 * 0.9}")
