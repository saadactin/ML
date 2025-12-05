# Day 4: NumPy Exercises — Solutions

**Note:** Only check these solutions after you've attempted the problems yourself!

---

## Exercise 1: Creating Arrays

### Solution 1.1

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)  # [1 2 3 4 5]
```

---

### Solution 1.2

```python
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)
# [[1 2 3]
#  [4 5 6]]
```

---

### Solution 1.3

```python
import numpy as np

# 1D array of 5 zeros
zeros_1d = np.zeros(5)
print(zeros_1d)  # [0. 0. 0. 0. 0.]

# 2D array of 3x4 ones
ones_2d = np.ones((3, 4))
print(ones_2d)
# [[1. 1. 1. 1.]
#  [1. 1. 1. 1.]
#  [1. 1. 1. 1.]]
```

---

### Solution 1.4

```python
import numpy as np

# Array from 0 to 9
arr1 = np.arange(10)
print(arr1)  # [0 1 2 3 4 5 6 7 8 9]

# 5 evenly spaced numbers from 0 to 10
arr2 = np.linspace(0, 10, 5)
print(arr2)  # [ 0.   2.5  5.   7.5 10. ]
```

---

## Exercise 2: Array Shape and Properties

### Solution 2.1

```python
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

print("Shape:", arr.shape)      # (2, 3)
print("Dimensions:", arr.ndim)  # 2
print("Size:", arr.size)        # 6
```

---

### Solution 2.2

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
arr_reshaped = arr.reshape(2, 3)
print(arr_reshaped)
# [[1 2 3]
#  [4 5 6]]
```

---

## Exercise 3: Array Indexing

### Solution 3.1

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print("First element:", arr[0])    # 10
print("Last element:", arr[-1])    # 50
print("Third element:", arr[2])    # 30
```

---

### Solution 3.2

```python
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print("Element at [0, 1]:", arr[0, 1])      # 2
print("Element at [2, 0]:", arr[2, 0])      # 7
print("First row:", arr[0])                 # [1 2 3]
print("Second column:", arr[:, 1])          # [2 5 8]
```

---

## Exercise 4: Array Slicing

### Solution 4.1

```python
import numpy as np

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# Elements from index 2 to 5 (exclusive)
print(arr[2:5])        # [2 3 4]

# Elements from index 5 to end
print(arr[5:])         # [5 6 7 8 9]

# Every 2nd element starting from 0
print(arr[::2])        # [0 2 4 6 8]
```

---

### Solution 4.2

```python
import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# First 2 rows, first 3 columns
print(arr[:2, :3])
# [[1 2 3]
#  [5 6 7]]

# All rows, columns 1 to 3
print(arr[:, 1:3])
# [[ 2  3]
#  [ 6  7]
#  [10 11]]
```

---

## Additional Notes

- **Array vs List:** NumPy arrays are more efficient for numerical operations than Python lists.

- **Shape tuple:** The shape `(2, 3)` means 2 rows and 3 columns. Always think "rows first, columns second."

- **Indexing:** Remember that indexing starts at 0, just like Python lists.

- **Slicing:** The slice `[start:stop]` includes `start` but excludes `stop`. So `[2:5]` gives indices 2, 3, and 4.

- **Views:** When you slice an array, you get a view (not a copy). Changes to the view affect the original. Use `.copy()` if you need an independent copy.

---

**Keep practicing! NumPy is a powerful tool for numerical computing. 🚀**

