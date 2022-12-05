import pandas as pd
import string

f = open('input.txt', 'r')

content = f.read()

content = content.replace(" ", ";")

df = pd.DataFrame([x.split(';') for x in content.split('\n')])
df.rename(columns = {0:'Bag_items'}, inplace = True)

df['compartment1'], df['compartment2'], df['duplicates'], df['letterpoints'] ='', '', '', ''

for i in range(len(df)):
    df.loc[i,'compartment1'] = df.loc[i,'Bag_items'][:len(df['Bag_items'][i])//2]
    df.loc[i,'compartment2'] = df.loc[i,'Bag_items'][len(df['Bag_items'][i])//2:]
    for char in df.loc[i, 'compartment1']:
        if char in df.loc[i, 'compartment2']:
            df.loc[i, 'duplicates'] = df.loc[i, 'duplicates'] + char
    df.loc[i, 'letterpoints'] = string.ascii_letters.index(df.loc[i, 'duplicates'][0])+1
 
sum(df['letterpoints'])

df['badge_points'] = 0
for i in range(0,298,3):
    for char in df.loc[i:i+2,'Bag_items'][i]:
        if char in df.loc[i:i+2,'Bag_items'][i+1]:
            if char in df.loc[i:i+2,'Bag_items'][i+2]:
                df.loc[i,'badge_points'] = string.ascii_letters.index(char)+1

sum(df['badge_points'])
