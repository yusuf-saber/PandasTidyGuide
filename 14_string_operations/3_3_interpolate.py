import pandas as pd

df = pd.DataFrame(
    {'col_1': ['A', 'B', 'C', 'D', 'E'],
     'col_2': ['a', 'b', 'c', 'd', 'e']})

# Concatenate two columns
df['col_3'] = \
    df.apply(lambda x: '{} is capital for {}'.format(x['col_1'], x['col_2']),
             axis=1)
