class Veiculo:
    def __init__(self, cor, preco):
        self.cor = cor
        self.preco = preco

    def detalhes(self):
        return f"Cor: {self.cor}\nPreço: R${self.preco:.2f}"


class Carro(Veiculo):
    def __init__(self, cor, preco, numero_portas):
        super().__init__(cor, preco)
        self.numero_portas = numero_portas

    def detalhes(self):
        return f"{super().detalhes()}\nNúmero de Portas: {self.numero_portas}"


class Bicicleta(Veiculo):
    def __init__(self, cor, preco, tipo):
        super().__init__(cor, preco)
        self.tipo = tipo

    def detalhes(self):
        return f"{super().detalhes()}\nTipo: {self.tipo} bicicleta"


# Exemplo de uso das classes
carro = Carro("Azul", 45000, 4)
bicicleta = Bicicleta("Vermelha", 1500, "montanha")

print("Detalhes do Carro:")
print(carro.detalhes())

print("\nDetalhes da Bicicleta:")
print(bicicleta.detalhes())