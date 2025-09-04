# %%
# 05.05 - Selecione a primeira transação diária de cada cliente.

import pandas as pd

#%%
transacoes = pd.read_csv("../../data/transacoes_3.csv", sep=";")
transacoes.head()

transacoes["data"] = pd.to_datetime(transacoes["DtCriacao"], format="%Y-%m-%d %H:%M:%S.%f").dt.date
transacoes = transacoes.sort_values("DtCriacao")


#%%
transacoes.drop_duplicates(keep="first", subset=["IdCliente", "data"])

#%%
first = transacoes.drop_duplicates(keep="first", subset=["IdCliente", "data"])
last = transacoes.drop_duplicates(keep="last", subset=["IdCliente", "data"])

pd.concat([last, first])