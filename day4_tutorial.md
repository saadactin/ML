# Day 4: Introduction to NumPy — Arrays, Indexing, Slicing, and Shape

## Introduction

**NumPy** (Numerical Python) is a fundamental library for scientific computing in Python. It provides powerful tools for working with arrays and performing mathematical operations efficiently.

**Why NumPy?**
- **Fast** — Operations are optimized in C
- **Efficient** — Uses less memory than Python lists
- **Powerful** — Built-in functions for mathematical operations
- **Foundation** — Used by many other libraries (Pandas, Matplotlib, etc.)

**What we'll learn today:**
- Creating NumPy arrays
- Array indexing and slicing
- Understanding array shape
- Basic array operations

---

## 1. Getting Started with NumPy

### Installation

If NumPy isn't installed, you can install it using:
```bash
pip install numpy
```

### Importing NumPy

The standard way to import NumPy is:
```python
import numpy as np
```

We use `np` as an alias (short name) for convenience. This is the convention used by everyone in the Python community.

---

## 2. Creating Arrays

### What is an Array?

An **array** in NumPy is similar to a list, but:
- All elements must be the same type (usually numbers)
- More efficient for mathematical operations
- Supports vectorized operations (operations on entire arrays at once)

### Creating Arrays from Lists

The most common way to create an array is from a Python list:

```python
import numpy as np

# 1D array (one-dimensional - like a list)
arr1d = np.array([1, 2, 3, 4, 5])
print(arr1d)  # [1 2 3 4 5]

# 2D array (two-dimensional - like a table/matrix)
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2d)
# [[1 2 3]
#  [4 5 6]]

# 3D array (three-dimensional)
arr3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr3d)
```

### Quick Array Creation Functions

NumPy provides several convenient functions to create arrays:

**`np.zeros()`** — Creates an array filled with zeros:
```python
# 1D array of zeros
zeros_1d = np.zeros(5)
print(zeros_1d)  # [0. 0. 0. 0. 0.]

# 2D array of zeros (3 rows, 4 columns)
zeros_2d = np.zeros((3, 4))
print(zeros_2d)
# [[0. 0. 0. 0.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]]
```

**`np.ones()`** — Creates an array filled with ones:
```python
# 1D array of ones
ones_1d = np.ones(5)
print(ones_1d)  # [1. 1. 1. 1. 1.]

# 2D array of ones
ones_2d = np.ones((2, 3))
print(ones_2d)
# [[1. 1. 1.]
#  [1. 1. 1.]]
```

**`np.arange()`** — Creates an array with a range of values (similar to `range()`):
```python
# From 0 to 9 (exclusive)
arr = np.arange(10)
print(arr)  # [0 1 2 3 4 5 6 7 8 9]

# From 2 to 9 (exclusive)
arr = np.arange(2, 10)
print(arr)  # [2 3 4 5 6 7 8 9]

# From 0 to 10 with step 2
arr = np.arange(0, 10, 2)
print(arr)  # [0 2 4 6 8]
```

**`np.linspace()`** — Creates an array with evenly spaced values:
```python
# 5 evenly spaced numbers from 0 to 10 (inclusive)
arr = np.linspace(0, 10, 5)
print(arr)  # [ 0.   2.5  5.   7.5 10. ]

# 3 evenly spaced numbers from 1 to 3
arr = np.linspace(1, 3, 3)
print(arr)  # [1. 2. 3.]
```

**`np.eye()`** — Creates an identity matrix (diagonal is 1, rest is 0):
```python
# 3x3 identity matrix
identity = np.eye(3)
print(identity)
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]
```

**`np.random`** — Create arrays with random values:
```python
# Random numbers between 0 and 1
random_arr = np.random.random(5)
print(random_arr)  # [0.234 0.567 0.891 ...]

# Random integers from 0 to 9
random_int = np.random.randint(0, 10, size=5)
print(random_int)  # [3 7 2 9 1]
```

### Array Data Types

Arrays have a specific data type. Common types:
- `int32` or `int64` — integers
- `float32` or `float64` — floating point numbers
- `bool` — boolean values

```python
arr = np.array([1, 2, 3])
print(arr.dtype)  # int64 (or int32 depending on system)

arr_float = np.array([1.0, 2.0, 3.0])
print(arr_float.dtype)  # float64

# Specify data type explicitly
arr_int = np.array([1, 2, 3], dtype=np.float64)
print(arr_int.dtype)  # float64
```

---

## 3. Array Shape

### Understanding Shape

The **shape** of an array describes its dimensions. It's a tuple showing the size of each dimension.

```python
import numpy as np

# 1D array with 5 elements
arr1d = np.array([1, 2, 3, 4, 5])
print(arr1d.shape)  # (5,) - 5 elements in one dimension

# 2D array with 2 rows and 3 columns
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2d.shape)  # (2, 3) - 2 rows, 3 columns

# 3D array
arr3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr3d.shape)  # (2, 2, 2) - 2x2x2 array
```

### Getting Array Dimensions

**`ndim`** — Returns the number of dimensions:
```python
arr1d = np.array([1, 2, 3])
print(arr1d.ndim)  # 1

arr2d = np.array([[1, 2], [3, 4]])
print(arr2d.ndim)  # 2
```

**`size`** — Returns the total number of elements:
```python
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.size)  # 6 (2 rows × 3 columns = 6 elements)
```

### Reshaping Arrays

**`reshape()`** — Changes the shape of an array without changing the data:
```python
arr = np.array([1, 2, 3, 4, 5, 6])

# Reshape to 2 rows, 3 columns
arr_2d = arr.reshape(2, 3)
print(arr_2d)
# [[1 2 3]
#  [4 5 6]]

# Reshape to 3 rows, 2 columns
arr_2d = arr.reshape(3, 2)
print(arr_2d)
# [[1 2]
#  [3 4]
#  [5 6]]

# Use -1 to let NumPy figure out one dimension
arr_2d = arr.reshape(2, -1)  # -1 means "figure it out"
print(arr_2d.shape)  # (2, 3)
```

**Important:** The total number of elements must remain the same when reshaping!

---

## 4. Array Indexing

### 1D Array Indexing

Indexing works just like Python lists:

```python
arr = np.array([10, 20, 30, 40, 50])

# Access single element
print(arr[0])   # 10 (first element)
print(arr[2])   # 30 (third element)
print(arr[-1])  # 50 (last element)
```

### 2D Array Indexing

For 2D arrays, use `[row, column]`:

```python
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Access single element (row 0, column 1)
print(arr[0, 1])  # 2

# Access entire row (row 1)
print(arr[1])     # [4 5 6]
print(arr[1, :])  # [4 5 6] (same thing)

# Access entire column (column 0)
print(arr[:, 0])  # [1 4 7]
```

**Indexing order:** `[row, column]` or `[row][column]` (both work):
```python
arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr[0, 1])   # 2
print(arr[0][1])    # 2 (same thing)
```

### 3D Array Indexing

For 3D arrays, use `[depth, row, column]`:

```python
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# Access element at depth 0, row 1, column 0
print(arr[0, 1, 0])  # 3

# Access entire 2D slice at depth 0
print(arr[0])
# [[1 2]
#  [3 4]]
```

### Boolean Indexing

You can use boolean arrays to select elements:

```python
arr = np.array([1, 2, 3, 4, 5])

# Create boolean array
mask = arr > 3
print(mask)  # [False False False  True  True]

# Use mask to select elements
print(arr[mask])  # [4 5]

# Or directly
print(arr[arr > 3])  # [4 5]
```

---

## 5. Array Slicing

### 1D Array Slicing

Slicing works like Python list slicing: `[start:stop:step]`

```python
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# Basic slicing
print(arr[2:5])      # [2 3 4] (from index 2 to 4, exclusive of 5)
print(arr[:5])       # [0 1 2 3 4] (from start to index 4)
print(arr[5:])       # [5 6 7 8 9] (from index 5 to end)
print(arr[:])        # [0 1 2 3 4 5 6 7 8 9] (entire array)

# With step
print(arr[::2])      # [0 2 4 6 8] (every 2nd element)
print(arr[1::2])     # [1 3 5 7 9] (every 2nd element starting from 1)
print(arr[::-1])     # [9 8 7 6 5 4 3 2 1 0] (reversed)
```

### 2D Array Slicing

For 2D arrays, slice both dimensions: `[row_slice, column_slice]`

```python
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# Get first 2 rows, first 3 columns
print(arr[:2, :3])
# [[1 2 3]
#  [5 6 7]]

# Get all rows, columns 1 to 3
print(arr[:, 1:3])
# [[ 2  3]
#  [ 6  7]
#  [10 11]]

# Get rows 1 to end, all columns
print(arr[1:, :])
# [[ 5  6  7  8]
#  [ 9 10 11 12]]

# Get every other row
print(arr[::2, :])
# [[1 2 3 4]
#  [9 10 11 12]]
```

### Important: Views vs Copies

**Views** — Slicing creates a view (not a copy) by default. Changes to the view affect the original:

```python
arr = np.array([1, 2, 3, 4, 5])
view = arr[1:4]  # This is a view, not a copy
view[0] = 99
print(arr)  # [1 99 3 4 5] - original changed!
```

**Copies** — Use `.copy()` to create an independent copy:

```python
arr = np.array([1, 2, 3, 4, 5])
copy = arr[1:4].copy()  # This is a copy
copy[0] = 99
print(arr)  # [1 2 3 4 5] - original unchanged
print(copy)  # [99 3 4]
```

---

## 6. Basic Array Operations

### Arithmetic Operations

Operations are performed element-wise:

```python
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

# Addition
print(arr1 + arr2)  # [ 6  8 10 12]

# Subtraction
print(arr2 - arr1)  # [4 4 4 4]

# Multiplication (element-wise, not matrix multiplication)
print(arr1 * arr2)  # [ 5 12 21 32]

# Division
print(arr2 / arr1)  # [5. 3. 2.333... 2.]

# Power
print(arr1 ** 2)  # [ 1  4  9 16]
```

### Operations with Scalars

You can perform operations with single numbers:

```python
arr = np.array([1, 2, 3, 4])

print(arr + 10)  # [11 12 13 14]
print(arr * 2)   # [2 4 6 8]
print(arr ** 2)  # [ 1  4  9 16]
```

### Useful Array Methods

**`sum()`** — Sum of all elements:
```python
arr = np.array([1, 2, 3, 4, 5])
print(arr.sum())  # 15

# For 2D arrays, sum along axis
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2d.sum())        # 21 (sum of all elements)
print(arr2d.sum(axis=0))  # [5 7 9] (sum along columns)
print(arr2d.sum(axis=1))  # [6 15] (sum along rows)
```

**`mean()`** — Average of all elements:
```python
arr = np.array([1, 2, 3, 4, 5])
print(arr.mean())  # 3.0
```

**`max()` and `min()`** — Maximum and minimum values:
```python
arr = np.array([3, 1, 4, 1, 5, 9, 2])
print(arr.max())  # 9
print(arr.min())  # 1
```

**`std()`** — Standard deviation:
```python
arr = np.array([1, 2, 3, 4, 5])
print(arr.std())  # 1.414...
```

---

## 7. Common Patterns and Examples

### Pattern 1: Creating Arrays for Calculations

```python
# Create array from 0 to 9
x = np.arange(10)
print(x)  # [0 1 2 3 4 5 6 7 8 9]

# Square all values
y = x ** 2
print(y)  # [ 0  1  4  9 16 25 36 49 64 81]
```

### Pattern 2: Working with 2D Data

```python
# Create a 3x4 matrix
matrix = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# Get shape
print(matrix.shape)  # (3, 4)

# Access specific elements
print(matrix[0, 0])  # 1 (top-left)
print(matrix[-1, -1]) # 12 (bottom-right)

# Get a row
print(matrix[1])  # [5 6 7 8]

# Get a column
print(matrix[:, 2])  # [3 7 11]
```

### Pattern 3: Filtering Arrays

```python
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Get all even numbers
evens = arr[arr % 2 == 0]
print(evens)  # [2 4 6 8 10]

# Get all numbers greater than 5
large = arr[arr > 5]
print(large)  # [6 7 8 9 10]
```

---

## 8. Common Mistakes

1. **Forgetting to import NumPy**
   ```python
   # ❌ WRONG
   # arr = array([1, 2, 3])  # NameError!
   
   # ✅ CORRECT
   import numpy as np
   arr = np.array([1, 2, 3])
   ```

2. **Confusing shape dimensions**
   ```python
   arr = np.array([[1, 2, 3], [4, 5, 6]])
   # Shape is (2, 3) - 2 rows, 3 columns
   # Not (3, 2)!
   ```

3. **Modifying views unintentionally**
   ```python
   arr = np.array([1, 2, 3, 4, 5])
   view = arr[1:4]
   view[0] = 99  # This changes arr too!
   
   # Use .copy() if you don't want to modify original
   copy = arr[1:4].copy()
   copy[0] = 99  # arr unchanged
   ```

4. **Wrong indexing order**
   ```python
   arr = np.array([[1, 2, 3], [4, 5, 6]])
   # Remember: [row, column]
   print(arr[0, 1])  # ✅ 2
   # Not [column, row]!
   ```

---

## Key Takeaways

1. **NumPy arrays** are efficient data structures for numerical computing
2. **Shape** describes array dimensions: `(rows, columns)` for 2D
3. **Indexing** uses `[row, column]` for 2D arrays
4. **Slicing** works like Python lists: `[start:stop:step]`
5. **Operations** are element-wise by default
6. **Views vs Copies** — slicing creates views; use `.copy()` for independent copies
7. **Import NumPy** as `import numpy as np`

---

## Next Steps

Practice with the exercises! NumPy is a powerful library, and mastering the basics will help you with data science, machine learning, and scientific computing.

Good luck! 🚀

