class SomarMultiplicar():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def somar(self):
        return self.a + self.b

    def multiplicar(self):
        return self.a * self.b

class derivada(SomarMultiplicar):
    def subtrair(self):
        return self.a - self.b
    
    def dividir(self):
        return self.a / self.b

d = derivada(10, 20)

print(f'A soma de A=10 e B=20 é {d.somar()}')