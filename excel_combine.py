#!/usr/bin/env python
# coding: utf-8

# In[65]:


# Script to concatenate a bunch of Excel files with
# Python and Pandas
#
# Remember that indexing starts with 0 in Python,
# whereas indexing starts with 1 in Excel
import os
import pandas as pd
import numpy as np
import glob
files = glob.glob("C:\\home\\jupyter_projects\\positions\\*.xlsx")
files


# In[66]:



# Number of files to process
# n = 10
# Excel sheetname
sheetname = 'Sheet0'
# Number of row to skip in each file
skiprows= 6
# Header line that will be kept for column name (index 8 in Excel)
header= 1
# Column containing the index for each row. Leave it to None if no index
index_col= 0
all_data = pd.DataFrame()
#DF = pd.read_excel(f, sheetname, skiprows = skiprows,header = header, index_col = index_col)

# Concatenate the content of other file to this dataframe
for f in files:
    DF = pd.read_excel(f, sheetname, skiprows = skiprows, header = header, index_col = None)
    DF['filename'] = os.path.basename(f)
    all_data = all_data.append(DF,ignore_index=True,sort=True)
# Write the concatenated content to excel
all_data


# In[67]:


all_data.to_excel('combined.xlsx',sheet_name = sheetname)


# In[ ]:




