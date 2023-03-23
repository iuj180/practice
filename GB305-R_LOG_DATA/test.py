import pandas as pd

test=pd.read_csv('d:/blindcat/GB305-R_LOG_DATA/220725/log1/2207221343.csv', encoding='cp949')

test.head(20)
test.describe()
