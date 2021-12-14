
import pandas as pd

df = pd.DataFrame(
    {'col_1': ['AB', 'BC', 'CD', 'cD', 'De']})

# Starts with
df['col_2'] = df['col_1'].str.endswith('d')

# Ignore Case
df['col_2'] = df['col_1'].str.lower().str.endswith('d')
