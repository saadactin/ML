# Day 9: Inspecting Data in Pandas — Understanding Your Data

## Introduction

When you load data (like from a CSV file), the first thing you should do is **inspect it** — look at it, understand what you have, and check if it looks correct.

**Why inspect data?**
- **See what you have** — What columns? How many rows?
- **Check for problems** — Missing values? Wrong data types?
- **Understand the data** — What are the ranges? What are typical values?
- **Make decisions** — How to clean or process the data

**What we'll learn today:**
- `head()` — See the first few rows
- `tail()` — See the last few rows
- `info()` — Get information about the data
- `describe()` — Get statistics about numeric columns
- `shape` — Get the size of your data

**Don't worry!** These are simple but powerful tools. We'll go step by step. You've got this! 💪

---

## 1. Getting Started — Loading Data

Before we can inspect data, we need some data to work with!

```python
import pandas as pd

# Create a sample DataFrame (or read from CSV)
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank', 'Grace', 'Henry'],
    'Age': [25, 30, 35, 28, 22, 40, 33, 27],
    'Score': [85, 90, 78, 92, 88, 75, 95, 82],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego']
})

print("DataFrame created!")
```

**This is our sample data** — 8 people with their names, ages, scores, and cities.

---

## 2. `head()` — See the First Rows

### What is `head()`?

`head()` shows you the **first few rows** of your data. It's like looking at the top of a spreadsheet.

**Why use it?**
- Quick preview of your data
- See column names
- Check if data loaded correctly
- See what the data looks like

### Basic Usage

```python
import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank', 'Grace', 'Henry'],
    'Age': [25, 30, 35, 28, 22, 40, 33, 27],
    'Score': [85, 90, 78, 92, 88, 75, 95, 82]
})

# See first 5 rows (default)
print(df.head())
```

**Output:**
```
      Name  Age  Score
0    Alice   25     85
1      Bob   30     90
2  Charlie   35     78
3    Diana   28     92
4      Eve   22     88
```

**What you see:**
- Column names at the top
- First 5 rows of data
- Row numbers on the left (0, 1, 2, 3, 4)

### Specifying Number of Rows

You can see more or fewer rows:

```python
# See first 3 rows
print(df.head(3))

# See first 10 rows
print(df.head(10))
```

**When to use:**
- **After loading data** — Check if it loaded correctly
- **Before processing** — See what you're working with
- **Quick preview** — Don't want to print everything

---

## 3. `tail()` — See the Last Rows

### What is `tail()`?

`tail()` shows you the **last few rows** of your data. It's like looking at the bottom of a spreadsheet.

**Why use it?**
- Check the end of your data
- See if data is complete
- Verify the last few records

### Basic Usage

```python
import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank', 'Grace', 'Henry'],
    'Age': [25, 30, 35, 28, 22, 40, 33, 27],
    'Score': [85, 90, 78, 92, 88, 75, 95, 82]
})

# See last 5 rows (default)
print(df.tail())
```

**Output:**
```
     Name  Age  Score
3   Diana   28     92
4     Eve   22     88
5   Frank   40     75
6   Grace   33     95
7   Henry   27     82
```

**What you see:**
- Last 5 rows of data
- Same format as `head()`

### Specifying Number of Rows

```python
# See last 3 rows
print(df.tail(3))

# See last 10 rows
print(df.tail(10))
```

**When to use:**
- **Check data completeness** — Are the last rows there?
- **Verify end of file** — Make sure nothing was cut off
- **Compare with head()** — See if data looks consistent

---

## 4. `info()` — Get Information About Your Data

### What is `info()`?

`info()` gives you **detailed information** about your DataFrame. It's like a summary report.

**What it shows:**
- Number of rows and columns
- Column names
- Data types (int, float, object/string)
- Number of non-null values (missing data check)
- Memory usage

### Basic Usage

```python
import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'Age': [25, 30, 35, 28, 22],
    'Score': [85, 90, 78, 92, 88]
})

# Get information
print(df.info())
```

**Output:**
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   Name    5 non-null      object
 1   Age     5 non-null      int64
 2   Score   5 non-null      int64
dtypes: int64(2), object(1)
memory usage: 248.0+ bytes
```

**What it tells you:**
- **RangeIndex: 5 entries** — You have 5 rows
- **3 columns** — Name, Age, Score
- **Non-Null Count** — All 5 values exist (no missing data)
- **Dtype** — Data types:
  - `object` = strings/text (Name)
  - `int64` = integers (Age, Score)
- **Memory usage** — How much memory it uses

### Understanding the Output

**If you see missing data:**
```
Name    4 non-null      object
Age     5 non-null      int64
Score   3 non-null      int64
```

This means:
- Name: 4 out of 5 values exist (1 missing)
- Age: All 5 values exist
- Score: 3 out of 5 values exist (2 missing)

**When to use:**
- **After loading data** — Check for problems
- **Before analysis** — Understand your data structure
- **Debugging** — Find missing values or wrong data types

---

## 5. `describe()` — Get Statistics

### What is `describe()`?

`describe()` gives you **statistics** about your numeric columns. It's like a quick summary of numbers.

**What it shows:**
- **count** — How many values (non-null)
- **mean** — Average
- **std** — Standard deviation (spread)
- **min** — Minimum value
- **25%** — 25th percentile (1/4 of values below this)
- **50%** — Median (middle value)
- **75%** — 75th percentile (3/4 of values below this)
- **max** — Maximum value

### Basic Usage

```python
import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'Age': [25, 30, 35, 28, 22],
    'Score': [85, 90, 78, 92, 88]
})

# Get statistics
print(df.describe())
```

**Output:**
```
             Age      Score
count   5.000000   5.000000
mean   28.000000  86.600000
std     4.949747   5.366563
min    22.000000  78.000000
25%    25.000000  85.000000
50%    28.000000  88.000000
75%    30.000000  90.000000
max    35.000000  92.000000
```

**What it tells you:**

**For Age:**
- count: 5 values
- mean: 28 years old (average)
- std: ~4.95 (ages are close together)
- min: 22 (youngest)
- max: 35 (oldest)
- 50% (median): 28 (middle age)

**For Score:**
- count: 5 values
- mean: 86.6 (average score)
- std: ~5.37 (scores are close together)
- min: 78 (lowest score)
- max: 92 (highest score)
- 50% (median): 88 (middle score)

**Note:** `describe()` only shows statistics for **numeric columns** (numbers). Text columns (like 'Name') are not included.

### Understanding Percentiles

**Simple explanation:**
- **25%** — 25% of values are below this number
- **50% (median)** — Half the values are below, half above
- **75%** — 75% of values are below this number

**Example:**
If Age 50% = 28, that means:
- Half the people are younger than 28
- Half the people are older than 28

**When to use:**
- **Quick overview** — See ranges and averages
- **Find outliers** — Very high or low values
- **Understand distribution** — Are values spread out or close together?

---

## 6. `shape` — Get the Size

### What is `shape`?

`shape` tells you **how many rows and columns** your DataFrame has. It's super simple but very useful!

**Returns:** A tuple `(rows, columns)`

### Basic Usage

```python
import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'Age': [25, 30, 35, 28, 22],
    'Score': [85, 90, 78, 92, 88]
})

# Get shape
print(df.shape)
```

**Output:**
```
(5, 3)
```

**What it means:**
- **5 rows** — 5 people/records
- **3 columns** — Name, Age, Score

**Remember:** `(rows, columns)` — always in that order!

### Using Shape Values

You can use the values separately:

```python
rows, columns = df.shape
print(f"Number of rows: {rows}")
print(f"Number of columns: {columns}")

# Or access individually
print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")
```

**When to use:**
- **Quick check** — How much data do I have?
- **Before processing** — Make sure data loaded correctly
- **Compare datasets** — Are they the same size?

---

## 7. Complete Inspection Workflow

### The Standard Workflow

When you load data, follow this pattern:

```python
import pandas as pd

# Step 1: Load data
df = pd.read_csv('data.csv')

# Step 2: Quick look at the top
print("First few rows:")
print(df.head())

# Step 3: Quick look at the bottom
print("\nLast few rows:")
print(df.tail())

# Step 4: Get detailed information
print("\nData Information:")
print(df.info())

# Step 5: Get statistics
print("\nStatistics:")
print(df.describe())

# Step 6: Get size
print(f"\nData size: {df.shape[0]} rows, {df.shape[1]} columns")
```

**This gives you a complete picture!**

### Real-World Example

```python
import pandas as pd

# Load student data
df = pd.read_csv('students.csv')

# Inspect the data
print("=" * 50)
print("DATA INSPECTION REPORT")
print("=" * 50)

print("\n1. First 5 rows:")
print(df.head())

print("\n2. Last 5 rows:")
print(df.tail())

print("\n3. Data Information:")
df.info()

print("\n4. Statistics:")
print(df.describe())

print(f"\n5. Size: {df.shape[0]} rows × {df.shape[1]} columns")
```

---

## 8. Common Patterns

### Pattern 1: Quick Data Check

```python
# Quick check after loading
df = pd.read_csv('data.csv')
print(df.head())  # Does it look right?
print(df.shape)   # How much data?
```

### Pattern 2: Finding Problems

```python
# Check for issues
df.info()  # Missing values? Wrong types?
df.describe()  # Any weird numbers?
```

### Pattern 3: Comparing Before and After

```python
# Before cleaning
print("Before:", df.shape)
print(df.head())

# ... do some cleaning ...

# After cleaning
print("After:", df.shape)
print(df.head())
```

---

## 9. Common Mistakes (And How to Avoid Them)

### Mistake 1: Forgetting Parentheses

```python
# ❌ WRONG
df.head  # This doesn't call the function!

# ✅ CORRECT
df.head()  # Need parentheses!
```

### Mistake 2: Not Understanding Shape Order

```python
# Shape is (rows, columns) - remember the order!
print(df.shape)  # (100, 5) means 100 rows, 5 columns
# NOT (5, 100)!
```

### Mistake 3: Expecting Text in describe()

```python
# describe() only shows numeric columns
df.describe()  # Won't show 'Name' column (it's text)
# Only shows Age, Score, etc. (numbers)
```

### Mistake 4: Not Checking After Loading

```python
# ❌ WRONG - Load and immediately process
df = pd.read_csv('data.csv')
df['Score'].mean()  # What if data is wrong?

# ✅ CORRECT - Inspect first
df = pd.read_csv('data.csv')
df.head()  # Check it first!
df.info()  # Understand it!
# Then process
```

---

## 10. Quick Reference

### The Five Essential Methods

```python
import pandas as pd
df = pd.read_csv('data.csv')

# 1. See first rows
df.head()        # First 5 rows
df.head(10)      # First 10 rows

# 2. See last rows
df.tail()        # Last 5 rows
df.tail(10)      # Last 10 rows

# 3. Get information
df.info()        # Detailed info about data

# 4. Get statistics
df.describe()    # Statistics for numeric columns

# 5. Get size
df.shape         # (rows, columns)
```

---

## Key Takeaways (Simple Summary)

1. **`head()`** — See first few rows (default: 5)
2. **`tail()`** — See last few rows (default: 5)
3. **`info()`** — Get detailed information (types, missing values, etc.)
4. **`describe()`** — Get statistics for numeric columns
5. **`shape`** — Get size: `(rows, columns)`
6. **Always inspect** — Check your data before processing!
7. **Workflow** — Load → head() → tail() → info() → describe() → shape

---

## Practice Tips

1. **Use them together** — Don't just use one, use all of them!
2. **After loading** — Always inspect data you just loaded
3. **Before processing** — Understand what you're working with
4. **When debugging** — If something's wrong, inspect the data
5. **Make it a habit** — Always inspect first!

---

## Next Steps

Try the exercises! They're designed to help you practice inspecting data. Remember:
- **Always inspect** your data first
- **Use all methods** to get a complete picture
- **Understand what each method tells you**

You're learning to be a data detective — that's awesome! 🎉

Good luck! 🚀

