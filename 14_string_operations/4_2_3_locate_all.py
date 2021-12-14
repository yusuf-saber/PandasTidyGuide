
import pandas as pd
import re

df = pd.DataFrame(
    {'col_1': ['23 12 AR', 'AJ PJ RR', '22 22 TT 06', '12 UD 56 12', '44 22']})


def locate_all(string, pattern, flags=0):
    matches = re.finditer(pattern, string, flags)
    match_locations = []
    for match in matches:
        match_locations.append({'start': match.start(),
                                'end': match.end()})
    return match_locations


# Series of Lists of Dictionaries
df['matches'] = df['col_1'].apply(lambda x: locate_all(x, '\d{2}'))


# Get nth Match
def get_nth_match(matches, n):
    if len(matches) > 0 and len(matches) > n:
        return matches[n].get('start'), matches[n].get('end')
    else:
        return -1, -1


df[['start', 'end']] = \
    df.apply(lambda x: get_nth_match(x['matches'], 2), axis=1, result_type='expand')
