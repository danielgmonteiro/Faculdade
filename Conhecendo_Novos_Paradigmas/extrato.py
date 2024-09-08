class Extrato:
    def __init__(self):
        self.transacoes = []

    def extrato(self, numeroConta):
        print(f'\nExtrato: {numeroConta}')
        print("="*45)
        for p in self.transacoes:
            print(f'{p[0]:15s} {p[1]:10.2f}   {p[2]:7s} {p[3].strftime("%d/%m/%y")}')