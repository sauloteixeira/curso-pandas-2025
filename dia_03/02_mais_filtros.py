#%%
import pandas as pd

df = pd.read_csv("../data/transacao_produto.csv", sep=";")
df

#%%
# filtro do idprotudo com dois valores
filtro = (df["IdProduto"] == 5) | (df["IdProduto"] == 11)
df[filtro]

#%%
# filtro do idprotudo com dois valores usando o isin
filtro = df["IdProduto"].isin([5, 11])
df[filtro]

#%%

clientes = pd.read_csv("../data/clientes_2.csv", sep=";")
clientes

#%%
# criando um filtro para clientes que tem a DtCriacao não nula
filtro = clientes["DtCriacao"].notna()
clientes[filtro]

#%%
# criando um filtro para clientes que tem a DtCriacao nula
filtro = clientes["DtCriacao"].isna()
clientes[filtro]

#%%
# negando uma condição
filtro = ~clientes["DtCriacao"].notna()
clientes[filtro]