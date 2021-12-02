import pandas as pd

# Generate sample data
df = pd.DataFrame({'col_1': [2, 4, 6, 8, 10],
                   'col_2': [1, 2, 3, 4, 5]})

# Chained Execution via assign()
df = df \
  .assign(
     col_3 = df[['col_1', 'col_2']].apply(lambda x: pow(*x), axis=1)
  )
