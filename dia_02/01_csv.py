#%%
import pandas as pd

df = pd.read_csv("../data/clientes.csv", sep=";")
df

#%%

df.to_csv("clientes2.csv", index=False)
df.to_parquet("clientes.parquet", index=False)
df.to_excel("clientes.xlsx", index=False)

#%%

df_2 = pd.read_excel("clientes.xlsx")
df_2