#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns


# In[16]:


df=pd.read_csv('C:/Users/Dell/Downloads/housing_train.csv')


# In[17]:


df.head()


# In[19]:


df.tail()


# In[20]:


df.shape


# In[26]:


df.columns


# In[27]:


df.info()


# In[35]:


#missing data
total=df.isnull().sum().sort_values(ascending=False)
percent= (df.isnull().sum()/df.isnull().count()).sort_values(ascending=False)
missing_data = pd.concat([total,percent], axis=1, keys=['Total','Percent'])


# In[36]:


missing_data.head(20)


# In[77]:


#dealing with missing data 

df=df.dropna()



# In[79]:


df.info()


# In[81]:


df.shape


# In[82]:


#statistical summary of data
df['SalePrice'].describe()


# In[88]:


#histogram
sns.distplot(df['SalePrice']);


# In[ ]:


#skewness and kurtosis


# In[ ]:


#standardizing data


# In[89]:


#Bivariate Analysis SalePrice/GrLivArea(GreaterLivingArea)
var='GrLivArea'
data=pd.concat([df['SalePrice'],df[var]],axis=1)
data.plot.scatter(x=var,y='SalePrice',ylim=(0,800000));


# In[99]:


#deleting points

df=df.drop(df[df['Id']==1299].index)
df=df.drop(df[df['Id']==524].index)


# In[100]:


#scatter plot totalbsmtsf/saleprice
var='TotalBsmtSF'
data=pd.concat([df['SalePrice'],df[var]],axis=1)
data.plot.scatter(x=var,y='SalePrice',ylim=(0,800000));


# In[102]:


#boxplot overallqual/saleprice
var='OverallQual'
data=pd.concat([df['SalePrice'],df[var]],axis=1)
f,ax=plt.subplots(figsize=(8,6))
fig=sns.boxplot(x=var,y="SalePrice",data=data)


# In[ ]:





# In[ ]:





# In[ ]:




