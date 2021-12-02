import pandas as pd
import numpy as np

# Generate sample data
df = pd.DataFrame({'col_1': ['one', 'two', 'three', 'four', 'five'],
                   'col_2': [2, 4, 6, 8, 10],
                   'col_3': [6, 8, 10, 16, 20]})

# Chained Execution via assign()
df = df \
  .assign(
    col_4 = df.apply(lambda x: len(x['col_1']), axis=1),
    col_5 = df.apply(lambda x: np.mean([x['col_2'], x['col_3']]), axis=1),
    col_6 = df.apply(lambda x: np.min([x['col_2'], x['col_3']]), axis=1)
  )

# Unchained execution
df['col_4'] = df.apply(lambda x: len(x['col_1']), axis=1)
df['col_5'] = df.apply(lambda x: np.mean([x['col_2'], x['col_3']]), axis=1)
df['col_6'] = df.apply(lambda x: np.min([x['col_2'], x['col_3']]), axis=1)
