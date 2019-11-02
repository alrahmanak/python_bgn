import numpy as np
import pandas as pd

mydata = {'x' : [10, 50, 18, 32, 47, 20], 'y' : ['12', '11', 'N/A', '13', '15', 'N/A']}
df = pd.DataFrame(mydata)
df.loc[df['y'] == 'N/A','y'] = np.nan
print("Completed")
print(df.head(6))

test_df = pd.read_csv('./test.csv', sep=",")
print(test_df.info())
print(test_df.head(5))
a_column = test_df['A']
print("a_column:", a_column)