import pandas as pd

df = pd.DataFrame({'col_1': ['one', 'two', 'three', 'four', 'five']})

df = df \
    .assign(
        col_2=df.apply(lambda x: 'Char count is ' + str(len(x['col_1'])), axis=1)
    )
