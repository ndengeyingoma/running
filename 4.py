import numpy as np

# 1. Create an array with arange and reshape it
b = np.arange(24).reshape(2, 3, 4)
print("Shape of b:", b.shape)
print("Array b:\n", b)

# 2. Select a specific element
print("\nb[0,0,0]:", b[0,0,0])  # First floor, first row, first column

# 3. Slice: first column and row on both floors
print("\nb[:,0,0]:", b[:,0,0])  # First column and row across both floors

# 4. Slice: entire first floor
print("\nb[0]:\n", b[0])

# Equivalent slicing using ellipsis
print("\nb[0, ...]:\n", b[0])

# 5. Select the second row on the first floor
print("\nb[0,1]:", b[0,1])

# Slice every second element of the second row on the first floor
print("\nb[0,1,::2]:", b[0,1,::2])

# 6. Select all rooms in the second column, across all rows and floors
print("\nb[...,1]:\n", b[...,1])

# Select all rooms in the second row, across both floors
print("\nb[:,1]:\n", b[:,1])

# Select rooms in the second column on the ground floor
print("\nb[0,:,1]:", b[0,:,1])

# Select last column on the ground floor
print("\nb[0,:,-1]:", b[0,:,-1])

# 7. Reverse the last column on the ground floor
print("\nb[0,::-1,-1]:", b[0,::-1,-1])

# Every second element of the reversed last column
print("\nb[0,::2,-1]:", b[0,::2,-1])

# 8. Reverse the entire array, switching the top and ground floors
print("\nb[::-1]:\n", b[::-1])
# Create a complex NumPy array
b = np.array([1+1j, 3+2j])
print("NumPy array b:", b)

# Convert the array to an integer array, discarding the imaginary part
b_int = b.astype(int)
print("Converted to integer array:", b_int)