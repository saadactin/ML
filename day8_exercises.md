# Day 8: Pandas Exercises — Series, DataFrames, and Reading CSV

**Estimated Time: 25 minutes**

**Instructions:**
- Read each question carefully - they're designed to be easy!
- Try to solve it yourself before checking the solution
- Type out the code (don't just read it) — this helps you remember
- If you get stuck, read the hint, then try again
- Check the solutions in `day8_solution.md` only after you've attempted the problem
- Remember: `import pandas as pd` at the start!

---

## Exercise 1: Series Basics (8 minutes)

### Question 1.1
Create a Series with the values `[10, 20, 30, 40, 50]` and print it.

<details>
<summary>Hint</summary>
Use `pd.Series([10, 20, 30, 40, 50])` and print it.
</details>

---

### Question 1.2
Create a Series with custom labels:
- Values: `[85, 90, 78, 92]`
- Labels: `['Alice', 'Bob', 'Charlie', 'Diana']`
- Print the Series
- Then print just Bob's score

<details>
<summary>Hint</summary>
Use `pd.Series(values, index=labels)`. Access Bob's score with `series['Bob']`.
</details>

---

### Question 1.3
Create a Series `scores = pd.Series([85, 90, 78, 92, 88])` and find:
- The average (mean)
- The maximum value
- The minimum value
- Print all three

<details>
<summary>Hint</summary>
Use `.mean()`, `.max()`, and `.min()` methods on the Series.
</details>

---

## Exercise 2: DataFrame Basics (10 minutes)

### Question 2.1
Create a DataFrame with this data:
- Names: `['Alice', 'Bob', 'Charlie']`
- Ages: `[25, 30, 35]`
- Scores: `[85, 90, 78]`
- Print the DataFrame

<details>
<summary>Hint</summary>
Use a dictionary: `pd.DataFrame({'Name': [...], 'Age': [...], 'Score': [...]})`
</details>

---

### Question 2.2
Using the DataFrame from Question 2.1:
- Print the first 2 rows using `.head(2)`
- Print the column names
- Print the shape (number of rows and columns)

<details>
<summary>Hint</summary>
Use `.head(2)`, `.columns`, and `.shape` on your DataFrame.
</details>

---

### Question 2.3
Using the same DataFrame:
- Get the 'Score' column and print it
- Calculate and print the average score
- Get both 'Name' and 'Score' columns and print them

<details>
<summary>Hint</summary>
Use `df['Score']` for one column, `df[['Name', 'Score']]` for multiple columns.
</details>

---

## Exercise 3: Reading CSV Files (7 minutes)

### Question 3.1
First, create a CSV file called `students.csv` with this data:
```
Name,Age,Score
Alice,25,85
Bob,30,90
Charlie,35,78
Diana,28,92
```

Then write Python code to:
- Read the CSV file using `pd.read_csv()`
- Print the DataFrame
- Print the first 3 rows

<details>
<summary>Hint</summary>
Create the CSV file in a text editor (like Notepad), save it as `students.csv` in the same folder as your Python script. Then use `pd.read_csv('students.csv')`.
</details>

---

### Question 3.2
After reading `students.csv`:
- Print basic information about the data using `.info()`
- Print statistics using `.describe()`
- Get the 'Score' column and print its average

<details>
<summary>Hint</summary>
Use `.info()`, `.describe()`, and `df['Score'].mean()`.
</details>

---

### Question 3.3
Using the same CSV file:
- Get and print the 'Name' column
- Get and print the 'Age' column
- Get and print both 'Name' and 'Score' columns together

<details>
<summary>Hint</summary>
Use `df['Name']`, `df['Age']`, and `df[['Name', 'Score']]`.
</details>

---

## Final Check

Before moving on, make sure you can:
- ✅ Create a Series from a list
- ✅ Create a DataFrame from a dictionary
- ✅ Access columns in a DataFrame
- ✅ Read a CSV file using `pd.read_csv()`
- ✅ Use `.head()`, `.info()`, `.describe()` to explore data
- ✅ Get basic statistics like `.mean()`, `.max()`, `.min()`

---

## Tips for Success

1. **Create the CSV file first** - For Exercise 3, you'll need to create a CSV file. Use a text editor like Notepad.

2. **Check your file location** - Make sure your CSV file is in the same folder as your Python script.

3. **Use print()** - Print everything to see what you're working with!

4. **Start simple** - Get a basic DataFrame working, then add more.

5. **Don't worry about errors** - If something doesn't work, check:
   - Did you import pandas? (`import pandas as pd`)
   - Is your CSV file in the right place?
   - Are your column names spelled correctly? (case-sensitive!)

---

**You're doing great! Pandas is a powerful tool, and you're learning the basics. 🎉**

Remember: Every expert was once a beginner. Keep practicing and you'll get comfortable with it!

