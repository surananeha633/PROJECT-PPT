#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import packages in python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


# In[2]:


my=pd.read_excel('Global.xls')
my.head()


# In[3]:


#check the null value from dataset
my.isnull().sum()


# In[4]:


#delete the null value column postal code
my=my.drop(columns=['Postal Code'])
my.head()


# In[5]:


#check the null value column delete or not 
my.isnull().sum()


# In[6]:


# to display statistics about data
my.describe()


# In[7]:


# to display basic info datatype
my.info()


# In[8]:


#to display no of sample on each class
my['Segment'].value_counts()


# In[9]:


#BAR CHART
a=my['Region']
b=my['Shipping Cost']
plt.title('REGION WISE SHIPPING COST')
plt.xlabel('Region')
plt.ylabel('Shipping Cost')
plt.barh(a,b)


# In[10]:


#pie chart
#change sales datatype float to int 
my['Sales'] =my['Sales'].astype(int)
display(my.dtypes)


# In[11]:


#scatter plot
f=my['Sub-Category']
my['Profit'] = my['Profit'].astype(int)
display(my.dtypes)
g=my['Profit']


# In[12]:


#SCATTER PLOT
plt.scatter(g,f)
plt.title("SUB-CATEGORY WISE PROFIT")
plt.xlabel("Sub-Category")
plt.ylabel("Profit")
plt.show()


# In[13]:


#line chart
x=my['Sales']
b= x.head(n = 6)
y=my['City']
a=y.head(n=6)
plt.plot(a,b)
plt.title('CITY WISE SALES')


# In[14]:


ab=my['Sales']
w=ab.head(n=3)
w


# In[15]:


cd=my['Segment']
l=cd.head(n=3)
l


# In[16]:


#PIE CHART
plt.pie(w,labels=l)
plt.title('SEGMENT WISE SALES')


# In[ ]:




