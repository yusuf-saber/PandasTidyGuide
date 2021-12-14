import pandas as pd

df = pd.DataFrame(
    {'col_1': ['23 AR 22 AR', 'AJ AR AR PJ', '22 22 TT 06', 'AR 5 AR 12', '44 22']})


# Find All
def find_all(string, substring):
    matches = []
    start = 0
    while True:
        start = string.find(substring, start)
        if start == -1:
            return matches
        matches.append(start)
        start += len(substring)


# One off
find_all('yay yay yo yay', 'yay')

# Transform Column
df['result'] = df['col_1'].apply(find_all, substring='AR')

# nth match
nth = 1
df['start'] = \
    df.apply(lambda x: x['result'][nth] if len(x['result']) > nth else -1,
             axis=1)


# Via a function
def get_nth_match(matches, n):
    return matches[n] if len(matches) > n else -1


df['start'] = df['result'].apply(get_nth_match, n=1)
