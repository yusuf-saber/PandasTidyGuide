import pandas as pd

df = pd.DataFrame(
    {'col_1': ['A', 'B', 'C', 'c', 'D']})

# String contains
df['col_2'] = df['col_1'].str.contains('c', regex=False)

# Ignore case
df['col_2'] = df['col_1'].str.contains('c', regex=False, case=False)
