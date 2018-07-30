import pandas as pd
import os,glob

cwd = os.getcwd()

path = cwd 
allFiles = glob.glob(path + "\\csv"+"/*.csv")
dataset2 = pd.DataFrame()
list_ = []
for file_ in allFiles:    
    df = pd.read_csv(file_,index_col=None, header=0, delimiter='\t',encoding='latin-1')
    list_.append(df) 
dataset2 = pd.concat(list_,ignore_index=True)

del allFiles,cwd,df,file_,list_,path

dataset2['title'].fillna('',inplace=True)

dataset2['trimmed_description'].fillna(dataset2['title'],inplace=True)

dataset2['summary'].fillna(dataset2['title'],inplace=True)

#-------------------------Get the max of trim_desc and summary and fill into the column news-----------------------

dataset2['news'] = dataset2.apply(lambda row: row['trimmed_description'] if len(row['trimmed_description'])>len(row['summary']) else row['summary'],axis=1)

A = pd.DataFrame(dataset2[dataset2['news'].str.contains('Virat')].count())

B = pd.DataFrame(dataset2[dataset2['news'].str.contains('Anushka')].count())

A_and_B = pd.DataFrame(dataset2[dataset2['news'].str.contains('Virat') & dataset2['news'].str.contains('Anushka')].count())

sample_space = dataset2.shape[0]

p_A_and_B = A_and_B/sample_space

p_B = B/sample_space

p_A = A/sample_space

p_A_given_B = p_A_and_B/p_B

print(p_A_given_B)


