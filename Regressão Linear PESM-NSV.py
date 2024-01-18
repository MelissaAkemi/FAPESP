#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
from scipy import stats
 
x=[20,17,11,14,15,13,12,10,18,13]
y=[0.6825, 0.7275,0.8105,0.5775,0.6991,0.8108,0.7108,0.6975,0.8150,0.7008]


# In[2]:


slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()


# In[ ]:




