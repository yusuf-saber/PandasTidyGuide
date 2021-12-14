import pandas as pd
import re

df = pd.DataFrame(
    {'col_1': ['23 12 AR', 'AJ PJ RR', '22 22 TT 06', '12 UD 56 12', '44 22']})


def locate_last(string, pattern, flags=0):
    matches = re.finditer(pattern, string, flags)
    match = None
    for match in matches:
        pass
    if match:
        return match.start(), match.end()
    else:
        return -1, -1


# Series of Lists of Dictionaries
df[['start', 'end']] = \
    df.apply(lambda x: locate_last(x['col_1'], '\d{2}'), axis=1, result_type='expand')
