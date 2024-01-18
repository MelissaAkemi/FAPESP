#!/usr/bin/env python
# coding: utf-8

# In[10]:


import matplotlib.pyplot as plt
from scipy import stats
 
x=[8,13,13,10,6,9,9,8,8,10]
y=[0.7925, 0.8483,0.8208,0.8483,0.8316,0.8483,0.8408,0.8758,0.8758,0.8483]


# In[11]:


slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()


# In[ ]:




