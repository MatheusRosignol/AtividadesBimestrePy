class Publicacao:
    def __init__(self, titulo, ano_publicacao):
        self.titulo = titulo
        self.ano_publicacao = ano_publicacao

    def descricao(self):
        return f"Título: {self.titulo}\nAno de Publicação: {self.ano_publicacao}"


class Livro(Publicacao):
    def __init__(self, titulo, ano_publicacao, autor, numero_paginas):
        super().__init__(titulo, ano_publicacao)
        self.autor = autor
        self.numero_paginas = numero_paginas

    def descricao(self):
        return f"{super().descricao()}\nAutor: {self.autor}\nNúmero de Páginas: {self.numero_paginas}"


class Revista(Publicacao):
    def __init__(self, titulo, ano_publicacao, editora, edicao):
        super().__init__(titulo, ano_publicacao)
        self.editora = editora
        self.edicao = edicao

    def descricao(self):
        return f"{super().descricao()}\nEditora: {self.editora}\nEdição: {self.edicao}"


# Exemplo de uso das classes
livro = Livro("Dom Casmurro", 1899, "Machado de Assis", 256)
revista = Revista("National Geographic", 2023, "NG Publishing", "Julho")

print("Descrição do Livro:")
print(livro.descricao())

print("\nDescrição da Revista:")
print(revista.descricao())