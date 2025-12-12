# Day 9: Inspecting Data Exercises — head(), tail(), info(), describe(), shape

**Estimated Time: 20 minutes**

**Instructions:**
- Read each question carefully - they're designed to be easy!
- Try to solve it yourself before checking the solution
- Type out the code (don't just read it) — this helps you remember
- If you get stuck, read the hint, then try again
- Check the solutions in `day9_solution.md` only after you've attempted the problem
- Remember: `import pandas as pd` at the start!

---

## Exercise 1: Creating and Inspecting Data (8 minutes)

### Question 1.1
Create a DataFrame with this data:
```python
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'Age': [25, 30, 35, 28, 22],
    'Score': [85, 90, 78, 92, 88]
}
df = pd.DataFrame(data)
```

Then:
- Print the first 3 rows using `head(3)`
- Print the last 2 rows using `tail(2)`
- Print the shape

<details>
<summary>Hint</summary>
Use `df.head(3)`, `df.tail(2)`, and `df.shape`. Don't forget to print them!
</details>

---

### Question 1.2
Using the same DataFrame from Question 1.1:
- Print `df.info()` to see information about the data
- Print `df.describe()` to see statistics
- What do you notice about the output of `describe()`? (Which columns are shown?)

<details>
<summary>Hint</summary>
Call `df.info()` and `df.describe()`. Notice that `describe()` only shows numeric columns (Age and Score), not the Name column.
</details>

---

### Question 1.3
Create a DataFrame with 10 rows:
```python
df = pd.DataFrame({
    'Product': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
    'Price': [10, 20, 15, 25, 30, 18, 22, 28, 12, 35],
    'Quantity': [5, 3, 7, 2, 4, 6, 8, 1, 9, 3]
})
```

Then:
- Print the first 5 rows (default)
- Print the last 5 rows (default)
- Print how many rows and columns using `shape`

<details>
<summary>Hint</summary>
Use `df.head()`, `df.tail()`, and `df.shape`. The shape should be (10, 3).
</details>

---

## Exercise 2: Understanding the Output (7 minutes)

### Question 2.1
Create this DataFrame:
```python
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Score': [85, 90, 78]
})
```

Answer these questions by inspecting the data:
- How many rows does it have? (Use `shape`)
- How many columns does it have? (Use `shape`)
- What is the average age? (Use `describe()`)

<details>
<summary>Hint</summary>
Use `df.shape` to get (rows, columns). Use `df.describe()` to see the mean age.
</details>

---

### Question 2.2
Using the same DataFrame from Question 2.1:
- What data type is the 'Name' column? (Check `info()`)
- What data type is the 'Age' column? (Check `info()`)
- What is the minimum score? (Use `describe()`)

<details>
<summary>Hint</summary>
Use `df.info()` to see data types (dtype). Use `df.describe()` to see min values.
</details>

---

### Question 2.3
Create a DataFrame and inspect it:
```python
df = pd.DataFrame({
    'City': ['New York', 'Los Angeles', 'Chicago'],
    'Population': [8000000, 4000000, 2700000],
    'Area': [783.8, 1302.0, 606.1]
})
```

- Print `info()` and identify: How many non-null values are in each column?
- Print `describe()` and identify: What is the mean population?
- What columns appear in `describe()` and why?

<details>
<summary>Hint</summary>
`info()` shows non-null counts. `describe()` shows mean and only includes numeric columns (Population and Area, not City).
</details>

---

## Exercise 3: Working with CSV Files (5 minutes)

### Question 3.1
First, create a CSV file called `students.csv` with this content:
```csv
Name,Age,Score,City
Alice,25,85,New York
Bob,30,90,Los Angeles
Charlie,35,78,Chicago
Diana,28,92,Houston
Eve,22,88,Phoenix
```

Then write Python code to:
- Read the CSV file
- Print the first 3 rows
- Print the shape
- Print `info()`

<details>
<summary>Hint</summary>
Use `pd.read_csv('students.csv')` to load, then use `head(3)`, `shape`, and `info()`.
</details>

---

### Question 3.2
After reading `students.csv`:
- Print `describe()` and identify the average age
- Print `tail()` to see the last rows
- Print how many rows and columns using `shape[0]` and `shape[1]`

<details>
<summary>Hint</summary>
Use `df.describe()` for average (mean), `df.tail()`, and `df.shape[0]` for rows, `df.shape[1]` for columns.
</details>

---

## Final Check

Before moving on, make sure you can:
- ✅ Use `head()` and `tail()` to view rows
- ✅ Use `info()` to get detailed information
- ✅ Use `describe()` to get statistics
- ✅ Use `shape` to get the size
- ✅ Understand what each method tells you
- ✅ Know that `describe()` only shows numeric columns

---

## Tips for Success

1. **Always inspect first** - Before doing anything with data, inspect it!

2. **Use all methods** - Don't just use one, use them together for a complete picture

3. **Read the output** - Take time to understand what each method shows

4. **Practice with real data** - Try inspecting CSV files you create

5. **Make it a habit** - Always inspect data after loading it

---

**You're doing great! Learning to inspect data is a crucial skill. 🎉**

Remember: A good data scientist always inspects their data first!

