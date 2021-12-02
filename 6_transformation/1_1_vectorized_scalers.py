import pandas as pd

# Generate sample data
df = pd.DataFrame({'col_0': ['1', '2', '3', '4', '5']})

# Chained Execution via assign()
df = df\
  .assign(
    col_1 = 3,
    col_2 = True
  )

# Unchained execution
df['col_1'] = 3
df['col_2'] = True
