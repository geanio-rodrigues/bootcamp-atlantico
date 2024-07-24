# Escreva uma função que receba duas listas e retorne outra lista com os
# elementos que estão presentes em apenas uma das listas.

def diff(lista1, lista2):
    """
    Recebe duas listas
    Retorna uma nova lista contendo apenas os elementos diferentes entre as listas
    """

    lista_diff = []
    for i in lista1:
        if i not in lista2:
            lista_diff.append(i)

    for i in lista2:
        if i not in lista1:
            lista_diff.append(i)
        
    return lista_diff


# Teste
lista1 = [1, 2, 3, 4, 5]
lista2 = [3, 4, 5, 6, 7]
print(diff(lista1, lista2))

# Teste 2
lista3 = ["a", "b", "c", "d", "e"]
lista4 = ["a", "e", "i", "o", "u"]
print(diff(lista1, lista2))
