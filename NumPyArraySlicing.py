# NumPy Array Slicing (陣列分割)

"""
Slicing in python means taking elements from one given index to another given index.
We pass slice instead of index like this: [start:end].
We can also define the step, like this: [start:end:step].
If we don't pass start its considered 0 , [:5] <=從頭到5(不含)
If we don't pass end its considered length of array in that dimension , [0:] <=從頭到尾
If we don't pass step its considered 1 , [0:4:2] <= 0,2,4
"""
# Note: The result includes the start index, but excludes the end index.
import numpy as np

arr = np.array([1,2,3,4,5,6,7])
print(arr[1:5]) # 2,3,4,5

# Slice elements from index 4 to end of the array.
print(arr[4:])

# Slice elements from the beginning to index 4(not included).
print(arr[:4])

#======== Negative Slicing ========
# Slice from the index 3 from the end to index 1 from the end
print(arr[-3:-1]) # 5,6 . -1 = 最後1個值.


#======== Step ========
print(arr[1:5:2]) # 2,4
print(arr[:]) # 1,2,3,4,5,6,7
print(arr[::2]) #1,3,5,7


#===== Slicing 2-D Arrays ======
# arr[最外維 , 內維 , 內內維,...] ( , <= 使用逗號表示挑出維度) | ( : <= 使用冒號表示挑出該維度內項目長度)
arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])

# from the second element , slice elements from index 1 to index 4(not included.)
print(arr[1,1:4]) #value is [7,8,9]

# from the first & second element , slice element from index 2
print(arr[0:2,2]) # value is [3,8]

# from both elements , slice index 1 to index4(not included.) , this will return a 2-D array.
print(arr[:,1:4])


