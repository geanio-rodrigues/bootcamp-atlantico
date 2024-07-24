# Utilizando pandas, como selecionar uma coluna específica e filtrar linhas
# em um “DataFrame” com base em uma condição?

import pandas as pd

# Lendo arquivo CSV
dados = pd.read_csv("meu_arquivo.csv")

# Selecionando uma coluna
coluna2 = dados["Coluna 2"]

# Filtrando linhas com informações especificas
dados_filtrados = dados[["Coluna 1", "Coluna 3"]][coluna2 != 'Dado 8,2']

# Exibindo primeiras linhas do Dataframe filtrado
print(dados_filtrados.head())
