#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 


# In[2]:


data= pd.read_csv(r"C:\Users\kumak\Desktop\selfstudy\Python\project 2.csv")


# In[11]:


data


# In[12]:


data.isnull().sum()


# In[17]:


data.dtypes


# In[18]:


data.fillna(data.mean(), inplace=True)
data


# In[19]:


data.isnull().sum()


# In[23]:


#slice the data to better control what iam working on without effecting other values
selected_columns = ['Make', 'Model', 'Type', 'Origin', 'DriveTrain', 'MSRP', 'Invoice']
sliced_data = data[selected_columns]

sliced_data


# In[22]:


sliced_data.isnull().sum()


# In[24]:


sliced_data.dtypes


# In[25]:


# Fill missing values in object columns with a specific value (e.g., 'Unknown')
object_columns = data.select_dtypes(include=['object']).columns
data[object_columns] = data[object_columns].fillna('Unknown')


# In[26]:


data.isnull().sum()


# In[30]:


# Fill missing values in numerical columns with the mean
numerical_columns = data.select_dtypes(include=['int', 'float']).columns
data[numerical_columns] = data[numerical_columns].fillna(data[numerical_columns].mean())

# Fill missing values in object columns with 'Unknown'
object_columns = data.select_dtypes(include=['object']).columns
data[object_columns] = data[object_columns].fillna('Unknown')

data


# In[31]:


data.isnull().sum()


# In[ ]:


#Check what are the different types of Make are there in our dataset


# In[32]:


data['Make'].dtypes


# In[33]:


unique_makes = data['Make'].unique()
print(unique_makes)


# In[44]:


data['Make'].value_counts()


# In[37]:


#And, what is the count (occurrence) of each Make in the data ?
len(unique_makes)


# In[ ]:


#Q. 3) Instruction ( Filtering ) - Show all the records where Origin is Asia or Europe.


# In[38]:


filer_byOrigine= data[(data['Origin'] =='Asia') | (data['Origin'] =='Europe')]


# In[39]:


filer_byOrigine


# In[ ]:


#using .isin and storing it in records


# In[45]:


records=data[data['Origin'].isin(['Europe','Asia'])]
records


# In[ ]:


#Q. 4)  Remove all the records (rows) where Weight is above 4000.


# In[48]:


#i, goin to use this sign ~ inorder to delete the rows in which weight is above 4000
data[~ (data['Weight'] > 4000)]


# In[ ]:


# Increase all the values of 'MPG_City' column by 3


# In[51]:


data['MPG_City']=data['MPG_City'].apply(lambda x:x+3)


# In[52]:


data


# In[ ]:




