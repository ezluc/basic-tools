#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import glob
import pandas as pd
os.chdir("C:\\home\\projects\\python_projects\\alternativeinvestments\\all_trans")


# In[2]:


extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]


# In[3]:


#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
#export to csv
combined_csv.to_csv( "combined1.csv", index=False, encoding='utf-8-sig')


# In[3]:


import pandas as pd
import numpy as np
import glob
files = glob.glob("C:\\home\\jupyter_projects\\positions\\*.xlsx")
sheetname = 'Sheet0'
# Number of row to skip in each file
skiprows=6
# Header line that will be kept for column name (index 5 in Excel)
header=1
# Column containing the index for each row. Leave it to None if no index
index_col= 0
all_data = pd.DataFrame()
#DF = pd.read_excel(f, sheetname, skiprows = skiprows,header = header, index_col = index_col)

# Concatenate the content of other file to this dataframe
for f in files:
    DF = pd.read_excel(f, sheetname, skiprows = skiprows, header = header, index_col = None)
    all_data = all_data.append(DF,ignore_index=True,sort=True)
# Write the concatenated content to excel
all_data.to_excel('combined.xlsx',sheet_name = sheetname)


# In[ ]:




