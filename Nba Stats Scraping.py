#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
import requests
pd.set_option('display.max_columns', None) # so we can see all columns in a wide DataFrame
import time
import numpy as np


# In[12]:


test_url = 'https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=PerGame&Scope=S&Season=2023-24&SeasonType=Regular%20Season&StatCategory=EFF'


# In[13]:


r = requests.get(url=test_url).json()


# In[15]:


table_headers = r['resultSet']['headers']


# In[20]:


pd.DataFrame(r['resultSet']['rowSet'], columns=table_headers)


# In[25]:


temp_df1 = pd.DataFrame(r['resultSet']['rowSet'], columns=table_headers)
temp_df2 = pd.DataFrame({'Year':['2023-24' for i in range(len(temp_df1))],
                         'Season_type':['Regular%20Season' for i in range(len(temp_df1))]})
temp_df3 = pd.concat([temp_df2,temp_df1], axis=1)
temp_df3


# In[27]:


del temp_df1, temp_df2, temp_df3


# In[29]:


df_cols = ['Year', 'Season_type'] + table_headers


# In[30]:


pd.DataFrame(columns=df_cols)


# In[ ]:





# In[38]:


df = pd.DataFrame(columns=df_cols)
season_types = ['Regular%20Season']
years = ['2023-24']

begin_loop = time.time()

for y in years:
    for s in season_types:
        api_url = 'https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=PerGame&Scope=S&Season='+y+'&SeasonType='+s+'&StatCategory=EFF'
        r = requests.get(url=api_url).json()
        temp_df1 = pd.DataFrame(r['resultSet']['rowSet'], columns=table_headers)
        temp_df2 = pd.DataFrame({'Year':[y for i in range(len(temp_df1))],
                         'Season_type':[s for i in range(len(temp_df1))]})
        temp_df3 = pd.concat([temp_df2,temp_df1], axis=1)
        df = pd.concat([df, temp_df3], axis=0)
        print(f'Finished scraping data for the {y} {s}.')
        lag = np.random.uniform(low=5,high=45)
        print(f'...waiting {round(lag,1)} seconds')
        time.sleep(lag)
        
print(f'Process completed!Total run time: {round(time.time()-begin_loop)/60,2}')
df.to_csv('nba_player_data.csv', index=False)


# In[39]:


df


# In[ ]:




