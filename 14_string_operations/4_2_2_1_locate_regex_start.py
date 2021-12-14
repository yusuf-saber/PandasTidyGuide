
import pandas as pd
import re

df = pd.DataFrame(
    {'col_1': ['LTE', '2G', '3g', '4G', '5GB']})


def locate(string, pattern, flags=0):
    match = re.search(pattern, string, flags)
    if match:
        return match.start()
    else:
        return -1


# locate first character of match
df['col_2'] = df['col_1'].apply(lambda x: locate(x, '\d+g'))

# ignore case
df['col_3'] = df['col_1'].apply(lambda x: locate(x, '\d+g', flags=re.IGNORECASE))
