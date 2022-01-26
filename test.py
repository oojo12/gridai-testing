import pandas as pd
import dask.dataframe as dd

df = pd.DataFrame([1,2,3])
ddf = dd.from_pandas(df)
print(ddf)
