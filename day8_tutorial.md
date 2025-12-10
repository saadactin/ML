# Day 8: Introduction to Pandas — Series, DataFrames, and Reading CSV Files

## Introduction

**Pandas** is a powerful library for working with data in Python. Think of it as Excel for Python!

**Why Pandas?**
- **Organize data** — Like a spreadsheet, but in code
- **Easy to use** — Simple commands for complex operations
- **Handle large data** — Works with millions of rows
- **Read files** — Easily load data from CSV, Excel, etc.

**What we'll learn today:**
- **Series** — A single column of data
- **DataFrames** — A table with rows and columns (like Excel)
- **Reading CSV files** — Loading data from files

**Don't worry!** We'll go step by step. Pandas might seem big, but we'll start with the basics. You've got this! 💪

---

## 1. Getting Started with Pandas

### Installation

If Pandas isn't installed:
```bash
pip install pandas
```

### Importing Pandas

The standard way to import:
```python
import pandas as pd
```

We use `pd` as a short name (everyone does this).

---

## 2. Series — A Single Column of Data

### What is a Series?

A **Series** is like a single column in a spreadsheet. It's a list with labels (indices).

**Simple analogy:** Think of it like a list, but better!

### Creating a Series

```python
import pandas as pd

# Create a Series from a list
ages = pd.Series([25, 30, 35, 40, 45])
print(ages)
```

**Output:**
```
0    25
1    30
2    35
3    40
4    45
dtype: int64
```

**What you see:**
- Left column: index (position number)
- Right column: values (the actual data)
- `dtype`: the type of data (int64 = integers)

### Series with Custom Labels

You can give your Series custom labels (like row names):

```python
import pandas as pd

# Create Series with custom labels
scores = pd.Series([85, 90, 78, 92], 
                   index=['Alice', 'Bob', 'Charlie', 'Diana'])
print(scores)
```

**Output:**
```
Alice      85
Bob        90
Charlie    78
Diana      92
dtype: int64
```

**Much clearer!** Now we can see who has which score.

### Accessing Series Data

```python
import pandas as pd

scores = pd.Series([85, 90, 78, 92], 
                   index=['Alice', 'Bob', 'Charlie', 'Diana'])

# Get a single value
print(scores['Alice'])  # 85

# Get multiple values
print(scores[['Alice', 'Bob']])
# Alice    85
# Bob      90

# Get by position (like a list)
print(scores[0])  # 85 (first value)
```

### Basic Series Operations

```python
import pandas as pd

scores = pd.Series([85, 90, 78, 92, 88])

# Find statistics
print(scores.mean())  # Average: 86.6
print(scores.max())  # Maximum: 92
print(scores.min())  # Minimum: 78
print(scores.sum())  # Total: 433
```

**That's it!** Super easy to get statistics.

---

## 3. DataFrames — Tables of Data

### What is a DataFrame?

A **DataFrame** is like an Excel spreadsheet or a table. It has:
- **Rows** — Each row is one record (like one person)
- **Columns** — Each column is one type of information (like name, age, score)

**Simple analogy:** Think of a DataFrame as a table with rows and columns.

### Creating a DataFrame

**Method 1: From a dictionary**

```python
import pandas as pd

# Create DataFrame from dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Age': [25, 30, 35, 28],
    'Score': [85, 90, 78, 92]
}

df = pd.DataFrame(data)
print(df)
```

**Output:**
```
      Name  Age  Score
0    Alice   25     85
1      Bob   30     90
2  Charlie   35     78
3    Diana   28     92
```

**What you see:**
- Column names at the top: Name, Age, Score
- Row numbers on the left: 0, 1, 2, 3
- Data in the middle

**Method 2: From a list of lists**

```python
import pandas as pd

# Create DataFrame from list of lists
data = [
    ['Alice', 25, 85],
    ['Bob', 30, 90],
    ['Charlie', 35, 78],
    ['Diana', 28, 92]
]

df = pd.DataFrame(data, columns=['Name', 'Age', 'Score'])
print(df)
```

**Same result!** Just a different way to create it.

### Viewing Your DataFrame

```python
import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Age': [25, 30, 35, 28],
    'Score': [85, 90, 78, 92]
})

# See first few rows
print(df.head())  # First 5 rows by default
print(df.head(2))  # First 2 rows

# See last few rows
print(df.tail())  # Last 5 rows
print(df.tail(2))  # Last 2 rows

# See basic info
print(df.info())  # Data types, number of rows, etc.

# See statistics
print(df.describe())  # Mean, min, max, etc. for numeric columns
```

### Accessing DataFrame Data

**Get a column:**
```python
import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Score': [85, 90, 78]
})

# Get a column (returns a Series)
ages = df['Age']
print(ages)
# 0    25
# 1    30
# 2    35

# Or use dot notation
ages = df.Age  # Same thing!
```

**Get multiple columns:**
```python
# Get multiple columns
subset = df[['Name', 'Score']]
print(subset)
```

**Get a row:**
```python
# Get first row
first_row = df.iloc[0]  # iloc = integer location
print(first_row)

# Get row by label (if you have custom index)
# row = df.loc['label']
```

**Get a specific value:**
```python
# Get Alice's score
alice_score = df.loc[0, 'Score']  # Row 0, Column 'Score'
print(alice_score)  # 85

# Or simpler:
alice_score = df['Score'][0]
print(alice_score)  # 85
```

### Basic DataFrame Operations

```python
import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Score': [85, 90, 78]
})

# Get number of rows and columns
print(df.shape)  # (3, 3) - 3 rows, 3 columns

# Get column names
print(df.columns)  # ['Name', 'Age', 'Score']

# Get basic statistics for numeric columns
print(df.describe())
```

---

## 4. Reading CSV Files — Loading Real Data

### What is a CSV File?

**CSV** = Comma-Separated Values. It's a simple text file that stores data in rows and columns.

**Example CSV file (`students.csv`):**
```
Name,Age,Score
Alice,25,85
Bob,30,90
Charlie,35,78
Diana,28,92
```

**Looks like:** A simple table saved as text!

### Reading a CSV File

**The magic command:** `pd.read_csv()`

```python
import pandas as pd

# Read a CSV file
df = pd.read_csv('students.csv')

# That's it! Now df contains your data
print(df)
```

**Output:**
```
      Name  Age  Score
0    Alice   25     85
1      Bob   30     90
2  Charlie   35     78
3    Diana   28     92
```

**It's that simple!** Pandas automatically:
- Reads the file
- Creates a DataFrame
- Uses the first row as column names
- Organizes everything nicely

### Common CSV Reading Options

```python
import pandas as pd

# Basic reading
df = pd.read_csv('data.csv')

# If your CSV doesn't have headers (column names)
df = pd.read_csv('data.csv', header=None)

# If you want to specify column names
df = pd.read_csv('data.csv', names=['Name', 'Age', 'Score'])

# If you only want certain columns
df = pd.read_csv('data.csv', usecols=['Name', 'Score'])

# If you only want first 100 rows (for large files)
df = pd.read_csv('data.csv', nrows=100)
```

### Creating a Sample CSV File for Practice

You can create a CSV file in a text editor or in Python:

**Create `students.csv` file:**
```csv
Name,Age,Score,City
Alice,25,85,New York
Bob,30,90,Los Angeles
Charlie,35,78,Chicago
Diana,28,92,Houston
```

**Or create it in Python:**
```python
import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Age': [25, 30, 35, 28],
    'Score': [85, 90, 78, 92],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
})

# Save to CSV
df.to_csv('students.csv', index=False)
print("File saved!")
```

### After Reading a CSV

Once you've read a CSV, you can do everything we learned:

```python
import pandas as pd

# Read the file
df = pd.read_csv('students.csv')

# View the data
print(df.head())

# Get a column
scores = df['Score']
print(scores.mean())  # Average score

# Get statistics
print(df.describe())

# Filter data (we'll learn more about this later)
high_scores = df[df['Score'] > 85]
print(high_scores)
```

---

## 5. Common Patterns and Examples

### Pattern 1: Load and Explore Data

```python
import pandas as pd

# Load data
df = pd.read_csv('data.csv')

# Explore
print("Shape:", df.shape)  # How many rows and columns?
print("\nFirst few rows:")
print(df.head())
print("\nColumn names:")
print(df.columns)
print("\nStatistics:")
print(df.describe())
```

### Pattern 2: Work with Specific Columns

```python
import pandas as pd

df = pd.read_csv('students.csv')

# Get one column
ages = df['Age']
print("Average age:", ages.mean())

# Get multiple columns
subset = df[['Name', 'Score']]
print(subset)
```

### Pattern 3: Basic Statistics

```python
import pandas as pd

df = pd.read_csv('students.csv')

# For one column
print("Score statistics:")
print(f"Average: {df['Score'].mean()}")
print(f"Highest: {df['Score'].max()}")
print(f"Lowest: {df['Score'].min()}")

# For all numeric columns
print("\nAll statistics:")
print(df.describe())
```

---

## 6. Common Mistakes (And How to Avoid Them)

### Mistake 1: File Not Found

```python
# ❌ WRONG - File doesn't exist
df = pd.read_csv('myfile.csv')  # FileNotFoundError!

# ✅ CORRECT - Check if file exists first
# Make sure the file is in the same folder as your Python script
# Or use the full path: pd.read_csv('C:/Users/.../myfile.csv')
```

**Solution:** Make sure your CSV file is in the same folder as your Python script, or use the full path.

### Mistake 2: Wrong Column Name

```python
# ❌ WRONG - Column name doesn't exist
score = df['score']  # KeyError! (case-sensitive)

# ✅ CORRECT - Use exact column name
score = df['Score']  # Capital S!
```

**Solution:** Column names are case-sensitive. Use exact names.

### Mistake 3: Forgetting to Import Pandas

```python
# ❌ WRONG
read_csv('data.csv')  # NameError!

# ✅ CORRECT
import pandas as pd
df = pd.read_csv('data.csv')
```

### Mistake 4: Confusing Series and DataFrame

```python
df = pd.DataFrame({'Name': ['Alice'], 'Age': [25]})

# Series (one column)
ages = df['Age']  # This is a Series
print(type(ages))  # <class 'pandas.core.series.Series'>

# DataFrame (multiple columns or whole table)
subset = df[['Name', 'Age']]  # This is a DataFrame
print(type(subset))  # <class 'pandas.core.frame.DataFrame'>
```

---

## 7. Quick Reference

### Series
```python
# Create
s = pd.Series([1, 2, 3], index=['a', 'b', 'c'])

# Access
s['a']  # Get value
s.mean()  # Average
```

### DataFrame
```python
# Create
df = pd.DataFrame({'Col1': [1, 2], 'Col2': [3, 4]})

# Access
df['Col1']  # Get column
df.head()  # First rows
df.shape  # (rows, columns)
```

### Read CSV
```python
# Read
df = pd.read_csv('file.csv')

# View
df.head()  # First 5 rows
df.info()  # Information about data
df.describe()  # Statistics
```

---

## Key Takeaways (Simple Summary)

1. **Series** = One column of data (like a list with labels)
2. **DataFrame** = A table with rows and columns (like Excel)
3. **Read CSV** = `pd.read_csv('filename.csv')` - super easy!
4. **Access columns** = `df['ColumnName']`
5. **View data** = `df.head()`, `df.tail()`, `df.info()`
6. **Statistics** = `df.describe()`, `df['Column'].mean()`
7. **Always import** = `import pandas as pd`

---

## Practice Tips

1. **Start simple** - Create small DataFrames first
2. **Use real data** - Try reading a CSV file you create
3. **Explore** - Use `.head()`, `.info()`, `.describe()` to see what you have
4. **Don't memorize** - Understand the concept, then practice
5. **Make mistakes** - That's how you learn!

---

## Next Steps

Try the exercises! They're designed to be straightforward. Remember:
- **Series** = one column
- **DataFrame** = a table
- **CSV** = a simple file format
- **pd.read_csv()** = your friend for loading data

You're learning to work with data - that's super valuable! 🎉

Good luck! 🚀

