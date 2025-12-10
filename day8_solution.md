# Day 8: Pandas Exercises — Solutions

**Note:** Only check these solutions after you've attempted the problems yourself!

Remember: The goal is to understand how to work with Series, DataFrames, and CSV files. Take your time! 💪

---

## Exercise 1: Series Basics

### Solution 1.1

```python
import pandas as pd

# Create a Series
series = pd.Series([10, 20, 30, 40, 50])
print(series)
```

**Output:**
```
0    10
1    20
2    30
3    40
4    50
dtype: int64
```

**Explanation:** This creates a simple Series with default index (0, 1, 2, 3, 4).

---

### Solution 1.2

```python
import pandas as pd

# Create Series with custom labels
scores = pd.Series([85, 90, 78, 92], 
                   index=['Alice', 'Bob', 'Charlie', 'Diana'])

# Print the Series
print(scores)

# Print just Bob's score
print("\nBob's score:", scores['Bob'])
```

**Output:**
```
Alice      85
Bob        90
Charlie    78
Diana      92
dtype: int64

Bob's score: 90
```

**Explanation:** 
- The `index` parameter gives custom labels to each value
- Access a value using `series['label']` or `series[label]`

---

### Solution 1.3

```python
import pandas as pd

# Create Series
scores = pd.Series([85, 90, 78, 92, 88])

# Calculate statistics
average = scores.mean()
maximum = scores.max()
minimum = scores.min()

# Print results
print(f"Average: {average}")
print(f"Maximum: {maximum}")
print(f"Minimum: {minimum}")
```

**Output:**
```
Average: 86.6
Maximum: 92
Minimum: 78
```

**Explanation:**
- `.mean()` calculates the average: (85+90+78+92+88) ÷ 5 = 86.6
- `.max()` finds the highest value: 92
- `.min()` finds the lowest value: 78

---

## Exercise 2: DataFrame Basics

### Solution 2.1

```python
import pandas as pd

# Create DataFrame from dictionary
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Score': [85, 90, 78]
})

print(df)
```

**Output:**
```
      Name  Age  Score
0    Alice   25     85
1      Bob   30     90
2  Charlie   35     78
```

**Explanation:** 
- Each key in the dictionary becomes a column name
- Each value (list) becomes the data in that column
- Pandas automatically adds row numbers (0, 1, 2)

---

### Solution 2.2

```python
import pandas as pd

# Create DataFrame (same as 2.1)
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Score': [85, 90, 78]
})

# Print first 2 rows
print("First 2 rows:")
print(df.head(2))

# Print column names
print("\nColumn names:")
print(df.columns)

# Print shape
print("\nShape (rows, columns):")
print(df.shape)
```

**Output:**
```
First 2 rows:
    Name  Age  Score
0  Alice   25     85
1    Bob   30     90

Column names:
Index(['Name', 'Age', 'Score'], dtype='object')

Shape (rows, columns):
(3, 3)
```

**Explanation:**
- `.head(2)` shows the first 2 rows (default is 5)
- `.columns` shows all column names
- `.shape` returns a tuple: (number of rows, number of columns)

---

### Solution 2.3

```python
import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Score': [85, 90, 78]
})

# Get the 'Score' column
scores = df['Score']
print("Score column:")
print(scores)

# Calculate average score
average_score = scores.mean()
print(f"\nAverage score: {average_score}")

# Get both 'Name' and 'Score' columns
name_score = df[['Name', 'Score']]
print("\nName and Score columns:")
print(name_score)
```

**Output:**
```
Score column:
0    85
1    90
2    78
Name: Score, dtype: int64

Average score: 84.33333333333333

Name and Score columns:
      Name  Score
0    Alice     85
1      Bob     90
2  Charlie     78
```

**Explanation:**
- `df['Score']` gets one column (returns a Series)
- `df[['Name', 'Score']]` gets multiple columns (returns a DataFrame)
- Note the double brackets `[[]]` for multiple columns!

---

## Exercise 3: Reading CSV Files

### Solution 3.1

**Step 1: Create the CSV file**

Create a file named `students.csv` in the same folder as your Python script with this content:
```csv
Name,Age,Score
Alice,25,85
Bob,30,90
Charlie,35,78
Diana,28,92
```

**Step 2: Read and display the CSV**

```python
import pandas as pd

# Read the CSV file
df = pd.read_csv('students.csv')

# Print the DataFrame
print("Full DataFrame:")
print(df)

# Print first 3 rows
print("\nFirst 3 rows:")
print(df.head(3))
```

**Output:**
```
Full DataFrame:
      Name  Age  Score
0    Alice   25     85
1      Bob   30     90
2  Charlie   35     78
3    Diana   28     92

First 3 rows:
      Name  Age  Score
0    Alice   25     85
1      Bob   30     90
2  Charlie   35     78
```

**Explanation:**
- `pd.read_csv('students.csv')` reads the file and creates a DataFrame
- The first row of the CSV becomes the column names
- Each subsequent row becomes a data row

**Note:** Make sure `students.csv` is in the same folder as your Python script!

---

### Solution 3.2

```python
import pandas as pd

# Read the CSV file
df = pd.read_csv('students.csv')

# Print basic information
print("DataFrame Info:")
print(df.info())

# Print statistics
print("\nStatistics:")
print(df.describe())

# Get average score
average_score = df['Score'].mean()
print(f"\nAverage Score: {average_score}")
```

**Output:**
```
DataFrame Info:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 4 entries, 0 to 3
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   Name    4 non-null      object
 1   Age     4 non-null      int64
 2   Score   4 non-null      int64
dtypes: int64(2), object(1)
memory usage: 224.0+ bytes
None

Statistics:
             Age      Score
count   4.000000   4.000000
mean   29.500000  86.250000
std     4.509250   6.344288
min    25.000000  78.000000
25%    26.750000  82.250000
50%    29.000000  87.500000
75%    32.250000  89.750000
max    35.000000  92.000000

Average Score: 86.25
```

**Explanation:**
- `.info()` shows data types, number of rows, and memory usage
- `.describe()` shows statistics (count, mean, std, min, max, etc.) for numeric columns
- `.mean()` on a column gives the average of that column

---

### Solution 3.3

```python
import pandas as pd

# Read the CSV file
df = pd.read_csv('students.csv')

# Get and print the 'Name' column
print("Name column:")
print(df['Name'])

# Get and print the 'Age' column
print("\nAge column:")
print(df['Age'])

# Get and print both 'Name' and 'Score' columns
print("\nName and Score columns:")
print(df[['Name', 'Score']])
```

**Output:**
```
Name column:
0      Alice
1        Bob
2    Charlie
3      Diana
Name: Name, dtype: object

Age column:
0    25
1    30
2    35
3    28
Name: Age, dtype: int64

Name and Score columns:
      Name  Score
0    Alice     85
1      Bob     90
2  Charlie     78
3    Diana     92
```

**Explanation:**
- `df['Name']` gets one column (returns a Series)
- `df['Age']` gets another column (returns a Series)
- `df[['Name', 'Score']]` gets multiple columns (returns a DataFrame)
- Remember: single brackets `[]` for one column, double brackets `[[]]` for multiple columns!

---

## Additional Practice Ideas

Once you're comfortable with these, try:

1. **Create your own CSV file:**
   - Make a CSV with your own data (maybe your expenses, scores, etc.)
   - Read it and explore it

2. **Experiment with different operations:**
   ```python
   df = pd.read_csv('students.csv')
   # Try these:
   print(df.tail())  # Last rows
   print(df['Age'].sum())  # Sum of ages
   print(df['Score'].max())  # Highest score
   ```

3. **Create DataFrames from your own data:**
   ```python
   # Your own data
   my_data = pd.DataFrame({
       'Item': ['Coffee', 'Lunch', 'Dinner'],
       'Cost': [5, 12, 25]
   })
   print(my_data)
   ```

---

## Common Questions

**Q: My CSV file isn't being found. What do I do?**
A: Make sure:
   - The CSV file is in the same folder as your Python script
   - The filename is spelled correctly (case-sensitive!)
   - Or use the full path: `pd.read_csv('C:/Users/.../file.csv')`

**Q: What's the difference between Series and DataFrame?**
A: 
   - **Series** = one column (like a list with labels)
   - **DataFrame** = multiple columns (like a table)

**Q: Why do I use double brackets for multiple columns?**
A: 
   - `df['Name']` = one column → Series
   - `df[['Name', 'Score']]` = multiple columns → DataFrame
   - The outer brackets are for "get these columns", inner brackets create a list of column names

**Q: Can I read Excel files too?**
A: Yes! Use `pd.read_excel('file.xlsx')` (but you need to install openpyxl: `pip install openpyxl`)

**Q: What if my CSV has different separators (not commas)?**
A: Use the `sep` parameter: `pd.read_csv('file.csv', sep=';')` for semicolons

---

## Key Takeaways

✅ **Series** = One column of data with labels

✅ **DataFrame** = A table with rows and columns (like Excel)

✅ **Read CSV** = `pd.read_csv('filename.csv')` - super simple!

✅ **Access columns** = `df['ColumnName']` for one, `df[['Col1', 'Col2']]` for multiple

✅ **Explore data** = `.head()`, `.tail()`, `.info()`, `.describe()`

✅ **Statistics** = `.mean()`, `.max()`, `.min()`, `.sum()` on columns

✅ **Always import** = `import pandas as pd`

---

## Final Reminder

**The most important things to remember:**
1. **Series** = one column
2. **DataFrame** = a table
3. **CSV** = a simple file format
4. **pd.read_csv()** = how you load data
5. **Always explore** = use `.head()`, `.info()`, `.describe()` to see what you have

**Great job completing the exercises! 🎉**

You've learned the basics of Pandas - Series, DataFrames, and reading CSV files. These are the foundation for working with data in Python. Keep practicing and you'll get more comfortable!

