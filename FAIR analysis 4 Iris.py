#!/usr/bin/env python
# coding: utf-8

# # FAIR analysis 4 Iris

# In[20]:


import sys
print("Python version:", sys.version)


# In[21]:


import pandas as pd
import numpy as np
import seaborn as sns


# In[22]:


print("Numpy version", np.__version__)


# In[23]:


print("pandas version:", pd.__version__)


# In[24]:


print("Seaborn version:", sns.__version__)


# ### Load iris dataset 

# In[25]:


iris = pd.read_csv('Iris.csv')


# In[26]:


iris = iris.drop(['Id'],axis=1)


# In[27]:


iris.head()


# ### Visualize

# In[28]:


sns.pairplot(iris, hue='Species')
plt.show()


# In[29]:


np.mean(iris['SepalLengthCm'])


# In[30]:


np.mean(iris['SepalWidthCm'])


# In[31]:


np.mean(iris['PetalLengthCm'])


# In[32]:


np.mean(iris['PetalWidthCm'])


# In[ ]:




