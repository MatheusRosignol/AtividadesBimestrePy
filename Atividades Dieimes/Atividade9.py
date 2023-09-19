class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return True
        else:
            print("Saldo insuficiente")
            return False


class ContaPoupanca(ContaBancaria):
    def sacar(self, valor):
        if self.saldo >= valor + 2:
            self.saldo -= valor + 2
            return True
        else:
            print("Saldo insuficiente")
            return False


class ContaCorrente(ContaBancaria):
    def __init__(self, titular, saldo=0, limite=0):
        super().__init__(titular, saldo)
        self.limite = limite

    def sacar(self, valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            return True
        else:
            print("Saldo insuficiente")
            return False



conta_poupanca = ContaPoupanca("João")
conta_corrente = ContaCorrente("Maria", limite=1000)

conta_poupanca.depositar(500)
conta_poupanca.sacar(100)
print(f"Saldo da conta poupança: {conta_poupanca.saldo}")

conta_corrente.depositar(1500)
conta_corrente.sacar(1200)
print(f"Saldo da conta corrente: {conta_corrente.saldo}")