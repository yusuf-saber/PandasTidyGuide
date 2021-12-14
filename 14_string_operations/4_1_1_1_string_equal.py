import pandas as pd

df = pd.DataFrame(
    {'col_1': ['A', 'B', 'C', 'c', 'D']})

# via basic string comparison
df['col_3'] = (df['col_1'] == 'c')

# Ignore Case
df['col_3'] = (df['col_1'].str.lower() == 'c')

# via str.fullmatch()
df['col_2'] = df['col_1'].str.fullmatch('C', case=False)
