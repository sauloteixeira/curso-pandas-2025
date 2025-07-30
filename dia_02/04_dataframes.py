#%%

import pandas as pd

df_clientes = pd.read_csv("../data/clientes.csv", sep=";")
df_clientes

#%%
df_clientes.head(n=10)


#%%
n = 8
df_clientes.tail(n)

#%%
n = 5
df_clientes.sample(n)

#%%
print(df_clientes.shape)
print(df_clientes.columns)
print(df_clientes.index)

#%%
print(df_clientes.info())
print(df_clientes.info(memory_usage="deep"))

#%%
df_clientes.dtypes
# df_clientes.dtypes["IdCliente"]
