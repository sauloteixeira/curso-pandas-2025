#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('../data/clientes.csv', sep=';')
df.head()

#%%
df.info()

#%%
df["QtdePontos"] + 100

#%%
df["pontos_100"] = df["QtdePontos"] + 100
df.head()

#%%
df["email_ou_twitch"] = df["FlEmail"] + df["FlTwitch"]
df.head()

#%%
df["email_e_twitch"] = df["FlEmail"] * df["FlTwitch"]
df.head()

#%%
df["qtdSocial"] = df["FlEmail"] + df["FlTwitch"] + df["FlYouTube"] + df["FlBlueSky"] + df["FlInstagram"]
df.head()

#%%
df["QtdePontos"].describe()

#%%
df["logPontos"] = np.log(df["QtdePontos"]+1)

#%%
plt.hist(df["logPontos"])
plt.grid(True)
plt.show()