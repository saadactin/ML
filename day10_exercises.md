# Day 10: Selecting Data Exercises — Columns and Filtering Rows

**Estimated Time: 25 minutes**

**Instructions:**
- Read each question carefully - they're designed to be easy!
- Try to solve it yourself before checking the solution
- Type out the code (don't just read it) — this helps you remember
- If you get stuck, read the hint, then try again
- Check the solutions in `day10_solution.md` only after you've attempted the problem
- Remember: `import pandas as pd` at the start!
- **Important:** Use `&` for AND, `|` for OR, and always use parentheses!

---

## Exercise 1: Selecting Columns (8 minutes)

### Question 1.1
Create a DataFrame:
```python
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Age': [25, 30, 35, 28],
    'Score': [85, 90, 78, 92],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
})
```

Then:
- Select and print just the 'Name' column
- Select and print just the 'Age' column
- Select and print both 'Name' and 'Score' columns together

<details>
<summary>Hint</summary>
Use `df['Name']` for single column, `df[['Name', 'Score']]` for multiple columns (double brackets!).
</details>

---

### Question 1.2
Using the same DataFrame from Question 1.1:
- Select and print 'Name', 'Age', and 'City' columns together
- What type of object do you get when selecting one column vs multiple columns? (Check with `type()`)

<details>
<summary>Hint</summary>
Use `df[['Name', 'Age', 'City']]` for multiple columns. Use `type(df['Name'])` and `type(df[['Name', 'Age']])` to see the difference.
</details>

---

## Exercise 2: Basic Row Filtering (10 minutes)

### Question 2.1
Using the DataFrame from Question 1.1:
- Filter and print rows where Age is greater than 28
- Filter and print rows where Score is greater than or equal to 85

<details>
<summary>Hint</summary>
Use `df[df['Age'] > 28]` and `df[df['Score'] >= 85]`. Remember to use `==` for equality, not `=`.
</details>

---

### Question 2.2
Using the same DataFrame:
- Filter and print rows where Age equals 30
- Filter and print rows where City is 'New York'
- Filter and print rows where Score is less than 80

<details>
<summary>Hint</summary>
Use `==` for equality: `df[df['Age'] == 30]`, `df[df['City'] == 'New York']`, `df[df['Score'] < 80]`.
</details>

---

### Question 2.3
Create a new DataFrame with more data:
```python
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank'],
    'Age': [25, 30, 35, 28, 22, 40],
    'Score': [85, 90, 78, 92, 88, 75]
})
```

Then:
- Filter rows where Age is greater than 25 AND Score is greater than 85
- Print the result

<details>
<summary>Hint</summary>
Use `&` for AND: `df[(df['Age'] > 25) & (df['Score'] > 85)]`. Don't forget parentheses around each condition!
</details>

---

### Question 2.4
Using the same DataFrame from Question 2.3:
- Filter rows where Age is greater than 35 OR Score is less than 80
- Print the result

<details>
<summary>Hint</summary>
Use `|` for OR: `df[(df['Age'] > 35) | (df['Score'] < 80)]`. Remember parentheses!
</details>

---

## Exercise 3: Combining Selection and Filtering (7 minutes)

### Question 3.1
Using the DataFrame from Question 2.3:
- Filter rows where Score is greater than 85
- From those filtered rows, select only the 'Name' and 'Score' columns
- Print the result

<details>
<summary>Hint</summary>
Combine them: `df[df['Score'] > 85][['Name', 'Score']]`. Filter first, then select columns.
</details>

---

### Question 3.2
Using the same DataFrame:
- Filter rows where Age is between 25 and 35 (inclusive)
- From those filtered rows, select only the 'Name' and 'Age' columns
- Print the result

<details>
<summary>Hint</summary>
Use `>=` and `<=` with `&`: `df[(df['Age'] >= 25) & (df['Age'] <= 35)][['Name', 'Age']]`.
</details>

---

### Question 3.3
Create a DataFrame:
```python
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'Age': [25, 30, 35, 28, 22],
    'Score': [85, 90, 78, 92, 88],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
})
```

Then:
- Filter rows where Score is greater than 85 AND City is 'New York' OR 'Los Angeles'
- From those rows, select 'Name', 'Score', and 'City' columns
- Print the result

<details>
<summary>Hint</summary>
You can use `.isin()` for multiple values: `df[(df['Score'] > 85) & (df['City'].isin(['New York', 'Los Angeles']))][['Name', 'Score', 'City']]`.
</details>

---

## Final Check

Before moving on, make sure you can:
- ✅ Select a single column using `df['ColumnName']`
- ✅ Select multiple columns using `df[['Col1', 'Col2']]` (double brackets!)
- ✅ Filter rows with simple conditions (`>`, `<`, `==`, etc.)
- ✅ Combine conditions with `&` (AND) and `|` (OR)
- ✅ Use parentheses when combining conditions
- ✅ Combine filtering and column selection
- ✅ Understand the difference between single and double brackets

---

## Tips for Success

1. **Remember the brackets:**
   - Single `[]` for one column → Series
   - Double `[[]]` for multiple columns → DataFrame

2. **Use parentheses:**
   - Always use `(condition1) & (condition2)`
   - Not `condition1 & condition2` (will cause errors!)

3. **Filter then select:**
   - `df[condition][['Col1', 'Col2']]` is clearer than the reverse

4. **Test your conditions:**
   - Print the condition first: `print(df['Age'] > 30)` to see True/False

5. **Read it out loud:**
   - "Get rows where Age is greater than 30" helps you write the code

---

**You're doing great! Selecting and filtering data is a fundamental skill. 🎉**

Remember: Practice makes perfect. Keep trying and you'll get comfortable with it!

