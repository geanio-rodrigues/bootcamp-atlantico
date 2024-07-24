# Utilizando pandas, como lidar com valores ausentes (NaN) em um
# DataFrame?

import pandas as pd

# Lendo arquivo CSV
dados = pd.read_csv('meu_arquivo.csv')

# Verificando a quantidade de valores ausentes por coluna
print(dados.isnull().sum())
