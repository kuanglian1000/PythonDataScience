import numpy as np

# Use a list to create a NumPy array.
arr = np.array([1,2,3,4,5]) #create ndarray by array() function

print(arr)
print(type(arr))

# Use a tuple to create a NumPy array.
arr = np.array((1,3,4,5,6))
print(arr)

#=== Dimensions in Arrays ===
# 0-D arrays
a = np.array(42)

# 1-D arrays(一維陣列 , 最常見的陣列型式) , 左右是一個[]
b = np.array([1,2,3,4,5])

# 2-D arrays(二維陣列 , NumPy有1個sub module for numpy.mat) , 左右是二個[[]]
c = np.array([[1,2,3],[4,5,6]])

# 3-D arrays(三維陣列) , 左右是三個[[[]]]
d = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])

# ===Check Number of Dimensions(回傳) => ndim
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

# Higher Dimensional Arrays(更多維度陣列)
arr = np.array([1,2,3,4],ndmin=5) #<=直接塞為五維陣列
print(arr)
print('number of dimension :' , arr.ndim)