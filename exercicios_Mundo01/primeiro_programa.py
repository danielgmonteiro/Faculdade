peso = eval(input("Informe o seu peso: "))
altura = eval(input("Informe sua altura: "))
imc = peso/(altura**2)
print(f'Seu IMC é {imc:5.5}')