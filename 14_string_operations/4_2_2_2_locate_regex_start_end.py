
import pandas as pd
import re

df = pd.DataFrame(
    {'col_1': ['LTE', '2G', '3g', '4G', '57GB']})


def locate(string, pattern, flags=0):
    match = re.search(pattern, string, flags)
    if match:
        return match.start(), match.end()
    else:
        return -1, -1


# locate first and last character of match
df[['start', 'end']] = \
    df.apply(lambda x: locate(x['col_1'], '\d+g'), axis=1, result_type='expand')

# ignore case
df[['start', 'end']] = \
    df.apply(lambda x: locate(x['col_1'], '\d+g', flags=re.IGNORECASE),
             axis=1, result_type='expand')

