#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

clientes = pd.read_csv('../data/clientes.csv', sep=';')
clientes.head()

#%%

clientes["QtdePontos"].sort_values(ascending=False)

#%%
clientes.sort_values(by="QtdePontos", ascending=False)


#%%
clientes

#%%
(clientes.sort_values(by="QtdePontos", ascending=False)
        .head(10)["IdCliente"]
)
#%%
# Exemplo de ordenaçao de mais de uma coluna
brinquedo = pd.DataFrame(
    {
        "Nome": ["Teo", "Ana", "Nah", "Jose"],
        "Idade": [32, 43, 35, 42], 
        "Salario": [2345, 4533, 3245, 4533],
    }
)

brinquedo

#%%
brinquedo.sort_values(by=["Salario", "Idade"], ascending=[False, True])
