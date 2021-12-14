
import pandas as pd

df = pd.DataFrame(
    {'col_1': ['good to go', 'come and go', 'now', 'Get it', 'hyper goat']})

# locate first character of match
df['col_2'] = df['col_1'].str.find('g')

# ignore case
df['col_3'] = df['col_1'].str.lower().str.find('g')
