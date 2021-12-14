
import pandas as pd

df = pd.DataFrame(
    {'col_1': ['AB', 'BC', 'CD', 'cD', 'De']})

# Starts with
df['col_2'] = df['col_1'].str.startswith('c')

# Ignore Case
df['col_2'] = df['col_1'].str.lower().str.startswith('c')
