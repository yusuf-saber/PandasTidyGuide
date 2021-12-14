import pandas as pd

df = pd.DataFrame({'col_1': ['one', 'two', 'three', 'five', 'six']})

df['col_2'] = df['col_1'].str.len()
