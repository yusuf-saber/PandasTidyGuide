import pandas as pd

# Generate sample data
df = pd.DataFrame({'col_1': [-4.2, 1.1, 0.5, 1.6, 2.4]})


# A non-vectorized function with two arguments
def limit_range(x, th_min, th_max):
    return max(min(x, th_max), th_min)


# Apply function with two positional arguments
df = df\
  .assign(
     col_2 = df['col_1'].apply(limit_range, th_min = 0, th_max = 2)
  )
