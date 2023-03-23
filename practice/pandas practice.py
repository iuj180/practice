import pandas as pd
import numpy as np

np.random.seed(0)
arr=np.random.randint(10, size=(2,2))
print(arr)

df1=pd.DataFrame(arr, copy=False)
df2=pd.DataFrame(arr, copy=True)

arr[0,0]=99
print(df1)
print(df2)

data={'A' : [1,2], 'B' : [3,4]}
df=pd.DataFrame(data=data)
print(df)

data=np.array([1,2,], [3,4])
df=pd.DataFrame(data=data, index=['row1', 'row2'], columns=['col1', 'col2'])
print(df)

data=[[1,10,100], [2,20,200], [3,30,300]]
col=['col1', 'col2', 'col3']
row=['row1', 'row2', 'row3']
df=pd.DataFrame(data=data, index=row, columns=col)
print(df)
result=df.add(1)
print(result)

data2=[[3], [4], [5]]
df2=pd.DataFrame(data=data2, index=['row1', 'row2', 'row3'], columns=['col1'])
print(df2)
result=df.add(df2)
print(result)
result=df.add(df2, fill_value=0)
print(result)


data=[[1,10,100],[2,20,200],[3,30,300]]
col=['col1','col2','col3']
row=['row1', 'row2', 'row3']
df=pd.DataFrame(data=data, index=row, columns=col)
print(df)
result=df.sub(1)
print(result)
result=df-1
print(result)

data2=[[3],[4],[5]]
df2=pd.DataFrame(data=data2, index=['row1', 'row2', 'row3'], columns=['col1'])
print(df2)

result=df.sub(df2)
print(result)
result=df.sub(df2, fill_value=0)
print(result)

data=[[1,10,100],[2,20,200],[3,30,300]]
col=['col1','col2','col3']
row=['row1','row2','rwo3']
df=pd.DataFrame(data=data, index=row, columns=col)
print(df)

result=df.mul(2)
print(result)
result=df*2
print(result)

data2=[[3],[4],[5]]
df2=pd.DataFrame(data=data2, index=['row1','row2','row3'], columns=['col1'])
print(df2)

result=df.mul(df2)
print(result)