class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


class Pedido:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, produto, quantidade):
        self.itens.append((produto, quantidade))

    def calcular_total(self):
        total = 0
        for produto, quantidade in self.itens:
            total += produto.preco * quantidade
        return total


# Criando produtos
produto1 = Produto("Camiseta", 25.99)
produto2 = Produto("Calça Jeans", 49.99)

# Criando um pedido
meu_pedido = Pedido()
meu_pedido.adicionar_item(produto1, 2)
meu_pedido.adicionar_item(produto2, 1)

# Calculando o total do pedido
total_pedido = meu_pedido.calcular_total()
print(f"Total do Pedido: R${total_pedido:.2f}")