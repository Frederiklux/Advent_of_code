import pandas as pd

f = open('New Text Document.txt', 'r')

content = f.read()

print(content)


content = content.replace("\\r\\n", "")
content = content.replace("\n\n", ";")
content = content.replace("\n", ",")

content2 = content.split(";")

calories = []

for i in range(len(content2)):
    a = content2[i].split(",")
    b = [int(x) for x in a]
    calories.append(sum(b))

max(calories)

df_cal = pd.DataFrame(calories)
sum(df_cal.iloc[:3,0])

calories.sort(reverse=True)
calories_sorted = calories.sort(reverse=True)

