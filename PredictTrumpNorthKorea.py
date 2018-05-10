# -*- coding: utf-8 -*-

import pandas as pd
import os,glob

# reading from a excel ,skipfooter defines how many rows you want to leave
df=pd.read_excel(r'C:\Users\windows\Desktop\Bigdata dataset\1.xlsx')
df2=pd.read_excel(r'C:\Users\windows\Desktop\Bigdata dataset\2.xlsx')
df3=pd.read_excel(r'C:\Users\windows\Desktop\Bigdata dataset\3.xlsx')
df4=pd.read_excel(r'C:\Users\windows\Desktop\Bigdata dataset\4.xlsx') 
## Appending all the above dataframes into
dfl=[]
dfl.append(df1)
dfl.append(df2)
dfl.append(df3)
dfl.append(df4)
dataset2 = pd.concat(df1_,ignore_index=True)

del allFiles,cwd,df,file_,list_,path

dataset2['title'].fillna('',inplace=True)

dataset2['trimmed_description'].fillna(dataset2['title'],inplace=True)

dataset2['summary'].fillna(dataset2['title'],inplace=True)

#-------------------------Get the max of trim_desc and summary and fill into the column news-----------------------

dataset2['news'] = dataset2.apply(lambda row: row['trimmed_description'] if len(row['trimmed_description'])>len(row['summary']) else row['summary'],axis=1)

A = pd.DataFrame(dataset2[dataset2['news'].str.contains('Donald Trump')].count())

B = pd.DataFrame(dataset2[dataset2['news'].str.contains('Missile') & dataset2['news'].str.contains('North Korea')].count())

A_and_B = pd.DataFrame(dataset2[dataset2['news'].str.contains('Missile') & dataset2['news'].str.contains('North Korea') & dataset2['news'].str.contains('Donald Trump')].count())

sample_space = dataset2.shape[0]

p_A_and_B = A_and_B/sample_space

p_B = B/sample_space

p_A = A/sample_space

p_A_given_B = p_A_and_B/p_B

print(p_A_given_B)


