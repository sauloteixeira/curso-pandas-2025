#%%
import pandas as pd

df = pd.read_csv('../data/clientes.csv', sep=';')
df

#%%
# alterando o tipo de dados da coluna inteiro para float
df["QtdePontos"].astype(float)

#%%
df["DtCriacao"]

#%%

replace = {"0000-00-00 00:00:00": "1900-01-01 00:00:00"}

#%%
df["DtCriacao"] = pd.to_datetime(df["DtCriacao"].replace(replace))

#%%
df["DtCriacao"].dt.month