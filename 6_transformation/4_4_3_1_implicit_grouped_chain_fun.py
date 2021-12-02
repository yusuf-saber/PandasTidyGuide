import pandas as pd
import numpy as np

# Generate sample data
df = pd.DataFrame({'col_1': ['A', 'B', 'A', 'B', 'A'],
                   'col_2': [2.3, 4.5, 6.1, 8.2, 10.3],
                   'col_3': [4.2, 8.6, 12.3, 16.2, 20.2]})


# Chained implicit grouped transformation
def custom_transform(df, g_cols, select_fn, apply_fun):
    df_c = df.copy()
    selected_columns = select_fn(df_c)
    df_c[selected_columns] = df_c \
        .groupby(g_cols)[selected_columns] \
        .transform(apply_fun)
    return df_c


df = df \
    .pipe(custom_transform,
          g_cols = ['col_1'],
          select_fn = lambda x: x.columns[x.dtypes == 'float64'],
          apply_fun = lambda x: (x - x.mean()) / x.std()
          ) \
    .assign(
        col_4=df['col_2'] / df['col_3']
    )