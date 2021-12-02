import pandas as pd
import numpy as np

# Generate sample data
df = pd.DataFrame({'col_1': [4.2, 8.6, 12.3, 16.2, 20.2],
                   'col_2': [2.3, 4.5, 6.1, 8.2, 10.3],
                   'col_3': ['A', 'B', 'A', 'B', 'A']})

# Grouped transformation - multiple functions
df_g = df.groupby('col_3')
selected_columns = df.columns[(df.dtypes == 'float64')]
renamed_columns = ['{col}_scaled'.format(col=col) for col in selected_columns]
df[renamed_columns] = df_g[selected_columns] \
    .transform(lambda x: (x - x.mean()) / x.std())
renamed_columns = ['{col}_delta'.format(col=col) for col in selected_columns]
df[renamed_columns] = df_g[selected_columns] \
    .transform(lambda x: x - x.shift(1))


# More compactly
def m_transform(df_g, apply_fns):
    df_n =  pd.concat([
        df_g
            .transform(fn)
            .add_suffix('_' + fn_name)
        for fn_name, fn in apply_fns.items()], axis=1)
    return df_n


df_n = df.groupby('col_3')[df.columns[(df.dtypes == 'float64')]]\
    .pipe(m_transform,
          {'scaled': lambda x: (x - x.mean()) / x.std(),
           'delta': lambda x: x - x.shift(1)})
df = pd.concat([df, df_n], axis=1)


# Alternative
def m_transform(df, apply_fns):
    return pd.concat({fn_name: df.transform(fn) for fn_name, fn in apply_fns.items()}).unstack(0)


df_n = df.groupby('col_3')[df.columns[(df.dtypes == 'float64')]]\
    .pipe(m_transform,
          {'scaled': lambda x: (x - x.mean()) / x.std(),
           'delta': lambda x: x - x.shift(1)})
df[df_n.columns.map('_'.join)] = df_n

# Another approach
df_g = df.groupby('col_3', group_keys=False)
selected_columns = df.columns[df.columns.str.startswith('cvr_')]
apply_fns = {'scaled': lambda x: (x - x.mean()) / x.std(),
             'delta': lambda x: x - x.shift(1)}
df_n = pd.concat({fn_name: df_g[selected_columns].transform(fn) for fn_name, fn in apply_fns.items()}).unstack(0)
df[df_n.columns.map('_'.join)] = df_n
