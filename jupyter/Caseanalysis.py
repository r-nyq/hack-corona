#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#For further details, tutorials and documentations, 
#  please consult our Github account:  https://github.com/tsi-dih 
#Please note that, if you want to know the data files list of this project, 
#  you can go to DIH Portal->Control Center->Storage, 
#  and then go to hackcorona_33@dih.telekom.net/1298/521 directory 
#if you leave parameter path as empty or '<FILENAME>', we will return the first available data file 
from dih.storage import read_storage_account

data = read_storage_account(
    path = '<FILENAME>',
    project_id = '521',
    workspace_id = '1298',
    application_key = '9df6429c-0083-4dc4-bed3-7f0edde2b5f2',
    api_gateway_endpoint = 'https://api.dih.telekom.net/api/v1/storage/fs/readfile',
    account = "pdataanalyticshub",
    username = "hackcorona_33@dih.telekom.net"
)

print(len(data))


# In[ ]:


data


# In[1]:


import requests
import json


# In[2]:


url = "https://opendata.arcgis.com/datasets/dd4580c810204019a7b8eb3e0b329dd6_0.geojson"


# In[3]:


urlData = requests.get(url).content


# In[4]:


jsonContent = json.loads(urlData.decode('utf-8'))


# In[5]:


jsonContent


# In[ ]:




