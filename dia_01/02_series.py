#%%
#Importações
import pandas as pd

#%%
#serie de idades em lista

idades = [
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 32, 
]
print(idades)

#%%
#Series

series_idades = pd.Series(idades)
series_idades

#%%
media_idades = series_idades.mean()
var_idades = series_idades.var()
summary_idades = series_idades.describe()

print(media_idades)
print(var_idades)
print(summary_idades)
