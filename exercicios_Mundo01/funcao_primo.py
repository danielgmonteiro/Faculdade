def ehprimo(num):
    cont = 0
    for i in range(1, num+1, 1):
        if (num % i == 0):
            cont = cont + 1
    return cont

num = 4
primo = ehprimo(num)
if primo == 2 :
    print(f"{num} É PRIMO")
else:
    print(f"{num} NÃO é primo")
