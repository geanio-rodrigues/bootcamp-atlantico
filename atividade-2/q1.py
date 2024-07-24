# Escreva uma função que receba uma lista de números e retorne outra lista com os números ímpares

def impar(lista):
    """
    Recebe uma lista com números inteiros
    Retorna uma nova lista contendo apenas os números ímpares.
    """
    
    lista_impar = []
    for i in lista:
        if i % 2 != 0:
            lista_impar.append(i)
    
    return lista_impar


# Teste
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(impar(lista))
