import pandas as pd
import numpy as np

# Generate sample data
df = pd.DataFrame({'col_1': ['A', 'B', 'A', 'B', 'A'],
                   'col_2': [2.3, 4.5, 6.1, 8.2, 10.3],
                   'col_3': [4.2, 8.6, 12.3, 16.2, 20.2]})


# Chained implicit grouped transformation
def custom_transform(df, g_cols, select_fn, apply_funs):
    df_c = df.copy()
    df_n = pd.concat([
        df.groupby(g_cols)[select_fn(df_c)]
            .transform(fn)
            .add_suffix('_' + fn_name)
        for fn_name, fn in apply_funs.items()], axis=1)
    df_c = pd.concat([df_c, df_n], axis=1)
    return df_c


df = df \
    .pipe(custom_transform,
          g_cols = ['col_1'],
          select_fn = lambda x: x.columns[x.dtypes == 'float64'],
          apply_funs = {'scaled': lambda x: (x - x.mean()) / x.std(),
                        'delta': lambda x: x - x.shift(1)}
          ) \
    .assign(
        col_4 = lambda x: x['col_2_scaled'] / x['col_3_scaled'],
        col_5 = lambda x: x['col_2_delta'] / x['col_3_delta']
    )
