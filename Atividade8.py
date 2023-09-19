class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        desconto = self.preco * (percentual / 100)
        return self.preco - desconto


class Livro(Produto):
    def __init__(self, nome, preco, autor):
        super().__init__(nome, preco)
        self.autor = autor

    def desconto(self, percentual):
        desconto_geral = super().desconto(percentual)
        desconto_adicional = desconto_geral * 0.10
        return desconto_geral - desconto_adicional


class Jogo(Produto):
    def __init__(self, nome, preco, plataforma):
        super().__init__(nome, preco)
        self.plataforma = plataforma


# Exemplo de uso das classes
produto = Produto("Produto Genérico", 100)
print(f"Preço com desconto: R${produto.desconto(20):.2f}")

livro = Livro("Dom Casmurro", 50, "Machado de Assis")
print(f"Preço do livro com desconto: R${livro.desconto(15):.2f}")

jogo = Jogo("The Witcher 3", 60, "PC")
print(f"Preço do jogo: R${jogo.preco:.2f}")