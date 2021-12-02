import pandas as pd
from scipy.stats import norm

df = pd.DataFrame({'col_1': [-1, 4, 6, 8, 10],
                   'col_2': [6, 8, 10, 4, 20]})

df = df\
  .assign(
     col_2 = df.apply(lambda x: norm.pdf(0.1, loc = x['col_1'], scale = x['col_2']), axis=1)
  )
