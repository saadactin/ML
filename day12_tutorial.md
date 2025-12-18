# Day 12: Grouping and Aggregation — `groupby()` with `.agg()`, `.count()`, `.mean()`

## Introduction

Sometimes you want to **group** your data and calculate statistics for each group. For example:
- "What's the average score for each city?"
- "How many people are in each age group?"
- "What's the total sales for each product category?"

This is where **grouping and aggregation** comes in!

**Why is this important?**
- **Summarize data** — Get insights by groups
- **Answer questions** — "Which group performs best?"
- **Compare groups** — See differences between categories
- **Prepare reports** — Create summaries for analysis

**What we'll learn today:**
- `groupby()` — Group data by categories
- `.count()` — Count items in each group
- `.mean()` — Calculate average for each group
- `.agg()` — Apply multiple functions at once
- Common patterns and examples

**Don't worry!** We'll go step by step with simple examples. You've got this! 💪

---

## 1. Getting Started — Sample Data

Let's create some sample data to work with:

```python
import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank', 'Grace', 'Henry'],
    'City': ['New York', 'Los Angeles', 'New York', 'Chicago', 'Los Angeles', 'Chicago', 'New York', 'Chicago'],
    'Age': [25, 30, 35, 28, 22, 40, 33, 27],
    'Score': [85, 90, 78, 92, 88, 75, 95, 82],
    'Department': ['Sales', 'Sales', 'IT', 'IT', 'Sales', 'IT', 'Sales', 'IT']
})

print(df)
```

**This is our data** — 8 people with their city, age, score, and department.

---

## 2. Understanding `groupby()` — The Basics

### What is `groupby()`?

`groupby()` **splits** your data into groups based on a column, then you can calculate statistics for each group.

**Simple analogy:** Like organizing students by their class, then finding the average grade for each class.

### Basic Syntax

```python
df.groupby('ColumnName').function()
```

**What it does:**
1. Groups rows by the values in 'ColumnName'
2. Applies a function (like mean, count) to each group
3. Returns results for each group

### Simple Example: Count by Group

**Question:** How many people are in each city?

```python
import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank'],
    'City': ['New York', 'Los Angeles', 'New York', 'Chicago', 'Los Angeles', 'Chicago']
})

# Count people in each city
result = df.groupby('City').count()
print(result)
```

**Output:**
```
            Name
City           
Chicago        2
Los Angeles    2
New York       2
```

**What happened:**
- Data was grouped by 'City'
- `.count()` counted how many people in each city
- Chicago: 2 people, Los Angeles: 2 people, New York: 2 people

**Note:** The result shows all columns (Name), but they all have the same count. We'll learn to select specific columns soon!

### Getting Count of Rows

To get just the number of rows in each group:

```python
# Count rows in each group
result = df.groupby('City').size()
print(result)
```

**Output:**
```
City
Chicago        2
Los Angeles    2
New York       2
dtype: int64
```

**Or use:**
```python
result = df.groupby('City')['Name'].count()
print(result)
```

**Output:**
```
City
Chicago        2
Los Angeles    2
New York       2
Name: Name, dtype: int64
```

---

## 3. Calculating Averages with `.mean()`

### What is `.mean()`?

`.mean()` calculates the **average** (mean) of numeric columns for each group.

### Simple Example: Average Score by City

**Question:** What's the average score for each city?

```python
import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank'],
    'City': ['New York', 'Los Angeles', 'New York', 'Chicago', 'Los Angeles', 'Chicago'],
    'Score': [85, 90, 78, 92, 88, 75]
})

# Average score for each city
result = df.groupby('City')['Score'].mean()
print(result)
```

**Output:**
```
City
Chicago        83.5
Los Angeles    89.0
New York       81.5
Name: Score, dtype: float64
```

**What happened:**
- Grouped by 'City'
- Selected 'Score' column: `['Score']`
- Calculated mean for each group:
  - Chicago: (92 + 75) / 2 = 83.5
  - Los Angeles: (90 + 88) / 2 = 89.0
  - New York: (85 + 78) / 2 = 81.5

### Multiple Columns with `.mean()`

You can calculate mean for multiple columns:

```python
# Average of multiple columns for each group
result = df.groupby('City')[['Score', 'Age']].mean()
print(result)
```

**Output:**
```
            Score   Age
City                   
Chicago      83.5  34.0
Los Angeles  89.0  26.0
New York     81.5  30.0
```

**What happened:**
- Grouped by 'City'
- Calculated mean for both 'Score' and 'Age' columns
- Result is a DataFrame with both averages

---

## 4. Using `.count()` for Counting

### What is `.count()`?

`.count()` counts the number of **non-null** (not missing) values in each group.

### Simple Example: Count People by Department

```python
import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'Department': ['Sales', 'Sales', 'IT', 'IT', 'Sales']
})

# Count people in each department
result = df.groupby('Department')['Name'].count()
print(result)
```

**Output:**
```
Department
IT      2
Sales   3
Name: Name, dtype: int64
```

**What happened:**
- Grouped by 'Department'
- Counted names in each group
- IT: 2 people, Sales: 3 people

### Count All Columns

If you don't specify a column, it counts all columns:

```python
result = df.groupby('Department').count()
print(result)
```

**Output:**
```
            Name
Department      
IT             2
Sales          3
```

---

## 5. The Powerful `.agg()` Method

### What is `.agg()`?

`.agg()` (short for "aggregate") lets you apply **multiple functions** at once to different columns. It's super powerful!

### Basic Syntax

```python
df.groupby('Column').agg({
    'Column1': 'function1',
    'Column2': 'function2'
})
```

### Simple Example: Multiple Statistics

**Question:** For each city, what's the average score and total count?

```python
import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank'],
    'City': ['New York', 'Los Angeles', 'New York', 'Chicago', 'Los Angeles', 'Chicago'],
    'Score': [85, 90, 78, 92, 88, 75],
    'Age': [25, 30, 35, 28, 22, 40]
})

# Multiple statistics for each city
result = df.groupby('City').agg({
    'Score': 'mean',  # Average score
    'Name': 'count'   # Count of people
})
print(result)
```

**Output:**
```
            Score  Name
City                   
Chicago      83.5     2
Los Angeles  89.0     2
New York     81.5     2
```

**What happened:**
- Grouped by 'City'
- For 'Score' column: calculated mean
- For 'Name' column: counted (number of people)
- Result shows both statistics

### Multiple Functions on Same Column

You can apply multiple functions to the same column:

```python
# Multiple statistics for Score column
result = df.groupby('City')['Score'].agg(['mean', 'min', 'max', 'count'])
print(result)
```

**Output:**
```
            mean  min  max  count
City                             
Chicago     83.5   75   92      2
Los Angeles 89.0   88   90      2
New York    81.5   78   85      2
```

**What happened:**
- Applied 4 functions to 'Score': mean, min, max, count
- Result shows all 4 statistics for each city

### Different Functions for Different Columns

You can apply different functions to different columns:

```python
result = df.groupby('City').agg({
    'Score': ['mean', 'max'],  # Multiple functions for Score
    'Age': 'mean',             # One function for Age
    'Name': 'count'            # One function for Name
})
print(result)
```

**Output:**
```
            Score      Age  Name
            mean  max  mean count
City                            
Chicago     83.5   92  34.0     2
Los Angeles 89.0   90  26.0     2
New York    81.5   85  30.0     2
```

**What happened:**
- Score: calculated mean and max
- Age: calculated mean
- Name: counted

---

## 6. Common Aggregation Functions

Here are the most common functions you can use:

```python
# Count
df.groupby('City')['Score'].count()    # Number of non-null values
df.groupby('City').size()              # Number of rows

# Statistics
df.groupby('City')['Score'].mean()     # Average
df.groupby('City')['Score'].sum()      # Total
df.groupby('City')['Score'].min()      # Minimum
df.groupby('City')['Score'].max()      # Maximum
df.groupby('City')['Score'].std()      # Standard deviation

# With agg()
df.groupby('City').agg({
    'Score': ['mean', 'min', 'max', 'count']
})
```

---

## 7. Grouping by Multiple Columns

### Grouping by Two Columns

You can group by multiple columns:

```python
import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank'],
    'City': ['New York', 'New York', 'Chicago', 'Chicago', 'New York', 'Chicago'],
    'Department': ['Sales', 'IT', 'Sales', 'IT', 'Sales', 'IT'],
    'Score': [85, 90, 78, 92, 88, 75]
})

# Group by City AND Department
result = df.groupby(['City', 'Department'])['Score'].mean()
print(result)
```

**Output:**
```
City      Department
Chicago   IT           83.5
          Sales        78.0
New York  IT           90.0
          Sales        86.5
Name: Score, dtype: float64
```

**What happened:**
- Grouped by both 'City' and 'Department'
- Calculated mean score for each combination
- Chicago-IT: 83.5, Chicago-Sales: 78.0, etc.

---

## 8. Common Patterns and Examples

### Pattern 1: Summary Statistics by Group

```python
# Get comprehensive statistics for each group
result = df.groupby('City')['Score'].agg(['mean', 'min', 'max', 'count'])
print(result)
```

### Pattern 2: Multiple Aggregations

```python
# Different statistics for different columns
result = df.groupby('Department').agg({
    'Score': 'mean',
    'Age': ['mean', 'min', 'max'],
    'Name': 'count'
})
print(result)
```

### Pattern 3: Count and Percentage

```python
# Count and calculate percentage
counts = df.groupby('City').size()
total = len(df)
percentages = (counts / total) * 100
print(percentages)
```

### Pattern 4: Filter After Grouping

```python
# Group, calculate, then filter
result = df.groupby('City')['Score'].mean()
high_avg = result[result > 85]  # Cities with average > 85
print(high_avg)
```

---

## 9. Common Mistakes (And How to Avoid Them)

### Mistake 1: Forgetting to Select Column

```python
# ❌ WRONG - This counts all columns
result = df.groupby('City').count()

# ✅ CORRECT - Select specific column
result = df.groupby('City')['Name'].count()
```

### Mistake 2: Wrong Function Name

```python
# ❌ WRONG
result = df.groupby('City')['Score'].average()  # No 'average' function!

# ✅ CORRECT
result = df.groupby('City')['Score'].mean()  # Use 'mean'
```

### Mistake 3: Forgetting Parentheses

```python
# ❌ WRONG
result = df.groupby('City')['Score'].mean  # Missing parentheses!

# ✅ CORRECT
result = df.groupby('City')['Score'].mean()  # Need parentheses
```

### Mistake 4: Wrong Syntax in `.agg()`

```python
# ❌ WRONG - Missing dictionary
result = df.groupby('City').agg('Score': 'mean')

# ✅ CORRECT - Use dictionary
result = df.groupby('City').agg({'Score': 'mean'})
```

### Mistake 5: Not Understanding the Result

```python
# The result is a Series or DataFrame
result = df.groupby('City')['Score'].mean()
print(type(result))  # <class 'pandas.core.series.Series'>

# You can use it like a Series/DataFrame
print(result['New York'])  # Get value for specific group
```

---

## 10. Quick Reference

### Basic Grouping

```python
# Count
df.groupby('Column').size()
df.groupby('Column')['Name'].count()

# Mean
df.groupby('Column')['Score'].mean()

# Multiple columns
df.groupby('Column')[['Col1', 'Col2']].mean()
```

### Using `.agg()`

```python
# Single function per column
df.groupby('Column').agg({'Score': 'mean', 'Age': 'mean'})

# Multiple functions per column
df.groupby('Column')['Score'].agg(['mean', 'min', 'max'])

# Mixed
df.groupby('Column').agg({
    'Score': ['mean', 'max'],
    'Age': 'mean',
    'Name': 'count'
})
```

### Grouping by Multiple Columns

```python
# Two columns
df.groupby(['Col1', 'Col2'])['Score'].mean()

# Three columns
df.groupby(['Col1', 'Col2', 'Col3'])['Score'].mean()
```

---

## Key Takeaways (Simple Summary)

1. **`groupby()`** — Split data into groups: `df.groupby('Column')`
2. **`.count()`** — Count items in each group
3. **`.mean()`** — Calculate average for each group
4. **`.agg()`** — Apply multiple functions: `agg({'Col': 'function'})`
5. **Select column first** — `df.groupby('Col')['Score'].mean()`
6. **Multiple groups** — `df.groupby(['Col1', 'Col2'])`
7. **Multiple functions** — Use list: `agg(['mean', 'min', 'max'])`

---

## Practice Tips

1. **Start simple** — Get one groupby working, then add complexity
2. **Select columns** — Always specify which column to aggregate
3. **Test your results** — Print and verify the output makes sense
4. **Use `.agg()`** — When you need multiple statistics
5. **Practice with real data** — Try grouping your own datasets

---

## Next Steps

Try the exercises! They're designed to help you practice grouping and aggregation. Remember:
- **`groupby()`** splits data into groups
- **`.mean()`, `.count()`** calculate statistics
- **`.agg()`** is powerful for multiple functions
- **Always select columns** you want to aggregate

You're learning to summarize data like a pro! 🎉

Good luck! 🚀

