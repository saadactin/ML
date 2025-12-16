# Day 11: DataFrame Operations — Adding/Removing Columns and the `.apply()` Method

## Introduction

Now that you know how to select and filter data, let's learn how to **modify** DataFrames by adding and removing columns, and how to use the powerful `.apply()` method to transform data.

**Why is this important?**
- **Add new information** — Create calculated columns
- **Clean up data** — Remove columns you don't need
- **Transform data** — Apply functions to columns or rows
- **Prepare for analysis** — Get your data in the right format

**What we'll learn today:**
- Adding new columns
- Removing columns
- The `.apply()` method — applying functions to data
- Common patterns and examples

**Don't worry!** We'll go step by step with simple examples. You've got this! 💪

---

## 1. Getting Started — Sample Data

Let's create some sample data to work with:

```python
import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'Age': [25, 30, 35, 28, 22],
    'Score': [85, 90, 78, 92, 88]
})

print(df)
```

**This is our starting data** — 5 people with their information.

---

## 2. Adding Columns

### What is Adding a Column?

**Adding a column** means creating a new column with data. You can:
- Add a column with the same value for all rows
- Add a column calculated from other columns
- Add a column with a list of values

### Method 1: Simple Assignment

The easiest way to add a column is to assign values to it:

```python
import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'Age': [25, 30, 35, 28, 22],
    'Score': [85, 90, 78, 92, 88]
})

# Add a column with the same value for all rows
df['Status'] = 'Active'
print(df)
```

**Output:**
```
      Name  Age  Score  Status
0    Alice   25     85  Active
1      Bob   30     90  Active
2  Charlie   35     78  Active
3    Diana   28     92  Active
4      Eve   22     88  Active
```

**What happened:** A new column 'Status' was added with 'Active' for everyone.

### Method 2: Add Column with Different Values

You can add a column with a list of values:

```python
# Add a column with different values
df['City'] = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
print(df)
```

**Output:**
```
      Name  Age  Score  Status      City
0    Alice   25     85  Active  New York
1      Bob   30     90  Active  Los Angeles
2  Charlie   35     78  Active    Chicago
3    Diana   28     92  Active    Houston
4      Eve   22     88  Active    Phoenix
```

**Important:** The list must have the same length as the number of rows!

### Method 3: Add Calculated Column

You can create a column from calculations on other columns:

```python
import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'Age': [25, 30, 35, 28, 22],
    'Score': [85, 90, 78, 92, 88]
})

# Add a column calculated from other columns
df['Score_Per_Age'] = df['Score'] / df['Age']
print(df)
```

**Output:**
```
      Name  Age  Score  Score_Per_Age
0    Alice   25     85       3.400000
1      Bob   30     90       3.000000
2  Charlie   35     78       2.228571
3    Diana   28     92       3.285714
4      Eve   22     88       4.000000
```

**What happened:** Each row's Score was divided by its Age.

### Method 4: Add Column Based on Conditions

You can create a column based on conditions (like if-else logic):

```python
import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'Age': [25, 30, 35, 28, 22],
    'Score': [85, 90, 78, 92, 88]
})

# Add a column based on condition
df['Grade'] = df['Score'].apply(lambda x: 'A' if x >= 90 else 'B' if x >= 80 else 'C')
print(df)
```

**Output:**
```
      Name  Age  Score Grade
0    Alice   25     85     B
1      Bob   30     90     A
2  Charlie   35     78     C
3    Diana   28     92     A
4      Eve   22     88     B
```

**What happened:** 
- Scores >= 90 → 'A'
- Scores >= 80 → 'B'
- Otherwise → 'C'

**Note:** We used `.apply()` here - we'll learn more about it soon!

### Simpler Way: Using NumPy's `where()`

For simple if-else, you can use NumPy:

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'Score': [85, 90, 78, 92, 88]
})

# Add column: 'Pass' if Score >= 80, else 'Fail'
df['Result'] = np.where(df['Score'] >= 80, 'Pass', 'Fail')
print(df)
```

**Output:**
```
      Name  Score Result
0    Alice     85   Pass
1      Bob     90   Pass
2  Charlie     78   Fail
3    Diana     92   Pass
4      Eve     88   Pass
```

**Syntax:** `np.where(condition, value_if_true, value_if_false)`

---

## 3. Removing Columns

### What is Removing a Column?

**Removing a column** means deleting it from the DataFrame. You might do this to:
- Remove unnecessary data
- Clean up your DataFrame
- Focus on relevant columns

### Method 1: Using `drop()`

The most common way to remove columns:

```python
import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'Age': [25, 30, 35, 28, 22],
    'Score': [85, 90, 78, 92, 88],
    'City': ['NY', 'LA', 'CHI', 'HOU', 'PHX']
})

# Remove one column
df = df.drop('City', axis=1)
print(df)
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

**Important:** 
- `axis=1` means "columns" (axis=0 would be rows)
- The original DataFrame isn't changed unless you use `inplace=True` or reassign

### Method 2: Remove Multiple Columns

You can remove multiple columns at once:

```python
# Remove multiple columns
df = df.drop(['Age', 'Score'], axis=1)
print(df)
```

**Output:**
```
      Name
0    Alice
1      Bob
2  Charlie
3    Diana
4      Eve
```

### Method 3: Using `inplace=True`

To modify the DataFrame directly (without reassigning):

```python
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Score': [85, 90, 78]
})

# Remove column directly (modifies df)
df.drop('Age', axis=1, inplace=True)
print(df)
```

**Output:**
```
      Name  Score
0    Alice     85
1      Bob     90
2  Charlie     78
```

**Note:** `inplace=True` modifies the original DataFrame.

### Method 4: Using `del` Statement

A simpler way for single columns:

```python
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Score': [85, 90, 78]
})

# Delete a column
del df['Age']
print(df)
```

**Output:**
```
      Name  Score
0    Alice     85
1      Bob     90
2  Charlie     78
```

**Note:** `del` modifies the DataFrame directly (like `inplace=True`).

---

## 4. The `.apply()` Method

### What is `.apply()`?

The `.apply()` method lets you **apply a function** to each element in a column (or row). It's like saying "do this operation to every value."

**Why use it?**
- Transform data (convert, calculate, format)
- Apply custom logic to each value
- Clean and prepare data

### Basic Syntax

```python
df['Column'].apply(function)
```

### Simple Example: Convert to Uppercase

```python
import pandas as pd

df = pd.DataFrame({
    'Name': ['alice', 'bob', 'charlie'],
    'Age': [25, 30, 35]
})

# Convert names to uppercase
df['Name'] = df['Name'].apply(str.upper)
print(df)
```

**Output:**
```
      Name  Age
0    ALICE   25
1      BOB   30
2  CHARLIE   35
```

**What happened:** Each name was converted to uppercase.

### Using Lambda Functions

**Lambda functions** are small, anonymous functions. They're perfect for simple operations:

```python
import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
})

# Add 5 to each age using lambda
df['Age_Plus_5'] = df['Age'].apply(lambda x: x + 5)
print(df)
```

**Output:**
```
      Name  Age  Age_Plus_5
0    Alice   25         30
1      Bob   30         35
2  Charlie   35         40
```

**Lambda syntax:** `lambda x: expression`
- `x` is the value from each row
- `expression` is what to do with it

### More Lambda Examples

**Example 1: Square each number**

```python
df = pd.DataFrame({'Numbers': [1, 2, 3, 4, 5]})
df['Squared'] = df['Numbers'].apply(lambda x: x ** 2)
print(df)
```

**Example 2: Check if score is passing**

```python
df = pd.DataFrame({'Score': [85, 90, 78, 92, 88]})
df['Passing'] = df['Score'].apply(lambda x: 'Pass' if x >= 80 else 'Fail')
print(df)
```

**Example 3: Get length of strings**

```python
df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie']})
df['Name_Length'] = df['Name'].apply(lambda x: len(x))
print(df)
```

### Using Regular Functions

You can also use regular functions (not just lambdas):

```python
import pandas as pd

# Define a function
def add_bonus(score):
    if score >= 90:
        return score + 10
    else:
        return score + 5

df = pd.DataFrame({'Score': [85, 90, 78, 92, 88]})

# Apply the function
df['Score_With_Bonus'] = df['Score'].apply(add_bonus)
print(df)
```

**Output:**
```
   Score  Score_With_Bonus
0     85                90
1     90               100
2     78                83
3     92               102
4     88                93
```

**When to use regular functions vs lambdas:**
- **Lambda:** Simple, one-line operations
- **Regular function:** Complex logic, multiple lines, reusable

### Applying to Multiple Columns

You can apply a function to the entire DataFrame (all columns):

```python
import pandas as pd

df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})

# Apply function to each element
df = df.apply(lambda x: x * 2)
print(df)
```

**Output:**
```
   A   B   C
0  2   8  14
1  4  10  16
2  6  12  18
```

**Note:** This applies to each element. Use `axis=0` for rows or `axis=1` for columns if needed.

---

## 5. Common Patterns and Examples

### Pattern 1: Create Calculated Column

```python
import pandas as pd

df = pd.DataFrame({
    'Price': [10, 20, 30],
    'Quantity': [2, 3, 4]
})

# Calculate total
df['Total'] = df['Price'] * df['Quantity']
print(df)
```

### Pattern 2: Categorize Data

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({'Age': [22, 25, 30, 35, 40]})

# Categorize ages
df['Age_Group'] = np.where(df['Age'] < 25, 'Young',
                  np.where(df['Age'] < 35, 'Adult', 'Senior'))
print(df)
```

### Pattern 3: Clean Text Data

```python
import pandas as pd

df = pd.DataFrame({'Name': ['  alice  ', '  BOB  ', '  Charlie  ']})

# Clean: strip whitespace and capitalize
df['Name'] = df['Name'].apply(lambda x: x.strip().capitalize())
print(df)
```

### Pattern 4: Add Timestamp Column

```python
import pandas as pd
from datetime import datetime

df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie']})

# Add current timestamp
df['Created_At'] = datetime.now()
print(df)
```

### Pattern 5: Remove Unnecessary Columns

```python
# Remove columns you don't need
df = df.drop(['Old_Column1', 'Old_Column2'], axis=1)
# Or keep only what you need
df = df[['Name', 'Score']]  # Keep only these columns
```

---

## 6. Common Mistakes (And How to Avoid Them)

### Mistake 1: Forgetting `axis=1` in `drop()`

```python
# ❌ WRONG
df.drop('Column')  # Drops row, not column!

# ✅ CORRECT
df.drop('Column', axis=1)  # Drops column
```

**Why:** Without `axis=1`, it tries to drop a row (by index), not a column.

### Mistake 2: Not Reassigning After `drop()`

```python
# ❌ WRONG - Original df unchanged
df.drop('Column', axis=1)
print(df)  # Column still there!

# ✅ CORRECT - Reassign
df = df.drop('Column', axis=1)
# Or use inplace=True
df.drop('Column', axis=1, inplace=True)
```

### Mistake 3: Wrong List Length When Adding Column

```python
# ❌ WRONG - List too short
df['New_Col'] = [1, 2]  # Error if df has more than 2 rows!

# ✅ CORRECT - List matches number of rows
df['New_Col'] = [1, 2, 3, 4, 5]  # Matches 5 rows
```

### Mistake 4: Using Wrong Function in `apply()`

```python
# ❌ WRONG - str.upper() needs to be called
df['Name'].apply(str.upper())  # Error!

# ✅ CORRECT - Pass function, not call it
df['Name'].apply(str.upper)  # No parentheses
# Or use lambda
df['Name'].apply(lambda x: x.upper())
```

### Mistake 5: Confusing `apply()` with Direct Operations

```python
# For simple operations, you don't need apply()
# ❌ UNNECESSARY
df['Double'] = df['Number'].apply(lambda x: x * 2)

# ✅ SIMPLER
df['Double'] = df['Number'] * 2
```

**Use `apply()` when:** You need custom logic, functions, or complex operations.

---

## 7. Quick Reference

### Adding Columns

```python
# Same value for all
df['New_Col'] = 'value'

# List of values
df['New_Col'] = [val1, val2, val3, ...]

# Calculated from other columns
df['New_Col'] = df['Col1'] * df['Col2']

# Based on condition
df['New_Col'] = np.where(df['Col'] > 10, 'High', 'Low')
```

### Removing Columns

```python
# One column
df = df.drop('Column', axis=1)
# Or
del df['Column']

# Multiple columns
df = df.drop(['Col1', 'Col2'], axis=1)

# With inplace
df.drop('Column', axis=1, inplace=True)
```

### Using `.apply()`

```python
# With lambda
df['New'] = df['Col'].apply(lambda x: x * 2)

# With function
df['New'] = df['Col'].apply(function_name)

# With built-in
df['New'] = df['Col'].apply(str.upper)
```

---

## Key Takeaways (Simple Summary)

1. **Add column:** `df['New_Col'] = values` (list, calculation, or single value)
2. **Remove column:** `df.drop('Col', axis=1)` or `del df['Col']`
3. **`.apply()`:** Apply function to each value: `df['Col'].apply(function)`
4. **Lambda functions:** `lambda x: expression` for simple operations
5. **Use `axis=1`** for columns in `drop()`
6. **Reassign or use `inplace=True`** when dropping columns
7. **List length must match** number of rows when adding columns

---

## Practice Tips

1. **Start simple** — Add a column with a constant value first
2. **Test calculations** — Print intermediate results to check
3. **Use `apply()` for complex logic** — Simple operations can be done directly
4. **Check your data** — Use `head()` after adding/removing columns
5. **Practice with real data** — Try modifying your own datasets

---

## Next Steps

Try the exercises! They're designed to help you practice adding/removing columns and using `.apply()`. Remember:
- **Adding columns** is as simple as assignment
- **Removing columns** needs `axis=1` in `drop()`
- **`.apply()`** is powerful for transformations
- **Lambda functions** are great for simple operations

You're learning to manipulate data like a pro! 🎉

Good luck! 🚀

