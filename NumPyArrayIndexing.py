import numpy as np

# Access Array Elements
arr = np.array([1,2,3,4])
print(arr[0]) #存取值,key從0開始
print(arr[1])
print(arr[2] + arr[3])

# Access 2-D Arrays
c = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print('2nd element on 1st dim:' , c[0,1]) #value = 2
print('5th element on 2nd dim:' , c[1,4]) #value = 10

# Access 3-D Arrays
d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(d[0,1])
print(d[0,1,2]) #value = 6

# Negative Indexing
arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print('Last element from 2nd dim:' , arr[1,-1]) #value = 10