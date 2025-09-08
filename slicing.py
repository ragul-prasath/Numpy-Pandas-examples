'''
arr = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90,100,110,120],
    [130,140,150,160]
])
1. Extract the 2x2 top-left corner.
2.Extract the last two rows and last two columns.
3.Extract all rows, but only columns 1 and 2.
4.Extract every second row and every second column
5.Replace all elements greater than 100 with 0
'''
import numpy as np
arr = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90,100,110,120],
    [130,140,150,160]
])
# Extract the 2x2 top-left corner.
print(arr[0:2,0:2])
print()

# Extract the last two rows and last two columns.
print(arr[-2:,-2:])
print()

# Extract all rows, but only columns 1 and 2.
print(arr[:,1:3])
print()

# Extract every second row and every second column
print(arr[:2,:2])
print()

# Replace all elements greater than 100 with 0
arr[arr>100]=0
print(arr)