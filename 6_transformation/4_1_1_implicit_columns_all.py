import pandas as pd

# Generate sample data
df = pd.DataFrame({'col_1': [4.2, 8.6, 12.3, 16.2, 20.2],
                   'col_2': [2.3, 4.5, 6.1, 8.2, 10.3]})

# Execute on all columns via apply
df = df.apply(round)
