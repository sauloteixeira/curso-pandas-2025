#%%

import pandas as pd

clientes = pd.read_csv("../data/clientes_2.csv", sep=";")
clientes

#%%

clientes.dropna(how="any")

# %%
df = pd.DataFrame(
    {
        "nome": ["Téo", None, "Nah", "Marcio"],
        "idade": [None, None, 43, 52],
        "salario": [3453,4324,None,5423]
    }
)

# how="all" deleta linha se todas as colunas forem nulas
# how="all" com subset deleta linha se todos os criterios forem nulos
# how="any" com subset deleta linha se algum dos criterios for nulo
df

#%%
df.dropna(how="all", subset=["idade", "nome"])


# %%

# substitui nulos por 0 nos valores de idade
df["idade"] = df["idade"].fillna(0)
df

# %%
df.fillna({"nome": "nao informado", "idade": 0})

# %%
medias = df[['idade', 'salario']].mean()
df.fillna(medias)