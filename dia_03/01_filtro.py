#%%
import pandas as pd

#%%
df = pd.read_csv("../data/transacoes.csv", sep=";")
df.head()

#%%
# Filtro por coluna pela coluna "QtdePontos"
filtro = df["QtdePontos"] >= 50
df[filtro]

#%%
# Filtro por coluna pela coluna "QtdePontos" maior que 50 e menor que 100
filtro = (df["QtdePontos"] >= 50) & (df["QtdePontos"] < 100)
df[filtro].sample(10)

#%%
filtro = (df["QtdePontos"] == 1) | (df["QtdePontos"] == 100)
df[filtro].sample(10)

#%%
# filtro por coluna pela coluna "QtdePontos" maior que 0 e menor que 50 também filtrado por "dtCriacao" maior que 2025-01-01
filtro = (df["QtdePontos"] > 0) & (df["QtdePontos"] <= 50) & (df["DtCriacao"] > "2025-01-01")
df[filtro].sample(10)

#%%
# # filtro por coluna pela coluna "QtdePontos" maior que 0 e menor que 50 ou filtrado por "dtCriacao" maior que 2025-01-01
filtro = (df["QtdePontos"] > 0) & (df["QtdePontos"] <= 50) | (df["DtCriacao"] > "2025-01-01")
df[filtro].sample(10)



