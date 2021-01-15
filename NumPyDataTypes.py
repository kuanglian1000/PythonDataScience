""" 
Data Types in Python
  strings ex."ABCD"
  integer ex. -1 , -2 , -3
  float   ex. 1.2 , 2.4
  boolean ex. True or False
  complex ex. 1.0 + 2.0j , 1.5 + 2.5j
"""
""" 
Data Types in NumPy
i - integer
b - boolean
u - unsigned integer(0 & 正整數)
f - float
c - complex float
m - timedelta
M - datetime
O - Object
s - string
U - Unicode string
V - fixed chunk of memory for other type(void)
"""

# Checking the Data Type of an array (dtype) <= 檢查array內的資料型別,是NumPy的型別
import numpy as np
arr = np.array([1,2,3,4])
print(arr.dtype)

arr = np.array(['apple','banana','cherry'])
print(arr.dtype)

