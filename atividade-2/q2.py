# Escreva uma função que receba uma lista de números e retorne outra lista
# com os números primos presentes.

def primo(lista):
    """
    Recebe uma lista de número inteiros
    Retorna uma nova lista contendo apenas os números primos.
    """

    lista_primo = []
    for i in lista:
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                lista_primo.append(i)

    return lista_primo


# Teste
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(primo(lista))
