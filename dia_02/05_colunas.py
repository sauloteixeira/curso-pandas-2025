#%%

import pandas as pd

df = pd.read_csv("../data/transacoes.csv", sep=";")

#%%
df.shape

#%%
df.head(n=5)

#%%

df.info(memory_usage="deep")

#%%
df.dtypes

#%%
#criando um novo dataframe com nomes de colunas trocados

# df2 = df.rename(columns={
#                             "QtdePontos": "QtPontos",
#                             "DescSistemaOrigem": "SistemaOrigem"
#                         })
# 
# df2.info(memory_usage="deep")

#%%
#alterando o nome das colunas no proprio dataframe

renamed_coluns = {
                    "QtdePontos": "QtPontos",
                    "DescSistemaOrigem": "SistemaOrigem"
                }

df.rename(columns=renamed_coluns, inplace=True)
df.info(memory_usage="deep")

#%%
colunas = ["IdCliente", "QtPontos", ]

df[colunas]

#%%
# SELECT * FROM df
df

# %%
# SELECT idCliente FROM df

df[["IdCliente"]]

# %%

# SELECT idCliente, qtPontos FROM df LIMIT 5

df[["IdCliente", "QtPontos"]].sample(5)
# df[["IdCliente", "QtPontos"]].head(5)
# df[["IdCliente", "QtPontos"]].tail(5)

# %%

# SELECT idCliente, idTransacao, qtPontos
# FROM df
# LIMIT 5

df[["IdCliente", "IdTransacao", "QtPontos"]].head(5)

# %%

colunas = list(df.columns)
colunas.sort()
colunas

df = df[colunas]
df