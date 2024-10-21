import numpy as np

# Create an array
a = np.array([[1, 2, 3], [4, 5, 6],[2,5,6]])

# Reshape the array
b = a.reshape((3, 3))

# Perform an operation
c = a + 10
d=a-19

# Calculate mean
mean_value = np.mean(c)
median_value=np.median(c)
variance_value=np.var(c)

print("Original Array:\n", a)
print("Reshaped Array:\n", b)
print("Array after adding 10:\n", c)
print("Array after subs 19:\n", d)
print("Mean Value:", mean_value)
print("Median Value:", median_value)
print("varian         Value:", variance_value)
