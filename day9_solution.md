# Day 9: Inspecting Data Exercises — Solutions

**Note:** Only check these solutions after you've attempted the problems yourself!

Remember: The goal is to understand how to inspect and understand your data. Take your time! 💪

---

## Exercise 1: Creating and Inspecting Data

### Solution 1.1

```python
import pandas as pd

# Create DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'Age': [25, 30, 35, 28, 22],
    'Score': [85, 90, 78, 92, 88]
}
df = pd.DataFrame(data)

# Print first 3 rows
print("First 3 rows:")
print(df.head(3))

# Print last 2 rows
print("\nLast 2 rows:")
print(df.tail(2))

# Print shape
print("\nShape:")
print(df.shape)
```

**Output:**
```
First 3 rows:
      Name  Age  Score
0    Alice   25     85
1      Bob   30     90
2  Charlie   35     78

Last 2 rows:
    Name  Age  Score
3  Diana   28     92
4    Eve   22     88

Shape:
(5, 3)
```

**Explanation:**
- `head(3)` shows the first 3 rows
- `tail(2)` shows the last 2 rows
- `shape` returns `(5, 3)` meaning 5 rows and 3 columns

---

### Solution 1.2

```python
import pandas as pd

# Create DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'Age': [25, 30, 35, 28, 22],
    'Score': [85, 90, 78, 92, 88]
}
df = pd.DataFrame(data)

# Print info
print("Data Information:")
print(df.info())

# Print describe
print("\nStatistics:")
print(df.describe())
```

**Output:**
```
Data Information:
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
None

Statistics:
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

**What you notice:**
- `info()` shows all columns (Name, Age, Score)
- `describe()` only shows numeric columns (Age and Score)
- The 'Name' column is NOT in `describe()` because it's text (object type), not a number

**Key insight:** `describe()` only works with numeric data!

---

### Solution 1.3

```python
import pandas as pd

# Create DataFrame with 10 rows
df = pd.DataFrame({
    'Product': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
    'Price': [10, 20, 15, 25, 30, 18, 22, 28, 12, 35],
    'Quantity': [5, 3, 7, 2, 4, 6, 8, 1, 9, 3]
})

# Print first 5 rows (default)
print("First 5 rows:")
print(df.head())

# Print last 5 rows (default)
print("\nLast 5 rows:")
print(df.tail())

# Print shape
print(f"\nShape: {df.shape}")
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")
```

**Output:**
```
First 5 rows:
  Product  Price  Quantity
0       A     10         5
1       B     20         3
2       C     15         7
3       D     25         2
4       E     30         4

Last 5 rows:
  Product  Price  Quantity
5       F     18         6
6       G     22         8
7       H     28         1
8       I     12         9
9       J     35         3

Shape: (10, 3)
Rows: 10, Columns: 3
```

**Explanation:**
- `head()` without arguments shows first 5 rows (default)
- `tail()` without arguments shows last 5 rows (default)
- `shape` is `(10, 3)` - 10 rows, 3 columns
- You can access individual values: `shape[0]` for rows, `shape[1]` for columns

---

## Exercise 2: Understanding the Output

### Solution 2.1

```python
import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Score': [85, 90, 78]
})

# Get shape
rows, columns = df.shape
print(f"Number of rows: {rows}")
print(f"Number of columns: {columns}")

# Get average age from describe
print("\nStatistics:")
stats = df.describe()
print(stats)
print(f"\nAverage age: {stats.loc['mean', 'Age']}")
```

**Output:**
```
Number of rows: 3
Number of columns: 3

Statistics:
             Age      Score
count   3.000000   3.000000
mean   30.000000  84.333333
std     5.000000   6.110101
min    25.000000  78.000000
25%    27.500000  81.500000
50%    30.000000  85.000000
75%    32.500000  87.500000
max    35.000000  90.000000

Average age: 30.0
```

**Explanation:**
- Shape is `(3, 3)` - 3 rows, 3 columns
- Average age from `describe()` is 30.0
- You can see it in the 'mean' row under 'Age' column

---

### Solution 2.2

```python
import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Score': [85, 90, 78]
})

# Get info to see data types
print("Data Information:")
df.info()

# Get describe to see minimum score
print("\nStatistics:")
stats = df.describe()
print(stats)
print(f"\nMinimum score: {stats.loc['min', 'Score']}")
```

**Output:**
```
Data Information:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 3 entries, 0 to 4
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   Name    3 non-null      object
 1   Age     3 non-null      int64
 2   Score   3 non-null      int64
dtypes: int64(2), object(1)
None

Statistics:
             Age      Score
count   3.000000   3.000000
mean   30.000000  84.333333
std     5.000000   6.110101
min    25.000000  78.000000
25%    27.500000  81.500000
50%    30.000000  85.000000
75%    32.500000  87.500000
max    35.000000  90.000000

Minimum score: 78.0
```

**Answers:**
- **Name column data type:** `object` (this means text/string)
- **Age column data type:** `int64` (integer)
- **Minimum score:** `78.0`

**Explanation:**
- From `info()`, you can see the Dtype column showing data types
- From `describe()`, you can see the 'min' row showing minimum values

---

### Solution 2.3

```python
import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    'City': ['New York', 'Los Angeles', 'Chicago'],
    'Population': [8000000, 4000000, 2700000],
    'Area': [783.8, 1302.0, 606.1]
})

# Print info to see non-null counts
print("Data Information:")
df.info()

# Print describe to see statistics
print("\nStatistics:")
stats = df.describe()
print(stats)
print(f"\nMean population: {stats.loc['mean', 'Population']:.0f}")

# Explain which columns appear in describe
print("\nColumns in describe(): Population and Area")
print("Why: These are numeric columns (int64 and float64)")
print("City column is NOT in describe() because it's text (object type)")
```

**Output:**
```
Data Information:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 3 entries, 0 to 4
Data columns (total 3 columns):
 #   Column      Non-Null Count  Dtype
---  ------      --------------  -----
 0   City        3 non-null      object
 1   Population  3 non-null      int64
 2   Area        3 non-null      float64
dtypes: object(1), int64(1), float64(1)
None

Statistics:
        Population         Area
count     3.000000     3.000000
mean   4900000.000000   897.300000
std    2658300.000000   357.700000
min    2700000.000000   606.100000
25%    3350000.000000   694.950000
50%    4000000.000000   783.800000
75%    6000000.000000  1042.900000
max    8000000.000000  1302.000000

Mean population: 4900000

Columns in describe(): Population and Area
Why: These are numeric columns (int64 and float64)
City column is NOT in describe() because it's text (object type)
```

**Answers:**
- **Non-null values:** All 3 columns have 3 non-null values (no missing data)
- **Mean population:** 4,900,000
- **Columns in describe():** Population and Area (numeric columns only)
- **Why:** `describe()` only shows statistics for numeric data types (int64, float64), not text (object)

---

## Exercise 3: Working with CSV Files

### Solution 3.1

**Step 1: Create the CSV file**

Create a file named `students.csv` in the same folder as your Python script with this content:
```csv
Name,Age,Score,City
Alice,25,85,New York
Bob,30,90,Los Angeles
Charlie,35,78,Chicago
Diana,28,92,Houston
Eve,22,88,Phoenix
```

**Step 2: Read and inspect**

```python
import pandas as pd

# Read the CSV file
df = pd.read_csv('students.csv')

# Print first 3 rows
print("First 3 rows:")
print(df.head(3))

# Print shape
print(f"\nShape: {df.shape}")
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

# Print info
print("\nData Information:")
df.info()
```

**Output:**
```
First 3 rows:
      Name  Age  Score        City
0    Alice   25     85    New York
1      Bob   30     90  Los Angeles
2  Charlie   35     78      Chicago

Shape: (5, 4)
Rows: 5, Columns: 4

Data Information:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 4 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   Name    5 non-null      object
 1   Age     5 non-null      int64
 2   Score   5 non-null      int64
 3   City    5 non-null      object
dtypes: object(2), int64(2)
memory usage: 288.0+ bytes
None
```

**Explanation:**
- Successfully loaded 5 rows and 4 columns
- All columns have 5 non-null values (no missing data)
- Two text columns (Name, City) and two numeric columns (Age, Score)

---

### Solution 3.2

```python
import pandas as pd

# Read the CSV file
df = pd.read_csv('students.csv')

# Print describe and get average age
print("Statistics:")
stats = df.describe()
print(stats)
print(f"\nAverage age: {stats.loc['mean', 'Age']:.1f}")

# Print last rows
print("\nLast rows:")
print(df.tail())

# Print size using shape
print(f"\nSize: {df.shape[0]} rows × {df.shape[1]} columns")
```

**Output:**
```
Statistics:
             Age      Score
count   5.000000   5.000000
mean   28.000000  86.600000
std     5.099020   5.366563
min    22.000000  78.000000
25%    25.000000  85.000000
50%    28.000000  88.000000
75%    30.000000  90.000000
max    35.000000  92.000000

Average age: 28.0

Last rows:
      Name  Age  Score      City
3    Diana   28     92    Houston
4      Eve   22     88    Phoenix

Size: 5 rows × 4 columns
```

**Answers:**
- **Average age:** 28.0 years
- **Last rows:** Shows Diana and Eve (last 2 rows by default)
- **Size:** 5 rows × 4 columns

**Note:** `describe()` only shows Age and Score (numeric columns), not Name and City (text columns).

---

## Additional Practice Ideas

Once you're comfortable with these, try:

1. **Create your own CSV file:**
   - Make a CSV with your own data
   - Load it and inspect it using all methods

2. **Compare different datasets:**
   ```python
   df1 = pd.read_csv('data1.csv')
   df2 = pd.read_csv('data2.csv')
   print("Dataset 1:", df1.shape)
   print("Dataset 2:", df2.shape)
   ```

3. **Check for problems:**
   ```python
   df = pd.read_csv('data.csv')
   df.info()  # Look for missing values (non-null count < total rows)
   df.describe()  # Look for weird numbers (very high/low)
   ```

---

## Common Questions

**Q: Why doesn't `describe()` show my text column?**
A: `describe()` only shows statistics for numeric columns (numbers). Text columns (object type) don't have statistics like mean or std.

**Q: What's the difference between `head()` and `tail()`?**
A: 
- `head()` shows the **first** rows (top of the data)
- `tail()` shows the **last** rows (bottom of the data)

**Q: What does `shape` return?**
A: A tuple `(rows, columns)`. Always in that order!

**Q: When should I use each method?**
A:
- `head()` / `tail()` - Quick preview
- `info()` - Check for problems (missing values, data types)
- `describe()` - Understand numeric data (ranges, averages)
- `shape` - Quick size check

**Q: Can I use these methods on Series too?**
A: Yes! Series also have `head()`, `tail()`, `info()`, `describe()`, but `shape` returns just a number (not a tuple).

---

## Key Takeaways

✅ **`head(n)`** - First n rows (default: 5)

✅ **`tail(n)`** - Last n rows (default: 5)

✅ **`info()`** - Detailed information (types, missing values, memory)

✅ **`describe()`** - Statistics for numeric columns only

✅ **`shape`** - Returns `(rows, columns)` tuple

✅ **Always inspect first** - Before processing data, always inspect it!

✅ **Workflow** - Load → head() → tail() → info() → describe() → shape

---

## Final Reminder

**The most important habit:** Always inspect your data after loading it! This helps you:
- Understand what you're working with
- Find problems early
- Make better decisions about processing

**Great job completing the exercises! 🎉**

You've learned how to inspect data - this is a fundamental skill for data analysis. Keep practicing and make it a habit to always inspect your data first!

