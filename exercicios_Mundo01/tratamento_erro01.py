while True:
    try:
        n = eval(input("Digit um numemro: "))
        break
    except NameError:
        print("Informe um NAME válido.")
    except ValueError:
        print("Informe um Value válido.")

X = 1
Y = 2
Z = X
X = Y
Y = Z
print(X, Y)
