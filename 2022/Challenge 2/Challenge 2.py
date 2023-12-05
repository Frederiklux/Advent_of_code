import pandas as pd

"""
A = opponent Rock
B = opponent Paper
C = opponent Scissors
X = Rock
Y = Paper
Z = Scissors
"""
f = open('New Text Document.txt', 'r')

content = f.read()

content = content.replace(" ", ";")

df = pd.DataFrame([x.split(';') for x in content.split('\n')])

df.rename(columns = {0:'Opponent_choice', 1:'My_choice'}, inplace = True)

df["points_for_choice"] = 0
df["points_for_outcome"] = 0
df["Opponent_choice_translated"] = df["Opponent_choice"].replace({"A":"X", "B":"Y", "C":"Z"})

df.loc[df["My_choice"] == "X", 'points_for_choice'] = 1
df.loc[df["My_choice"] == "Y", 'points_for_choice'] = 2
df.loc[df["My_choice"] == "Z", 'points_for_choice'] = 3

df.loc[df['Opponent_choice_translated'] == df['My_choice'], 'points_for_outcome'] = 3

df.loc[(df["My_choice"] == "X") & (df["Opponent_choice_translated"] == "Z"), 'points_for_outcome'] = 6
df.loc[(df["My_choice"] == "Y") & (df["Opponent_choice_translated"] == "X"), 'points_for_outcome'] = 6
df.loc[(df["My_choice"] == "Z") & (df["Opponent_choice_translated"] == "Y"), 'points_for_outcome'] = 6

sum(df['points_for_choice']) + sum(df['points_for_outcome'])

"""
X = lose
Y = draw
Z = Win
"""

df['my_choice_2'] = 0

win_dict = [{"Opponent_choice": "A", "My_choice": "Y"},
{"Opponent_choice": "B", "My_choice": "Z"},
{"Opponent_choice": "C", "My_choice": "X"}]
draw_dict = [{"Opponent_choice": "A", "My_choice": "X"},
{"Opponent_choice": "B", "My_choice": "Y"},
{"Opponent_choice": "C", "My_choice": "Z"}]
lose_dict = [{"Opponent_choice": "A", "My_choice": "Z"},
{"Opponent_choice": "B", "My_choice": "X"},
{"Opponent_choice": "C", "My_choice": "Y"}]

df.loc[df['My_choice'] == "Z", 'my_choice_2'] = df['Opponent_choice'].map({i['Opponent_choice']:i['My_choice'] for i in win_dict})
df.loc[df['My_choice'] == "Y", 'my_choice_2'] = df['Opponent_choice'].map({i['Opponent_choice']:i['My_choice'] for i in draw_dict})
df.loc[df['My_choice'] == "X", 'my_choice_2'] = df['Opponent_choice'].map({i['Opponent_choice']:i['My_choice'] for i in lose_dict})

df["points_for_choice_2"] = 0
df["points_for_outcome_2"] = 0

df.loc[df["my_choice_2"] == "X", 'points_for_choice_2'] = 1
df.loc[df["my_choice_2"] == "Y", 'points_for_choice_2'] = 2
df.loc[df["my_choice_2"] == "Z", 'points_for_choice_2'] = 3

df.loc[df['Opponent_choice_translated'] == df['my_choice_2'], 'points_for_outcome_2'] = 3

df.loc[(df["my_choice_2"] == "X") & (df["Opponent_choice_translated"] == "Z"), 'points_for_outcome_2'] = 6
df.loc[(df["my_choice_2"] == "Y") & (df["Opponent_choice_translated"] == "X"), 'points_for_outcome_2'] = 6
df.loc[(df["my_choice_2"] == "Z") & (df["Opponent_choice_translated"] == "Y"), 'points_for_outcome_2'] = 6

sum(df['points_for_choice_2']) + sum(df['points_for_outcome_2'])