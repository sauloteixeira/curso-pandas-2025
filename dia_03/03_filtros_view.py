#%%
import pandas as pd

clientes = pd.read_csv("../data/clientes_2.csv", sep=";")
clientes

#%%

filtro = clientes["QtdePontos"] == 0
clientes_0 = clientes[filtro]

clientes_0["flag_1"] = 1
clientes_0