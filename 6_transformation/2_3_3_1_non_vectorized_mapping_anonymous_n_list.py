import pandas as pd

df = pd.DataFrame({'col_1': [-1, 4, 6, 8, 9],
                   'col_2': [6, 8, 10, 4, 20],
                   'col_3': [-8, 10, 12, 1, 30]})

df = df\
  .assign(
     col_4 = df[['col_1', 'col_2', 'col_3']].apply(lambda x: min(x), axis=1)
  )
