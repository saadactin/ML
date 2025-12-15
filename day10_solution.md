# Day 10: Selecting Data Exercises — Solutions

**Note:** Only check these solutions after you've attempted the problems yourself!

Remember: The goal is to understand how to select columns and filter rows. Take your time! 💪

---

## Exercise 1: Selecting Columns

### Solution 1.1

```python
import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Age': [25, 30, 35, 28],
    'Score': [85, 90, 78, 92],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
})

# Select and print just the 'Name' column
print("Name column:")
print(df['Name'])

# Select and print just the 'Age' column
print("\nAge column:")
print(df['Age'])

# Select and print both 'Name' and 'Score' columns together
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
- `df['Name']` returns a Series (one column)
- `df[['Name', 'Score']]` returns a DataFrame (multiple columns)
- Notice the double brackets `[[]]` for multiple columns!

---

### Solution 1.2

```python
import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Age': [25, 30, 35, 28],
    'Score': [85, 90, 78, 92],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
})

# Select and print 'Name', 'Age', and 'City' columns
print("Name, Age, and City columns:")
print(df[['Name', 'Age', 'City']])

# Check the types
print("\nType when selecting one column:")
print(type(df['Name']))  # <class 'pandas.core.series.Series'>

print("\nType when selecting multiple columns:")
print(type(df[['Name', 'Age']]))  # <class 'pandas.core.frame.DataFrame'>
```

**Output:**
```
Name, Age, and City columns:
      Name  Age        City
0    Alice   25    New York
1      Bob   30  Los Angeles
2  Charlie   35      Chicago
3    Diana   28     Houston

Type when selecting one column:
<class 'pandas.core.series.Series'>

Type when selecting multiple columns:
<class 'pandas.core.frame.DataFrame'>
```

**Key insight:**
- **Single column** → Returns a **Series**
- **Multiple columns** → Returns a **DataFrame**
- This is why you need double brackets for multiple columns!

---

## Exercise 2: Basic Row Filtering

### Solution 2.1

```python
import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Age': [25, 30, 35, 28],
    'Score': [85, 90, 78, 92],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
})

# Filter rows where Age is greater than 28
print("People older than 28:")
print(df[df['Age'] > 28])

# Filter rows where Score is greater than or equal to 85
print("\nPeople with score >= 85:")
print(df[df['Score'] >= 85])
```

**Output:**
```
People older than 28:
      Name  Age  Score        City
1      Bob   30     90  Los Angeles
2  Charlie   35     78      Chicago

People with score >= 85:
    Name  Age  Score        City
0  Alice   25     85    New York
1    Bob   30     90  Los Angeles
3  Diana   28     92     Houston
```

**Explanation:**
- `df['Age'] > 28` creates a boolean Series (True/False for each row)
- `df[condition]` keeps only rows where condition is True
- `>=` means "greater than or equal to"

---

### Solution 2.2

```python
import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Age': [25, 30, 35, 28],
    'Score': [85, 90, 78, 92],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
})

# Filter rows where Age equals 30
print("People who are 30:")
print(df[df['Age'] == 30])

# Filter rows where City is 'New York'
print("\nPeople from New York:")
print(df[df['City'] == 'New York'])

# Filter rows where Score is less than 80
print("\nPeople with score < 80:")
print(df[df['Score'] < 80])
```

**Output:**
```
People who are 30:
  Name  Age  Score        City
1  Bob   30     90  Los Angeles

People from New York:
    Name  Age  Score      City
0  Alice   25     85  New York

People with score < 80:
      Name  Age  Score     City
2  Charlie   35     78  Chicago
```

**Explanation:**
- Use `==` for equality (not `=`)
- Text comparisons are case-sensitive: `'New York'` not `'new york'`
- `<` means "less than"

---

### Solution 2.3

```python
import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank'],
    'Age': [25, 30, 35, 28, 22, 40],
    'Score': [85, 90, 78, 92, 88, 75]
})

# Filter rows where Age > 25 AND Score > 85
print("People older than 25 AND score > 85:")
result = df[(df['Age'] > 25) & (df['Score'] > 85)]
print(result)
```

**Output:**
```
People older than 25 AND score > 85:
    Name  Age  Score
1    Bob   30     90
3  Diana   28     92
4    Eve   22     88
```

**Explanation:**
- Use `&` for AND (not `and`)
- **Important:** Put each condition in parentheses: `(df['Age'] > 25) & (df['Score'] > 85)`
- Without parentheses, you'll get an error!

**Why parentheses?** Python needs to know the order of operations. Without them, it tries to do `df['Age'] > (25 & df['Score'])` which doesn't make sense.

---

### Solution 2.4

```python
import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank'],
    'Age': [25, 30, 35, 28, 22, 40],
    'Score': [85, 90, 78, 92, 88, 75]
})

# Filter rows where Age > 35 OR Score < 80
print("People older than 35 OR score < 80:")
result = df[(df['Age'] > 35) | (df['Score'] < 80)]
print(result)
```

**Output:**
```
People older than 35 OR score < 80:
      Name  Age  Score
2  Charlie   35     78
5    Frank   40     75
```

**Explanation:**
- Use `|` for OR (not `or`)
- **Important:** Put each condition in parentheses: `(df['Age'] > 35) | (df['Score'] < 80)`
- OR means "at least one condition must be True"
- Charlie: Age 35 (not > 35) but Score 78 (< 80) → True
- Frank: Age 40 (> 35) and Score 75 (< 80) → True

---

## Exercise 3: Combining Selection and Filtering

### Solution 3.1

```python
import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank'],
    'Age': [25, 30, 35, 28, 22, 40],
    'Score': [85, 90, 78, 92, 88, 75]
})

# Filter rows where Score > 85, then select Name and Score columns
print("Names and scores for people with score > 85:")
result = df[df['Score'] > 85][['Name', 'Score']]
print(result)
```

**Output:**
```
Names and scores for people with score > 85:
    Name  Score
1    Bob     90
3  Diana     92
4    Eve     88
```

**Explanation:**
- Step 1: `df[df['Score'] > 85]` filters rows (scores > 85)
- Step 2: `[['Name', 'Score']]` selects columns (Name and Score)
- Read it as: "From the filtered data, get Name and Score columns"

---

### Solution 3.2

```python
import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank'],
    'Age': [25, 30, 35, 28, 22, 40],
    'Score': [85, 90, 78, 92, 88, 75]
})

# Filter rows where Age is between 25 and 35 (inclusive)
# Then select Name and Age columns
print("Names and ages for people aged 25-35:")
result = df[(df['Age'] >= 25) & (df['Age'] <= 35)][['Name', 'Age']]
print(result)
```

**Output:**
```
Names and ages for people aged 25-35:
      Name  Age
0    Alice   25
1      Bob   30
2  Charlie   35
3    Diana   28
```

**Explanation:**
- `(df['Age'] >= 25) & (df['Age'] <= 35)` means "Age is 25 or more AND 35 or less"
- This gives us ages 25, 26, 27, ..., 35 (inclusive range)
- Then we select only Name and Age columns

---

### Solution 3.3

```python
import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'Age': [25, 30, 35, 28, 22],
    'Score': [85, 90, 78, 92, 88],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
})

# Filter rows where Score > 85 AND City is 'New York' OR 'Los Angeles'
# Then select Name, Score, and City columns
print("People with score > 85 from New York or Los Angeles:")
result = df[(df['Score'] > 85) & (df['City'].isin(['New York', 'Los Angeles']))][['Name', 'Score', 'City']]
print(result)
```

**Output:**
```
People with score > 85 from New York or Los Angeles:
  Name  Score        City
1  Bob     90  Los Angeles
```

**Explanation:**
- `df['City'].isin(['New York', 'Los Angeles'])` checks if City is in the list
- This is equivalent to: `(df['City'] == 'New York') | (df['City'] == 'Los Angeles')`
- `.isin()` is cleaner when checking multiple values
- Combined with `&` for the Score condition
- Then select Name, Score, and City columns

**Alternative approach:**
```python
# Same result, different syntax
result = df[(df['Score'] > 85) & ((df['City'] == 'New York') | (df['City'] == 'Los Angeles'))][['Name', 'Score', 'City']]
```

---

## Additional Practice Ideas

Once you're comfortable with these, try:

1. **More complex filters:**
   ```python
   # People with scores in top 3
   top_3 = df.nlargest(3, 'Score')
   
   # People with names starting with 'A'
   names_a = df[df['Name'].str.startswith('A')]
   ```

2. **Chaining multiple operations:**
   ```python
   # Filter, select, then get statistics
   result = df[df['Age'] > 30]['Score'].mean()
   ```

3. **Practice with your own data:**
   - Create a CSV with your data
   - Load it and practice filtering and selecting

---

## Common Questions

**Q: Why do I need double brackets for multiple columns?**
A: 
- Single brackets `[]` are for indexing (one column → Series)
- Double brackets `[[]]` create a list of columns (multiple columns → DataFrame)
- It's how Pandas distinguishes between "get one thing" vs "get multiple things"

**Q: Why can't I use `and` instead of `&`?**
A: 
- Python's `and` is for single True/False values
- Pandas `&` is for element-wise operations on arrays
- Each row gets checked individually with `&`

**Q: Do I always need parentheses?**
A: 
- Yes, when using `&` or `|` with multiple conditions
- Without them, Python gets confused about operator precedence
- Better safe than sorry - always use them!

**Q: Can I filter on text columns?**
A: 
- Yes! Use `==` for exact match: `df[df['City'] == 'New York']`
- Use `.str.startswith()`, `.str.contains()`, etc. for pattern matching
- Use `.isin()` for multiple values

**Q: What's the difference between `&` and `|`?**
A:
- `&` (AND): Both conditions must be True
- `|` (OR): At least one condition must be True

---

## Key Takeaways

✅ **Single column:** `df['Column']` → Series (one bracket)

✅ **Multiple columns:** `df[['Col1', 'Col2']]` → DataFrame (double brackets!)

✅ **Filter rows:** `df[condition]` where condition is `df['Column'] > value`

✅ **AND condition:** `(cond1) & (cond2)` - use `&` with parentheses

✅ **OR condition:** `(cond1) | (cond2)` - use `|` with parentheses

✅ **Combine both:** Filter first, then select: `df[condition][['Col1', 'Col2']]`

✅ **Use `==` for equality** (not `=`)

✅ **Always use parentheses** when combining conditions

---

## Final Reminder

**The most important things to remember:**
1. **Double brackets** for multiple columns: `[[]]`
2. **Parentheses** for combined conditions: `(cond1) & (cond2)`
3. **Filter then select** for clarity: `df[filter][['cols']]`
4. **Use `==` not `=`** for comparisons

**Great job completing the exercises! 🎉**

You've learned how to select columns and filter rows - these are essential skills for working with data. Keep practicing and you'll get faster and more comfortable with it!

