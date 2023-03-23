import numpy as np

data=[1,2,3]
arr=np.array(data)
print(arr)
print(type(arr))

result=arr*10
print(result)


data2d=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

arr2=np.array(data2d)
print(arr2[:,0])