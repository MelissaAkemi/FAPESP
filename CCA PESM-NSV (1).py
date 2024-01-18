#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.cross_decomposition import CCA

link = "https://raw.githubusercontent.com/MelissaAkemi/FAPESP/main/DataFrame%20-%20PESM-NSV%20-%20Copia.csv"
df = pd.read_csv(link, delimiter=";")
df =df.dropna()


# In[3]:


X=df[['Altitude',  'Profundidade',  'Largura',  'Velocidade' ]]
Y=df[[ 'Oxigênio',"pH","Temperatura","Integridade Ambiental"]]


# In[4]:


cca = CCA(n_components=4)
cca.fit(X, Y)
Xc,Yc=cca.transform(X, Y)
Yc.shape


# In[5]:


df[["U1","U2","U3","U4"]]=Xc
df[["V1","V2","V3","V4"]]=Yc


# In[6]:


corr=df[["U1","V1","U2","V2","U3","V3","U4","V4"]].corr()
ax=plt.subplots(figsize=(15,15))
ax=sns.heatmap(
    corr,
    vmin=-1,vmax=1,center=0,
    cmap=sns.diverging_palette(20,220,n=200),
    square=True)
ax.set_xticklabels(
    ax.get_xticklabels(), rotation=45, horizontalalignment="right" )


# In[23]:




