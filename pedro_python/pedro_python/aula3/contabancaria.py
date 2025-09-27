
class contabancaria:

    def __init__(self, saldo):
        self.saldo = saldo

    def depositar(self, valor):
        self.valor = self.saldo + valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo - valor
            return True
        else:
            return False
    
    def get_saldo(self):
        return self.saldo

contapedro = contabancaria(2000)

contapedro.sacar(100)
contapedro.depositar(80)

print(contapedro.get_saldo())
