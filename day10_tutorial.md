# Day 10: Selecting Data in Pandas — Columns and Filtering Rows

## Introduction

Once you've loaded and inspected your data, the next step is to **select** the data you need. This means:
- **Selecting columns** — Getting specific columns you want
- **Filtering rows** — Getting rows that meet certain conditions

**Why is this important?**
- **Focus on what matters** — Work with only the data you need
- **Answer questions** — "Who scored above 90?" "What are the ages?"
- **Prepare for analysis** — Get the right data before processing
- **Save time** — Don't work with unnecessary data

**What we'll learn today:**
- Selecting single columns
- Selecting multiple columns
- Filtering rows with conditions (>, <, ==, etc.)
- Combining filters (AND, OR)
- Common patterns and examples

**Don't worry!** We'll go step by step with simple examples. You've got this! 💪

---

## 1. Getting Started — Sample Data

Let's create some sample data to work with:

```python
import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank'],
    'Age': [25, 30, 35, 28, 22, 40],
    'Score': [85, 90, 78, 92, 88, 75],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia']
})

print(df)
```

**This is our data** — 6 people with their information.

---

## 2. Selecting Columns

### What is Column Selection?

**Column selection** means getting specific columns (like getting just the "Name" column or "Name" and "Score" columns).

### Selecting a Single Column

**Method 1: Using square brackets**

```python
import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank'],
    'Age': [25, 30, 35, 28, 22, 40],
    'Score': [85, 90, 78, 92, 88, 75]
})

# Select one column
ages = df['Age']
print(ages)
```

**Output:**
```
0    25
1    30
2    35
3    28
4    22
5    40
Name: Age, dtype: int64
```

**What you get:** A **Series** (one column of data)

**Method 2: Using dot notation**

```python
# Same thing, different syntax
ages = df.Age
print(ages)
```

**Same result!** But square brackets `[]` are more common and safer.

### Selecting Multiple Columns

To select multiple columns, use **double square brackets** `[[]]`:

```python
import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank'],
    'Age': [25, 30, 35, 28, 22, 40],
    'Score': [85, 90, 78, 92, 88, 75],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia']
})

# Select multiple columns
subset = df[['Name', 'Score']]
print(subset)
```

**Output:**
```
      Name  Score
0    Alice     85
1      Bob     90
2  Charlie     78
3    Diana     92
4      Eve     88
5    Frank     75
```

**What you get:** A **DataFrame** (table with selected columns)

**Important:** 
- Single column: `df['Age']` → Series
- Multiple columns: `df[['Name', 'Score']]` → DataFrame
- Notice the **double brackets** `[[]]` for multiple columns!

### Examples of Column Selection

```python
# Get just names
names = df['Name']

# Get names and ages
name_age = df[['Name', 'Age']]

# Get names, ages, and scores
name_age_score = df[['Name', 'Age', 'Score']]

# Get all columns except one (we'll learn this later)
```

---

## 3. Filtering Rows — The Basics

### What is Row Filtering?

**Row filtering** means getting only rows that meet certain conditions (like "only people older than 30" or "only scores above 85").

### Creating Conditions

A **condition** is a comparison that gives `True` or `False` for each row.

**Basic comparison operators:**
- `>` — greater than
- `<` — less than
- `>=` — greater than or equal
- `<=` — less than or equal
- `==` — equal to
- `!=` — not equal to

### Simple Filtering Example

**Question:** Who scored above 85?

```python
import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank'],
    'Age': [25, 30, 35, 28, 22, 40],
    'Score': [85, 90, 78, 92, 88, 75]
})

# Create condition: scores > 85
condition = df['Score'] > 85
print(condition)
```

**Output:**
```
0    False
1     True
2    False
3     True
4     True
5    False
Name: Score, dtype: bool
```

**What this shows:** `True` for rows where score > 85, `False` otherwise.

**Now use the condition to filter:**

```python
# Filter rows where condition is True
high_scores = df[df['Score'] > 85]
print(high_scores)
```

**Output:**
```
    Name  Age  Score
1    Bob   30     90
3  Diana   28     92
4    Eve   22     88
```

**What happened:**
- `df['Score'] > 85` creates a boolean Series (True/False)
- `df[condition]` keeps only rows where condition is True
- Result: Only people with scores above 85!

### Common Filtering Patterns

**Pattern 1: Greater than**

```python
# People older than 30
older_than_30 = df[df['Age'] > 30]
print(older_than_30)
```

**Pattern 2: Less than**

```python
# Scores less than 80
low_scores = df[df['Score'] < 80]
print(low_scores)
```

**Pattern 3: Equal to**

```python
# People exactly 30 years old
age_30 = df[df['Age'] == 30]
print(age_30)
```

**Pattern 4: Not equal to**

```python
# People not from New York
not_ny = df[df['City'] != 'New York']
print(not_ny)
```

**Pattern 5: Greater than or equal**

```python
# Scores 85 or higher
good_scores = df[df['Score'] >= 85]
print(good_scores)
```

---

## 4. Multiple Conditions — AND and OR

### Combining Conditions with AND

**Question:** Who is older than 25 AND scored above 85?

Use `&` (ampersand) for AND:

```python
import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank'],
    'Age': [25, 30, 35, 28, 22, 40],
    'Score': [85, 90, 78, 92, 88, 75]
})

# Both conditions must be True
result = df[(df['Age'] > 25) & (df['Score'] > 85)]
print(result)
```

**Output:**
```
    Name  Age  Score
1    Bob   30     90
3  Diana   28     92
4    Eve   22     88
```

**Important:** 
- Use `&` for AND (not `and`)
- Put each condition in parentheses: `(condition1) & (condition2)`

**Why parentheses?** Without them, Python gets confused about the order of operations.

### Combining Conditions with OR

**Question:** Who is older than 35 OR scored below 80?

Use `|` (pipe) for OR:

```python
# Either condition can be True
result = df[(df['Age'] > 35) | (df['Score'] < 80)]
print(result)
```

**Output:**
```
      Name  Age  Score
2  Charlie   35     78
5    Frank   40     75
```

**Important:**
- Use `|` for OR (not `or`)
- Put each condition in parentheses: `(condition1) | (condition2)`

### AND vs OR — Understanding the Difference

**AND (`&`):** Both conditions must be True
- Age > 25 **AND** Score > 85
- Must satisfy BOTH

**OR (`|`):** At least one condition must be True
- Age > 35 **OR** Score < 80
- Must satisfy AT LEAST ONE

---

## 5. Combining Column Selection and Filtering

### Select Columns AND Filter Rows

You can do both at once!

**Example:** Get names and scores for people who scored above 85:

```python
import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank'],
    'Age': [25, 30, 35, 28, 22, 40],
    'Score': [85, 90, 78, 92, 88, 75]
})

# Filter rows first, then select columns
result = df[df['Score'] > 85][['Name', 'Score']]
print(result)
```

**Output:**
```
    Name  Score
1    Bob     90
3  Diana     92
4    Eve     88
```

**What happened:**
1. `df[df['Score'] > 85]` — Filter rows (scores > 85)
2. `[['Name', 'Score']]` — Select columns (Name and Score)

**Read it as:** "From the filtered data, get Name and Score columns"

### Another Example

**Get names of people older than 30:**

```python
names_old = df[df['Age'] > 30]['Name']
print(names_old)
```

**Output:**
```
2    Charlie
5      Frank
Name: Name, dtype: object
```

---

## 6. Common Patterns and Examples

### Pattern 1: Find Top Performers

```python
# People with scores in top 3
top_scores = df.nlargest(3, 'Score')
print(top_scores)

# Or using filtering
top_scores = df[df['Score'] >= 90]
print(top_scores)
```

### Pattern 2: Find Specific Values

```python
# People from a specific city
ny_people = df[df['City'] == 'New York']
print(ny_people)
```

### Pattern 3: Range Filtering

```python
# Ages between 25 and 35 (inclusive)
age_range = df[(df['Age'] >= 25) & (df['Age'] <= 35)]
print(age_range)
```

### Pattern 4: Multiple Values

```python
# People from specific cities
cities = ['New York', 'Chicago', 'Houston']
selected = df[df['City'].isin(cities)]
print(selected)
```

**Note:** `.isin()` checks if a value is in a list.

### Pattern 5: Text Filtering

```python
# Names starting with 'A'
names_a = df[df['Name'].str.startswith('A')]
print(names_a)

# Names containing 'an'
names_an = df[df['Name'].str.contains('an')]
print(names_an)
```

---

## 7. Common Mistakes (And How to Avoid Them)

### Mistake 1: Using `and` instead of `&`

```python
# ❌ WRONG
result = df[df['Age'] > 25 and df['Score'] > 85]  # Error!

# ✅ CORRECT
result = df[(df['Age'] > 25) & (df['Score'] > 85)]
```

**Why:** Pandas uses `&` for element-wise AND, not Python's `and`.

### Mistake 2: Forgetting Parentheses

```python
# ❌ WRONG
result = df[df['Age'] > 25 & df['Score'] > 85]  # Error!

# ✅ CORRECT
result = df[(df['Age'] > 25) & (df['Score'] > 85)]
```

**Why:** Without parentheses, Python doesn't know the order of operations.

### Mistake 3: Using `=` instead of `==`

```python
# ❌ WRONG
result = df[df['Age'] = 30]  # SyntaxError!

# ✅ CORRECT
result = df[df['Age'] == 30]
```

**Why:** `=` is assignment, `==` is comparison.

### Mistake 4: Wrong Brackets for Multiple Columns

```python
# ❌ WRONG
result = df['Name', 'Score']  # Error!

# ✅ CORRECT
result = df[['Name', 'Score']]  # Double brackets!
```

**Why:** Single brackets `[]` for one column, double brackets `[[]]` for multiple.

### Mistake 5: Filtering Before Selecting (Wrong Order)

```python
# This works, but is less clear:
result = df[['Name', 'Score']][df['Score'] > 85]  # Works but confusing

# Better - filter first, then select:
result = df[df['Score'] > 85][['Name', 'Score']]  # Clearer!
```

---

## 8. Quick Reference

### Selecting Columns

```python
# Single column (returns Series)
df['Age']
df.Age  # Same thing

# Multiple columns (returns DataFrame)
df[['Name', 'Age', 'Score']]
```

### Filtering Rows

```python
# Single condition
df[df['Age'] > 30]
df[df['Score'] >= 85]
df[df['City'] == 'New York']

# Multiple conditions (AND)
df[(df['Age'] > 25) & (df['Score'] > 85)]

# Multiple conditions (OR)
df[(df['Age'] > 35) | (df['Score'] < 80)]
```

### Combining Both

```python
# Filter rows, then select columns
df[df['Score'] > 85][['Name', 'Score']]
```

---

## Key Takeaways (Simple Summary)

1. **Select single column:** `df['ColumnName']` → Series
2. **Select multiple columns:** `df[['Col1', 'Col2']]` → DataFrame (double brackets!)
3. **Filter rows:** `df[condition]` where condition is `df['Column'] > value`
4. **AND condition:** Use `&` with parentheses: `(cond1) & (cond2)`
5. **OR condition:** Use `|` with parentheses: `(cond1) | (cond2)`
6. **Combine both:** Filter first, then select: `df[condition][['Col1', 'Col2']]`
7. **Use `==` for equality** (not `=`)
8. **Always use parentheses** when combining conditions

---

## Practice Tips

1. **Start simple** — Get one filter working, then add more
2. **Test your conditions** — Print the condition first to see True/False
3. **Read it out loud** — "Get rows where Age is greater than 30"
4. **Use parentheses** — Always use them with `&` and `|`
5. **Practice with real data** — Try filtering your own datasets

---

## Next Steps

Try the exercises! They're designed to help you practice selecting columns and filtering rows. Remember:
- **Single column:** One bracket `[]`
- **Multiple columns:** Double brackets `[[]]`
- **Filtering:** `df[condition]`
- **AND/OR:** Use `&` and `|` with parentheses

You're learning to work with data like a pro! 🎉

Good luck! 🚀

