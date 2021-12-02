import pandas as pd
import numpy as np

# Generate sample data
df = pd.DataFrame({'col_1': [4, 8, 12, 16, 20],
                   'col_2': [2, 4, 6, 8, 10]})

# Chained Execution via assign()
df = df\
  .assign(
     col_3 = df['col_1'].abs(),
     col_4 = df['col_2'].round(2),
     col_5 = lambda x: np.log10(x['col_3'])
   )

# Unchained execution
df['col_3'] = df['col_1'].abs(),
df['col_4'] = df['col_2'].round(2)
df['col_5'] = np.log10(df['col_4'])
