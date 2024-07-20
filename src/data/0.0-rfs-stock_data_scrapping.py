#!/usr/bin/env python
# coding: utf-8

# **File:** 0.0-rfs-stock_data_scrapping.py<br>
# **Author:** Ryne F. Shelton<br>
# **Contact:** rfshelton@att.net<br>
# _____________
# **Description:**<br>
# This script fetches stock price data from finance.yahoo.com and saves it to project '*../data/external*' file location.  

# In[4]:


import numpy as np
import pandas as pd
import yfinance as yf


# In[7]:


# my_lst = ['appl','intc','nvda']
# period = '5y'


# In[16]:


def get_yfinance_data(ticker_list,period):
    for i in range(len(ticker_list)):
        tick = yf.Ticker(ticker_list[i])
        df=tick.history(period=period)
        df.to_csv("../data/external/"+ticker_list[i]+"_data_raw")

