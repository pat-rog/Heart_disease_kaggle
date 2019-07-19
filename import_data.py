import pandas as pd

data = pd.read_csv('heart.csv')
print(data.loc[[1,10,15],['age','sex']])

