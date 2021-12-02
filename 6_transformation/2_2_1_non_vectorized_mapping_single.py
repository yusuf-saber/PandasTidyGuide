import pandas as pd

# Generate sample data
df = pd.DataFrame({'col_1': ['one', 'two', 'three', 'four', 'five']})

# Chained Execution via assign()
df = df \
  .assign(
    col_2 = df['col_1'].apply(len)
  )
