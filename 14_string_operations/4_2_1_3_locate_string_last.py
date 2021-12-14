
import pandas as pd

df = pd.DataFrame(
    {'col_1': ['23 AR 22', 'AJ PJ AR', '22 22 TT 06', '12 UD ar 12', '44 22']})

# Match last substring
df['col_2'] = df['col_1'].str.rfind('AR')

# Ignore case
df['col_3'] = df['col_1'].str.upper().str.rfind('AR')
