# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 18:21:46 2024

@author: sofaca

This is a self assigment given for the solemn 
purpose of learning how to manage datasets on
python... so if you laugh at my noobie code
i will punch you in the face ok?? (ง'̀-'́)ง
""" 

#### 1.Loading the data ####

import pandas as pd

# URL to the data file
file_path =r"C:\Users\sofia\Desktop\sofa\proyectos\python\worldleaders\arch_annual.txt"

data = pd.read_csv(file_path, delimiter='\t', encoding='latin1')

#### 2.Exploring the data ####
# Display the first few rows to understand its structure
# print(data.head())

# Display the basic information about the data set
print (data.info())

# Displayed informations is:
    # "RangeIndex: 17686 entries, 0 to 17685
    # Data columns (total 24 columns):
    #  #   Column              Non-Null Count  Dtype  
    # ---  ------              --------------  -----  
    #  0   obsid               17686 non-null  object 
    #  1   leadid              17686 non-null  object 
    #  2   ccode               17686 non-null  int64  
    #  3   idacr               17686 non-null  object 
    #  4   leader              17686 non-null  object 
    #  5   startdate           17686 non-null  object 
    #  6   enddate             17686 non-null  object 
    #  7   entry               17686 non-null  object 
    #  8   exit                17686 non-null  object 
    #  9   exitcode            17686 non-null  object 
    #  10  prevtimesinoffice   17686 non-null  object 
    #  11  posttenurefate      17686 non-null  object 
    #  12  gender              17686 non-null  object 
    #  13  yrborn              17686 non-null  int64  
    #  14  yrdied              17686 non-null  int64  
    #  15  borndate            12507 non-null  object 
    #  16  deathdate           5924 non-null   object 
    #  17  dbpedia.uri         9134 non-null   object 
    #  18  num.entry           17686 non-null  object 
    #  19  num.exit            17686 non-null  object 
    #  20  num.exitcode        17686 non-null  object 
    #  21  num.posttenurefate  17686 non-null  object 
    #  22  fties               1872 non-null   object 
    #  23  ftcur               1655 non-null   float64
    # dtypes: float64(1), int64(3), object(20)
    # memory usage: 3.2+ MB
    # None"

# What is this telling me about my code?

#Non-null, as oppossite of NaN, stands for the rows 
#with completed information. If the Non-Null count matches
#the number of rows meands absolute completeness.

#This dataset is incomplete in borndate, deathdate (probably sons
#of bitches still alive), dbpedia.uri (link a wikipedia), fties (family ties), f
#ftcur (0 or 1 wether the fties is to a past or future leader)

# print (data.describe())
# print (data.columns)

