# Day 12: Grouping and Aggregation Exercises — `groupby()` with `.agg()`, `.count()`, `.mean()`

**Estimated Time: 25 minutes**

**Instructions:**
- Read each question carefully - they're designed to be easy!
- Try to solve it yourself before checking the solution
- Type out the code (don't just read it) — this helps you remember
- If you get stuck, read the hint, then try again
- Check the solutions in `day12_solution.md` only after you've attempted the problem
- Remember: `import pandas as pd` at the start!

---

## Exercise 1: Basic Grouping (8 minutes)

### Question 1.1
Create a DataFrame:
```python
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank'],
    'City': ['New York', 'Los Angeles', 'New York', 'Chicago', 'Los Angeles', 'Chicago'],
    'Score': [85, 90, 78, 92, 88, 75]
})
```

Then:
- Group by 'City' and count how many people are in each city
- Print the result

<details>
<summary>Hint</summary>
Use `df.groupby('City')['Name'].count()` or `df.groupby('City').size()`.
</details>

---

### Question 1.2
Using the same DataFrame from Question 1.1:
- Group by 'City' and calculate the average score for each city
- Print the result

<details>
<summary>Hint</summary>
Use `df.groupby('City')['Score'].mean()`. Don't forget to select the 'Score' column!
</details>

---

### Question 1.3
Using the same DataFrame:
- Group by 'City' and calculate both the minimum and maximum score for each city
- Use `.agg()` with a list of functions: `['min', 'max']`
- Print the result

<details>
<summary>Hint</summary>
Use `df.groupby('City')['Score'].agg(['min', 'max'])`.
</details>

---

## Exercise 2: Using `.agg()` Method (9 minutes)

### Question 2.1
Create a DataFrame:
```python
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank'],
    'Department': ['Sales', 'Sales', 'IT', 'IT', 'Sales', 'IT'],
    'Score': [85, 90, 78, 92, 88, 75],
    'Age': [25, 30, 35, 28, 22, 40]
})
```

Then:
- Group by 'Department'
- Use `.agg()` to calculate:
  - Average 'Score' for each department
  - Count of 'Name' for each department
- Print the result

<details>
<summary>Hint</summary>
Use `df.groupby('Department').agg({'Score': 'mean', 'Name': 'count'})`.
</details>

---

### Question 2.2
Using the same DataFrame from Question 2.1:
- Group by 'Department'
- Use `.agg()` to calculate multiple statistics for 'Score':
  - Mean, minimum, maximum, and count
- Print the result

<details>
<summary>Hint</summary>
Use `df.groupby('Department')['Score'].agg(['mean', 'min', 'max', 'count'])`.
</details>

---

### Question 2.3
Using the same DataFrame:
- Group by 'Department'
- Use `.agg()` to calculate:
  - For 'Score': mean and max
  - For 'Age': mean and min
  - For 'Name': count
- Print the result

<details>
<summary>Hint</summary>
Use a dictionary in `.agg()`: `agg({'Score': ['mean', 'max'], 'Age': ['mean', 'min'], 'Name': 'count'})`.
</details>

---

## Exercise 3: Multiple Grouping and Real-World Scenarios (8 minutes)

### Question 3.1
Create a DataFrame:
```python
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank', 'Grace', 'Henry'],
    'City': ['New York', 'New York', 'Chicago', 'Chicago', 'New York', 'Chicago', 'New York', 'Chicago'],
    'Department': ['Sales', 'IT', 'Sales', 'IT', 'Sales', 'IT', 'Sales', 'IT'],
    'Score': [85, 90, 78, 92, 88, 75, 95, 82]
})
```

Then:
- Group by both 'City' and 'Department'
- Calculate the average score for each combination
- Print the result

<details>
<summary>Hint</summary>
Use `df.groupby(['City', 'Department'])['Score'].mean()`. Pass a list of column names for multiple grouping.
</details>

---

### Question 3.2
Using the same DataFrame from Question 3.1:
- Group by 'City'
- Calculate the total count of people and average score for each city
- Print the result

<details>
<summary>Hint</summary>
Use `df.groupby('City').agg({'Name': 'count', 'Score': 'mean'})`.
</details>

---

### Question 3.3
Create a DataFrame with sales data:
```python
df = pd.DataFrame({
    'Product': ['A', 'A', 'B', 'B', 'C', 'C', 'A', 'B'],
    'Salesperson': ['John', 'Jane', 'John', 'Jane', 'John', 'Jane', 'John', 'Jane'],
    'Sales': [100, 150, 200, 180, 120, 130, 110, 190]
})
```

Then:
- Group by 'Product'
- Calculate the total sales and average sales for each product
- Print the result

<details>
<summary>Hint</summary>
Use `df.groupby('Product').agg({'Sales': ['sum', 'mean']})`.
</details>

---

## Final Check

Before moving on, make sure you can:
- ✅ Use `groupby()` to group data by a column
- ✅ Use `.count()` to count items in each group
- ✅ Use `.mean()` to calculate averages for each group
- ✅ Use `.agg()` with a dictionary for multiple statistics
- ✅ Use `.agg()` with a list for multiple functions on one column
- ✅ Group by multiple columns using a list
- ✅ Select specific columns before aggregating

---

## Tips for Success

1. **Always select columns** - Use `df.groupby('Col')['Score'].mean()` not just `df.groupby('Col').mean()`

2. **Use `.agg()` for multiple functions** - It's cleaner than calling multiple methods

3. **Remember the syntax** - `.agg({'Column': 'function'})` uses a dictionary

4. **Test your results** - Print and verify the output makes sense

5. **Start simple** - Get one groupby working, then add complexity

---

**You're doing great! Grouping and aggregation are powerful tools for data analysis. 🎉**

Remember: Practice makes perfect. Keep trying and you'll get comfortable with grouping data!

