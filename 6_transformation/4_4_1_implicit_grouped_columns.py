import pandas as pd

# Generate sample data
df = pd.DataFrame({'col_1': ['A', 'B', 'A', 'B', 'A'],
                   'col_2': [4.2, 8.6, 12.3, 16.2, 20.2],
                   'col_3': [2.3, 4.5, 6.1, 8.2, 10.3]})

# Grouped transformation with implicitly selected columns
selected_columns = df.columns[(df.dtypes == 'float64')]
df[selected_columns] = df \
    .groupby('col_1')[selected_columns] \
    .transform(lambda x: (x - x.mean()) / x.std())
