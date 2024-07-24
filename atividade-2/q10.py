# Utilizando pandas, como lidar com valores ausentes (NaN) em um
# DataFrame?

import pandas as pd

# Lendo arquivo CSV
dados = pd.read_csv('meu_arquivo.csv')

# Verificando a quantidade de valores ausentes por coluna
print(dados.isnull().sum())

# Excluir linhas com valores ausentes na coluna "Coluna 4"
dados.dropna(subset=["Coluna 4"], inplace=True)

# Preencher valores ausentes da coluna "Coluna 5" com a mediana
dados["Coluna 5"].fillna(dados["Coluna 5"].median(), inplace=True)

# Excluir colunas com mais de 20% de valores ausentes
dados.drop(columns=dados.columns[dados.isnull().sum() / len(dados) > 0.2], inplace=True)

# Existem diferentes métodos e cada um se aplica em cada caso de forma específica. 