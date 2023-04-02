#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


data = pd.read_csv('movies.csv',low_memory=False)
data['new_ID'] = range(1,len(data)+1)
data.head()


# In[4]:


data.isna().any()


# In[5]:


data.dropna(inplace=True)
#Checking for the Null Values
data.isna().sum()


# In[6]:


new_data = data[['new_ID','title','genres','imdb_score']]
new_data.head()


# In[7]:


def string_to_list(input_val):
    return input_val.split(",")


# In[8]:


new_data['Genre'] = new_data['genres'].apply(string_to_list)
new_data['Genre']


# In[9]:


new_data_genre = new_data.copy()
##For every row in the dataframe, iterate through the list of genres and place a 1 into the corresponding column
for index,row in new_data.iterrows():
    for genre in row['Genre']:
        new_data_genre.at[index,genre] = 1
##Filling in the NaN values with 0 to show that a movie doesn't have that column's genre
new_data_genre = new_data_genre.fillna(0)
new_data_genre.tail()


# In[10]:


data


# In[11]:


user_Input = [
    {'title':'Tampa Baes','imdb_score':4.4,'new_ID':9165},{'title':'I Love Lucy','imdb_score':8.5,'new_ID':957}]
    
input_movies = pd.DataFrame(user_Input)
input_movies


# In[12]:


user_Movies = new_data_genre[new_data_genre['new_ID'].isin(input_movies['new_ID'].tolist())]
user_Movies


# In[13]:


##Resetting the index to avoid confusion 
user_Movies = user_Movies.reset_index(drop=True)
##Dropping the unnecessary columns to save the memory and processing time
user_Movies.drop(['new_ID','title','Genre'],axis=1,inplace=True)
user_Movies


# In[17]:


genre_table = new_data_genre.set_index(new_data_genre['new_ID'])
genre_table.drop(['new_ID','title','Genre','genres','imdb_score'],axis=1,inplace=True)
genre_table


# In[19]:


user_Profile = user_Movies.transpose().dot(input_movies['imdb_score'])
user_Profile = user_Profile[1:]
user_Profile


# In[20]:


recommendation_tabel = recommendation_tabel.sort_values(ascending=False)
recommendation_tabel.head()


# In[ ]:




