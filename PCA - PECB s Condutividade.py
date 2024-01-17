#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
import plotly.express as px
link = "https://raw.githubusercontent.com/MelissaAkemi/FAPESP/main/DataFrame%20-%20PECB%20-%20Copia.csv"
df = pd.read_csv(link, delimiter=";")
print(df)
x = df.loc[: , df.columns != 'Córrego'].values
y = df["Córrego"].values
nomes=["Altitude","Profundidade","Largura","Velocidade","Oxigênio","pH","Temperatura","Integridade Ambiental"]
X= df[nomes]


# In[2]:


pca = PCA(n_components=2)
components = pca.fit_transform(X)

loadings = pca.components_.T * np.sqrt(pca.explained_variance_)

fig = px.scatter(components, x=0, y=1, color=df['Córrego'])

for i, nome in enumerate(nomes):
    fig.add_annotation(
        ax=0, ay=0,
        axref="x", ayref="y",
        x=loadings[i, 0],
        y=loadings[i, 1],
        showarrow=True,
        arrowsize=1,
        arrowhead=1,
        xanchor="right",
        yanchor="top"
    )
    fig.add_annotation(
        x=loadings[i, 0],
        y=loadings[i, 1],
        ax=0, ay=0,
        xanchor="center",
        yanchor="bottom",
        text=nome,
        yshift=5,
    )
fig.show()

