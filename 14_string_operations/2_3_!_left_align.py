import pandas as pd

df = pd.DataFrame({'col_1': ['This is a long phrase.',
                             'This is another long phrase.',
                             'And yet another longer phrase.',
                             'And longer still this time round.']})

df['col_2'] = df['col_1'].str.ljust(40)
