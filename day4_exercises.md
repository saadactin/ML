# Day 4: NumPy Exercises — Arrays, Indexing, Slicing, and Shape

**Estimated Time: 20 minutes**

**Instructions:**
- Read each question carefully
- Try to solve it yourself before checking the solution
- Type out the code (don't just read it) — muscle memory helps!
- If you get stuck, read the hint, then try again
- Check the solutions in `day4_solution.md` only after you've attempted the problem
- Make sure to import NumPy: `import numpy as np`

---

## Exercise 1: Creating Arrays (5 minutes)

### Question 1.1
Create a 1D NumPy array from the list `[1, 2, 3, 4, 5]` and print it.

<details>
<summary>Hint</summary>
Use `np.array()` with a Python list.
</details>

---

### Question 1.2
Create a 2D NumPy array from the nested list `[[1, 2, 3], [4, 5, 6]]` and print it.

<details>
<summary>Hint</summary>
Pass a nested list to `np.array()`.
</details>

---

### Question 1.3
Create a 1D array of 5 zeros using `np.zeros()`. Then create a 2D array of 3x4 ones using `np.ones()`.

<details>
<summary>Hint</summary>
For 2D arrays, pass a tuple: `(rows, columns)`.
</details>

---

### Question 1.4
Create an array with numbers from 0 to 9 using `np.arange()`. Then create an array with 5 evenly spaced numbers from 0 to 10 using `np.linspace()`.

<details>
<summary>Hint</summary>
`np.arange(10)` gives 0-9, `np.linspace(0, 10, 5)` gives 5 evenly spaced numbers.
</details>

---

## Exercise 2: Array Shape and Properties (5 minutes)

### Question 2.1
Create a 2D array `arr = np.array([[1, 2, 3], [4, 5, 6]])`. Print:
- The shape of the array
- The number of dimensions
- The total number of elements

<details>
<summary>Hint</summary>
Use `.shape`, `.ndim`, and `.size` attributes.
</details>

---

### Question 2.2
Create an array `arr = np.array([1, 2, 3, 4, 5, 6])`. Reshape it to a 2x3 array (2 rows, 3 columns) and print it.

<details>
<summary>Hint</summary>
Use `.reshape(2, 3)` method.
</details>

---

## Exercise 3: Array Indexing (5 minutes)

### Question 3.1
Create an array `arr = np.array([10, 20, 30, 40, 50])`. Print:
- The first element
- The last element
- The third element

<details>
<summary>Hint</summary>
Use indexing: `arr[0]`, `arr[-1]`, `arr[2]`.
</details>

---

### Question 3.2
Create a 2D array `arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])`. Print:
- The element at row 0, column 1
- The element at row 2, column 0
- The entire first row
- The entire second column

<details>
<summary>Hint</summary>
Use `[row, column]` for 2D indexing. Use `:` to get entire rows/columns.
</details>

---

## Exercise 4: Array Slicing (5 minutes)

### Question 4.1
Create an array `arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])`. Using slicing, create and print:
- Elements from index 2 to 5 (exclusive of 5)
- Elements from index 5 to the end
- Every 2nd element starting from 0

<details>
<summary>Hint</summary>
Use `[start:stop]` and `[start:stop:step]` syntax.
</details>

---

### Question 4.2
Create a 2D array `arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])`. Using slicing, extract and print:
- First 2 rows, first 3 columns
- All rows, columns 1 to 3

<details>
<summary>Hint</summary>
Use `[row_slice, column_slice]` format. Remember `:` means "all".
</details>

---

## Final Check

Before moving on, make sure you can:
- ✅ Create 1D and 2D NumPy arrays
- ✅ Use `np.zeros()`, `np.ones()`, `np.arange()`, `np.linspace()`
- ✅ Understand and get array shape
- ✅ Reshape arrays
- ✅ Index 1D and 2D arrays
- ✅ Slice arrays in 1D and 2D

---

## Tips for Learning

1. **Import NumPy first** - Always start with `import numpy as np`

2. **Check your arrays** - Use `print()` to see what your arrays look like

3. **Understand shape** - For 2D: `(rows, columns)` - think "how many rows, how many columns"

4. **Practice indexing** - Remember `[row, column]` for 2D arrays

5. **Experiment** - Try different slice ranges to see what happens

---

**Great job completing Day 4! 🎉**

You've learned the fundamentals of NumPy arrays. These skills are essential for data science and machine learning!

