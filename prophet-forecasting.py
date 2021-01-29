#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Python
import pandas as pd
import numpy as np
from fbprophet import Prophet
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


# Python
df = pd.read_csv('./data/example_wp_peyton_manning.csv')
df.head()


# In[3]:


# Python
def forecast(tdf):
  forecast_df = tdf[['ds', 'y']]
  
  m = Prophet()
  m.fit(forecast_df)
  
  future = m.make_future_dataframe(periods=365)
  forecast = m.predict(future)
  
  m.plot(forecast)
  
  return m, forecast


# In[4]:


m, forecast = forecast(df)


# In[5]:


# Python
m.plot_components(forecast);

