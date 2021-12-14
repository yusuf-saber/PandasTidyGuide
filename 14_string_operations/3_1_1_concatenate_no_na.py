import pandas as pd

df = pd.DataFrame(
    {'col_1': ['A', 'B', 'C', 'D', 'E'],
     'col_2': ['a', 'b', 'c', 'd', 'e']})

# Concatenate two columns
df['col_3'] = df['col_1'].str.cat(df['col_2'], sep=',')

# Concatenate n columns
df['col_4'] = df['col_1'].str.cat([df['col_2'], df['col_3']], sep=',')
