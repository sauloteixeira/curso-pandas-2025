# %%

import pandas as pd

# %%

df = pd.DataFrame({
    "nome": ['teo', 'lara', 'nah', 'bia', 'mah', 'lara', 'mah', 'mah'],
    "sobrenome": ['calvo', 'calvo', 'ataide', 'ataide', 'silva', 'silva', 'silva', 'silva'],
    "salario": [2132, 1231, 454, 6543, 6532, 4322, 987, 2134],
})

df

# %%
# df.drop_duplicates(keep='last')

#remove linhas duplicadas
df.drop_duplicates() 

#%%
df = df.sort_values("salario", ascending=False)
df

# %%

#remove linhas duplicadas baseado em uma ou mais colunas
df = df.drop_duplicates(subset=['nome', 'sobrenome'])
df = df.sort_index()
df

# %%
df = (df.sort_values("salario", ascending=False)
        .drop_duplicates(keep='last', subset=["nome", "sobrenome"]))

df

# %%
df = (df.sort_values("salario", ascending=False)
        .drop_duplicates(keep='last', subset=["nome", "sobrenome"])
        .sort_index())

df
