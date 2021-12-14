
import pandas as pd

df = pd.DataFrame(
    {'col_1': ['LTE', '2G', '3g', '4G', '5GB']})

# Full regex match
df['col_2'] = df['col_1'].str.fullmatch('\d+g')

# Ignore Case
df['col_2'] = df['col_1'].str.fullmatch('\d+g', case=False)
