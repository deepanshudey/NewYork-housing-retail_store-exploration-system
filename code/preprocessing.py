#!/usr/bin/env python
# coding: utf-8

# In[34]:


import pandas as pd
import numpy as np

def preprocess():
        
    # In[35]:


    housing = pd.read_csv("data/housing.csv")


    # In[36]:


    housing.head()


    # In[37]:


    project = housing[['project_id', 'project_name', 'project_start_date', 'project_completion_date', 'postcode','bbl']]


    # In[39]:


    project


    # In[40]:


    house_affordability = housing[['prevailing_wage_status', 'low_income_units', 'middle_income_units','moderate_income_units', 'extremely_low_income_units', 'very_low_income_units','project_id',]]


    # In[42]:


    house_affordability.head()


    # In[43]:


    building_address = housing[['building_id','borough', 'street_name', 'house_number', 'project_id', 'latitude', 'longitude']]


    # In[44]:


    building_address


    # In[54]:


    house_description = housing[['total_units','counted_rental_units','counted_homeownership_units','_1_br_units','_2_br_units','_3_br_units','_4_br_units','_5_br_units','_6_br_units','project_id']]


    # In[58]:


    house_description


    # In[60]:
    retail_stores = pd.read_csv("data/ud4g-9x9z.csv")
    retail_stores_list = retail_stores[['store_name', 'street_address', 'borough', 'zip_code', 'bbl','latitude','longitude']]
    retail_stores_list.to_csv('data/retail_stores.csv')

    project.to_csv('data/project.csv')
    house_affordability.to_csv('data/house_affordability.csv')
    building_address.to_csv('data/building_address.csv')
    house_description.to_csv('data/house_description.csv')


    # In[ ]:
    hospital = pd.read_csv("data/f7b6-v6v3.csv")
    hospital_list = hospital[['facility_type','facility_name','postcode','borough','location_1', 'phone','latitude','longitude']]
    hospital_list.to_csv('data/hospital_list.csv')



