# Inicialização da Biblioteca
biblioteca = [
    {"titulo": "Python Básico", "autor": "João Silva", "ano": 2021, "disponivel": True},
    {"titulo": "Algoritmos Avançados", "autor": "Maria Souza", "ano": 2019, "disponivel": True},
    {"titulo": "Machine Learning", "autor": "Carlos Pereira", "ano": 2020, "disponivel": True},
    {"titulo": "Data Science", "autor": "Ana Martins", "ano": 2018, "disponivel": True},
    {"titulo": "Deep Learning", "autor": "Pedro Alves", "ano": 2022, "disponivel": True}
]

# Função para Adicionar Livro
def adicionar_livro(titulo, autor, ano):
    for livro in biblioteca:
        if livro["titulo"].lower() == titulo.lower():
            print("Livro já existe na biblioteca.")
            return
    novo_livro = {"titulo": titulo, "autor": autor, "ano": ano, "disponivel": True}
    biblioteca.append(novo_livro)
    print("Livro adicionado com sucesso.")

# Função para Buscar Livro
def buscar_livro(titulo):
    for livro in biblioteca:
        if livro["titulo"].lower() == titulo.lower():
            print("Informações do livro:")
            print("Título:", livro["titulo"])
            print("Autor:", livro["autor"])
            print("Ano:", livro["ano"])
            print("Disponível:", "Sim" if livro["disponivel"] else "Não")
            return
    print("Livro não encontrado.")

# Função para Listar Livros
def listar_livros():
    print("Lista de Livros:")
    for livro in biblioteca:
        print("Título:", livro["titulo"])
        print("Autor:", livro["autor"])
        print("Ano:", livro["ano"])
        print("Disponível:", "Sim" if livro["disponivel"] else "Não")
        print("-------------------")

# Função para Emprestar Livro
def emprestar_livro(titulo):
    for livro in biblioteca:
        if livro["titulo"].lower() == titulo.lower():
            if livro["disponivel"]:
                livro["disponivel"] = False
                print("Livro emprestado com sucesso.")
            else:
                print("Livro já está emprestado.")
            return
    print("Livro não encontrado.")

# Função para Devolver Livro
def devolver_livro(titulo):
    for livro in biblioteca:
        if livro["titulo"].lower() == titulo.lower():
            if not livro["disponivel"]:
                livro["disponivel"] = True
                print("Livro devolvido com sucesso.")
            else:
                print("Este livro não está emprestado.")
            return
    print("Livro não encontrado.")

# Exemplo de uso das funções:
adicionar_livro("Introdução à Inteligência Artificial", "Fernanda Santos", 2023)
buscar_livro("Machine Learning")
listar_livros()
emprestar_livro("Data Science")
devolver_livro("Machine Learning")
listar_livros()