# Day 11: DataFrame Operations Exercises — Adding/Removing Columns and `.apply()`

**Estimated Time: 25 minutes**

**Instructions:**
- Read each question carefully - they're designed to be easy!
- Try to solve it yourself before checking the solution
- Type out the code (don't just read it) — this helps you remember
- If you get stuck, read the hint, then try again
- Check the solutions in `day11_solution.md` only after you've attempted the problem
- Remember: `import pandas as pd` at the start!

---

## Exercise 1: Adding Columns (10 minutes)

### Question 1.1
Create a DataFrame:
```python
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Age': [25, 30, 35, 28],
    'Score': [85, 90, 78, 92]
})
```

Then:
- Add a column 'Status' with the value 'Active' for all rows
- Add a column 'City' with values: ['New York', 'Los Angeles', 'Chicago', 'Houston']
- Print the DataFrame

<details>
<summary>Hint</summary>
Use simple assignment: `df['Status'] = 'Active'` and `df['City'] = [list of values]`.
</details>

---

### Question 1.2
Using the same DataFrame from Question 1.1:
- Add a column 'Total_Points' that is Age + Score for each row
- Add a column 'Score_Per_Age' that is Score divided by Age
- Print the DataFrame

<details>
<summary>Hint</summary>
Use calculations: `df['Total_Points'] = df['Age'] + df['Score']` and `df['Score_Per_Age'] = df['Score'] / df['Age']`.
</details>

---

### Question 1.3
Using the same DataFrame:
- Add a column 'Grade' where:
  - 'A' if Score >= 90
  - 'B' if Score >= 80
  - 'C' otherwise
- Use `.apply()` with a lambda function
- Print the DataFrame

<details>
<summary>Hint</summary>
Use: `df['Grade'] = df['Score'].apply(lambda x: 'A' if x >= 90 else 'B' if x >= 80 else 'C')`.
</details>

---

## Exercise 2: Removing Columns (6 minutes)

### Question 2.1
Create a DataFrame:
```python
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Score': [85, 90, 78],
    'City': ['NY', 'LA', 'CHI'],
    'Country': ['USA', 'USA', 'USA']
})
```

Then:
- Remove the 'City' column using `drop()`
- Remove the 'Country' column using `del`
- Print the DataFrame

<details>
<summary>Hint</summary>
Use `df = df.drop('City', axis=1)` and `del df['Country']`. Don't forget `axis=1`!
</details>

---

### Question 2.2
Using a new DataFrame:
```python
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Score': [85, 90, 78],
    'Temp1': [1, 2, 3],
    'Temp2': [4, 5, 6]
})
```

Remove both 'Temp1' and 'Temp2' columns in one operation, then print the DataFrame.

<details>
<summary>Hint</summary>
Use `df = df.drop(['Temp1', 'Temp2'], axis=1)` with a list of column names.
</details>

---

## Exercise 3: Using `.apply()` Method (9 minutes)

### Question 3.1
Create a DataFrame:
```python
df = pd.DataFrame({
    'Name': ['alice', 'bob', 'charlie']
})
```

Then:
- Use `.apply()` to convert all names to uppercase
- Print the DataFrame

<details>
<summary>Hint</summary>
Use `df['Name'] = df['Name'].apply(str.upper)` or `df['Name'] = df['Name'].apply(lambda x: x.upper())`.
</details>

---

### Question 3.2
Create a DataFrame:
```python
df = pd.DataFrame({
    'Numbers': [1, 2, 3, 4, 5]
})
```

Then:
- Use `.apply()` with a lambda function to create a new column 'Squared' that contains each number squared
- Print the DataFrame

<details>
<summary>Hint</summary>
Use `df['Squared'] = df['Numbers'].apply(lambda x: x ** 2)`.
</details>

---

### Question 3.3
Create a DataFrame:
```python
df = pd.DataFrame({
    'Score': [85, 90, 78, 92, 88]
})
```

Then:
- Use `.apply()` with a lambda function to create a column 'Result' where:
  - 'Pass' if Score >= 80
  - 'Fail' if Score < 80
- Print the DataFrame

<details>
<summary>Hint</summary>
Use `df['Result'] = df['Score'].apply(lambda x: 'Pass' if x >= 80 else 'Fail')`.
</details>

---

### Question 3.4
Create a DataFrame:
```python
df = pd.DataFrame({
    'Name': ['Alice Smith', 'Bob Johnson', 'Charlie Brown']
})
```

Then:
- Use `.apply()` with a lambda function to create a column 'Name_Length' that contains the length of each name
- Print the DataFrame

<details>
<summary>Hint</summary>
Use `df['Name_Length'] = df['Name'].apply(lambda x: len(x))`.
</details>

---

## Final Check

Before moving on, make sure you can:
- ✅ Add a column with a constant value
- ✅ Add a column with a list of values
- ✅ Add a calculated column from other columns
- ✅ Remove a column using `drop()` with `axis=1`
- ✅ Remove a column using `del`
- ✅ Remove multiple columns at once
- ✅ Use `.apply()` with lambda functions
- ✅ Use `.apply()` with built-in functions like `str.upper`

---

## Tips for Success

1. **Remember `axis=1`** - Always use it when dropping columns

2. **Reassign or use `inplace=True`** - When using `drop()`, either reassign (`df = df.drop(...)`) or use `inplace=True`

3. **Lambda syntax** - `lambda x: expression` where `x` is each value

4. **List length matters** - When adding a column with a list, it must match the number of rows

5. **Test your calculations** - Print intermediate results to make sure they're correct

---

**You're doing great! Learning to modify DataFrames is a crucial skill. 🎉**

Remember: Practice makes perfect. Keep trying and you'll get comfortable with adding, removing, and transforming columns!

