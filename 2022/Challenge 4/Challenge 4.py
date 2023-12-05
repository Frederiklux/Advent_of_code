import pandas as pd

f = open('input.txt', 'r')

content = f.read()

content = content.replace(",", ";")

df = pd.DataFrame([x.split(';') for x in content.split('\n')])

df.rename(columns = {0:'First_Elf', 1:'Second_Elf'}, inplace = True)
df['contained'] = False


for i in range(len(df)):
    if (int(df['First_Elf'][i].split('-')[0]) >= int(df['Second_Elf'][i].split('-')[0])) and (int(df['First_Elf'][i].split('-')[1]) <= int(df['Second_Elf'][i].split('-')[1])):
        df.loc[i, 'contained'] = True
    else:
        df.loc[i, 'contained'] = False

for i in range(len(df)):
    if (int(df['Second_Elf'][i].split('-')[0]) >= int(df['First_Elf'][i].split('-')[0])) and (int(df['Second_Elf'][i].split('-')[1]) <= int(df['First_Elf'][i].split('-')[1])):
        df.loc[i, 'contained'] = True
    else:
        pass

sum(df['contained'])

df['contained'] = False
i=0
for i in range(len(df)):
    first_low = int(df['First_Elf'][i].split('-')[0])
    first_high = int(df['First_Elf'][i].split('-')[1])
    second_low = int(df['Second_Elf'][i].split('-')[0])
    second_high = int(df['Second_Elf'][i].split('-')[1])
    if (first_low >= second_low) and (first_low <= second_high):
        df.loc[i, 'contained'] = True
    if (first_high >= second_low) and (first_high <= second_high):
        df.loc[i, 'contained'] = True
    if (second_low >= first_low) and (second_low <= first_high):
        df.loc[i, 'contained'] = True
    if (second_high >= first_low) and (second_high <= first_high):
        df.loc[i, 'contained'] = True

sum(df['contained'])