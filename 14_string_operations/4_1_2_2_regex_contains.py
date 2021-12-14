import pandas as pd

df = pd.DataFrame(
    {'col_1': ['LTE', '2G', '3g', '4G', '5GB']})

# String contains
df['col_2'] = df['col_1'].str.contains('\d+g', regex=True)

# Ignore case
df['col_3'] = df['col_1'].str.contains('\d+g', regex=True, case=False)
