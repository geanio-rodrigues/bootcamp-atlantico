# Crie uma função que receba uma lista de tuplas, cada uma contendo o
# nome e a idade de uma pessoa, e retorne a lista ordenada pelo nome das
# pessoas em ordem alfabética.

def ordena_nome(lista):
    """
    Recebe uma lista de nomes
    Retorna uma nova lista contendo os nomes ordenados em ordem alfabética
    """

    lista_ordenada = lista.copy()  # Cria uma cópia da lista original
    lista_ordenada.sort(key=lambda x: x[0])  # A lista de tulplas será ordenada pelo primeiro valor em cada tupla
    return lista_ordenada


# Teste
lista = [("Bianca", 30), ("Alice", 25), ("Daniel", 28), ("Carlos", 20),
         ("José", 31), ("Abraão", 17)]
print(ordena_nome(lista))
