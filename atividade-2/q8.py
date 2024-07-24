# Utilizando pandas, como realizar a leitura de um arquivo CSV em um
# DataFrame e exibir as primeiras linhas?

import pandas as pd

# Lendo o aquivo CSV em um DataFrame
dados = pd.read_csv('meu_arquivo.csv')

# Exibindo as primeiras linhas
print(dados.head())
