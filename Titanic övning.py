#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 


# In[2]:


file_path = "Titanic-Dataset.csv"
df = pd.read_csv(file_path)


# In[3]:


df.info()


# In[4]:


# create column FamilySize
df["FamilySize"] = df["SibSp"] + df["Parch"]
df["Sex_nr"] = df["Sex"].replace({"male": 0, "female": 1})
df


# In[7]:


df


# In[8]:


df.info()


# In[10]:


import pandas as pd

# Antag att du har en DataFrame kallad 'df' med en kolumn 'Embarked'
# Använd one-hot encoding
df_encoded = pd.get_dummies(df, columns=['Embarked'], prefix='Embarked')

# Visa den modifierade DataFrame
print(df_encoded.head())


# In[12]:


df_encoded


# In[ ]:




