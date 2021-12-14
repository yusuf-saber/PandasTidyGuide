
import pandas as pd
import re

df = pd.DataFrame(
    {'col_1': ['One', 'Two', 'Three', 'Four', 'Five']})

# Count vowels
df['col_2'] = df['col_1'].str.count('[aeiou]')

# Ignoring Case
df['col_3'] = df['col_1'].str.count('[aeiou]', flags=re.IGNORECASE)
