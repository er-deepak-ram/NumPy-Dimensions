import numpy as np

# 0-D Array
a = np.array(42)
print("0-D Array")
print(a)

# 1-D Array
b = np.array([1, 2, 3, 4, 5])
print("\n1-D Array")
print(b)

# 2-D Array
c = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2-D Array")
print(c)

# 3-D Array
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print("\n3-D Array")
print(d)

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)
