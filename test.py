import pypeline as pl
from pypeline import impute
import pandas as pd

df = pd.DataFrame([[0, 1, 2], [2, 3, 4]], columns=['A', 'B', 'C'])
print(df)

pipe = pl.Pype(df)

pipe.add(impute.gaussian(df, 'A', 1))