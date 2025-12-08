# Day 5: NumPy Operations Exercises — Mathematical Operations and Aggregation

**Estimated Time: 20 minutes**

**Instructions:**
- Read each question carefully - they're designed to be easy!
- Try to solve it yourself before checking the solution
- Type out the code (don't just read it) — this helps you remember
- If you get stuck, read the hint, then try again
- Check the solutions in `day5_solution.md` only after you've attempted the problem
- Remember: `import numpy as np` at the start!

---

## Exercise 1: Basic Math Operations (Easy!) (6 minutes)

### Question 1.1
Create two arrays: `arr1 = np.array([1, 2, 3])` and `arr2 = np.array([4, 5, 6])`. 
- Add them together and print the result
- Subtract arr2 from arr1 and print the result

<details>
<summary>Hint</summary>
Just use + and - between the arrays. NumPy does the rest!
</details>

---

### Question 1.2
Create an array `arr = np.array([2, 4, 6, 8, 10])`. 
- Multiply every number by 3
- Add 5 to every number
- Print both results

<details>
<summary>Hint</summary>
You can do operations with a single number: `arr * 3` or `arr + 5`
</details>

---

### Question 1.3
Create an array `arr = np.array([1, 2, 3, 4, 5])`. 
- Square each number (raise to power of 2)
- Print the result

<details>
<summary>Hint</summary>
Use `**` for power: `arr ** 2` means "each number to the power of 2"
</details>

---

## Exercise 2: Aggregation Functions (Easy!) (8 minutes)

### Question 2.1
Create an array `scores = np.array([85, 90, 78, 92, 88])`. 
- Find and print the sum (total) of all scores
- Find and print the mean (average) of all scores

<details>
<summary>Hint</summary>
Use `.sum()` for total and `.mean()` for average
</details>

---

### Question 2.2
Create an array `temperatures = np.array([72, 75, 68, 80, 73])`. 
- Find and print the maximum (hottest) temperature
- Find and print the minimum (coldest) temperature

<details>
<summary>Hint</summary>
Use `.max()` for biggest and `.min()` for smallest
</details>

---

### Question 2.3
Create an array `numbers = np.array([10, 20, 30, 40, 50])`. 
- Find and print the standard deviation
- (Don't worry about understanding what it means yet - just practice using it!)

<details>
<summary>Hint</summary>
Use `.std()` to find standard deviation
</details>

---

## Exercise 3: 2D Arrays (Easy!) (6 minutes)

### Question 3.1
Create a 2D array: `arr = np.array([[1, 2, 3], [4, 5, 6]])`
- Find and print the sum of ALL numbers
- Find and print the sum of each ROW (use `axis=1`)
- Find and print the sum of each COLUMN (use `axis=0`)

<details>
<summary>Hint</summary>
- `arr.sum()` for all numbers
- `arr.sum(axis=1)` for rows (across)
- `arr.sum(axis=0)` for columns (down)
</details>

---

### Question 3.2
Create a 2D array: `grades = np.array([[85, 90, 88], [78, 82, 80]])`
- Find and print the average of ALL grades
- Find and print the average of each ROW (each student's average)

<details>
<summary>Hint</summary>
- `grades.mean()` for all grades
- `grades.mean(axis=1)` for each row (student)
</details>

---

## Final Check

Before moving on, make sure you can:
- ✅ Add, subtract, multiply arrays
- ✅ Do operations with a single number (like `arr * 2`)
- ✅ Find sum, mean, max, min of an array
- ✅ Use `axis=0` and `axis=1` for 2D arrays
- ✅ Understand that operations work on entire arrays at once

---

## Tips for Success

1. **Don't rush** - Take your time with each question
2. **Print everything** - See what your code produces
3. **Start simple** - If a question seems hard, break it into smaller steps
4. **It's okay to make mistakes** - That's how we learn!
5. **Ask for help** - If you're really stuck, check the solution and try to understand it

---

**You're doing great! These exercises are designed to build your confidence. 🎉**

Remember: Every expert was once a beginner. Keep practicing and you'll get it!

