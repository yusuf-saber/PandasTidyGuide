import pandas as pd

# Generate sample data
df = pd.DataFrame({'col_1': [2, 4, 6, 8, 10],
                   'col_2': [1, 2, 3, 4, 5],
                   'col_3': [5, 9, 6, 8, 20]})

# Chained Execution via assign()
df = df \
  .assign(
     col_4 = df[['col_1', 'col_2', 'col_3']].apply(min, axis=1)
  )
