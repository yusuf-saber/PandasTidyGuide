import pandas as pd

df = pd.DataFrame({'col_1': [1, 2, 3, 4, 5]})

df['col_1'] = df['col_1'].astype('string')

print(df['col_1'].dtype)
