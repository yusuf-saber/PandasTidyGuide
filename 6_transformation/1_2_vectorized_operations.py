import pandas as pd

# Generate sample data
df = pd.DataFrame({'col_1': [4, 8, 12, 16, 20],
                   'col_2': [2, 4, 6, 8, 10],
                   'col_3': [True, True, False, False, True]})

# Chained Execution via assign()
df = df \
  .assign(
    col_4 = ~df['col_3'],
    col_5 = df['col_1'] + df['col_2'],
    col_6 = df['col_1'] - df['col_2'],
    col_7 = lambda x: x['col_5'] / x['col_6']
   )

# Unchained execution
df['col_4'] = ~df['col_3']
df['col_5'] = df['col_1'] + df['col_2']
df['col_6'] = df['col_1'] - df['col_2']
df['col_7'] = df['col_5'] / df['col_6']
