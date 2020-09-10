import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer#SimpleImputer use new version, if use old version use Imputer

data= pd.read_csv('data.csv', header=None)
print(data)# now data is missing you must be filling in the blank(can dien vao cho trong) 

# process data

# received data from file csv
x=data.values
# init data missing
#imp=SimpleImputer(missing_values=np.nan,strategy='mean')#mean is missing=average in column
imp=SimpleImputer(missing_values=np.nan,strategy='most_frequent')#most_frequent is missing= the most values in column
print(x)
imp.fit(x)# fit() need an array
result=imp.transform(x)# step important
print(result)
pd.DataFrame(result).to_csv('output.csv')#convert ndarray to DataFrame and write csv file

