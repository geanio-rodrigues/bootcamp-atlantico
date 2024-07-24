# Dada uma lista de números inteiros, escreva uma função para encontrar o
# segundo maior valor na lista.

def segundo_maior(lista):
    """
    Recebe uma lista de números inteiros
    Retorna o segundo maior valor da lista
    """
    
    lista.sort()  # Ordena a lista em ordem crescente
    return lista[-2]  # Retorna o penúltimo valor da lista


# Teste
lista = [4, 1, 0, 8, 6, 12, 9]
print(segundo_maior(lista))
