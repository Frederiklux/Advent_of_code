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

all_ranges_list = list(df['First_Elf']) + list(df['Second_Elf'])
all_ranges = pd.DataFrame(all_ranges_list)
all_ranges.rename(columns = {0:'Full_ranges'}, inplace = True)
all_ranges[['lower', 'higher']] = all_ranges['Full_ranges'].str.split('-', expand=True)

counted = 0

for i in range(len(all_ranges)):
    for j in range(len(all_ranges)
    all_ranges_temp = all_ranges.copy().drop(i)
    if len(
        all_ranges.loc[
        (int(all_ranges.loc[i,'Full_ranges'].split('-')[0])>=all_ranges['lower'].astype(int)) & 
        (int(all_ranges.loc[i,'Full_ranges'].split('-')[1])<=all_ranges['higher'].astype(int)),:]) > 1:
        counted += 1

all_ranges.loc[
        (int(all_ranges.loc[i,'Full_ranges'].split('-')[0])>=all_ranges_temp['lower'].astype(int)),:]





del all_ranges_temp[1]

int(all_ranges.loc[i,'Full_ranges'].split('-')[0])
int(all_ranges.loc[i,'Full_ranges'].split('-')[1])

counted = 0

filter(lambda counted: int(all_ranges[1].split('-')[0]) >= int(all_ranges_temp[1].split('-')[0]), counted)


for i in range(len(all_ranges_list)):
    for j in range(len(all_ranges_list)-1):
        all_ranges_temp = all_ranges_list.copy()
        del all_ranges_temp[j]
        if (int(all_ranges_list[i].split('-')[0]) >= int(all_ranges_temp[j].split('-')[0])) and (int(all_ranges_list[i].split('-')[1]) <= int(all_ranges_temp[j].split('-')[1])):
            counted += 1
        else:
            pass

if (int(all_ranges[1].split('-')[0]) >= int(all_ranges_temp[2].split('-')[0])) and (int(all_ranges[i].split('-')[1]) <= int(all_ranges_temp[j].split('-')[1])):
    counted += 1