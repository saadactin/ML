# Day 11: DataFrame Operations Exercises — Solutions

**Note:** Only check these solutions after you've attempted the problems yourself!

Remember: The goal is to understand how to add/remove columns and use the `.apply()` method. Take your time! 💪

---

## Exercise 1: Adding Columns

### Solution 1.1

```python
import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Age': [25, 30, 35, 28],
    'Score': [85, 90, 78, 92]
})

# Add a column 'Status' with the value 'Active' for all rows
df['Status'] = 'Active'

# Add a column 'City' with specific values
df['City'] = ['New York', 'Los Angeles', 'Chicago', 'Houston']

# Print the DataFrame
print(df)
```

**Output:**
```
      Name  Age  Score  Status        City
0    Alice   25     85  Active    New York
1      Bob   30     90  Active  Los Angeles
2  Charlie   35     78  Active      Chicago
3    Diana   28     92  Active     Houston
```

**Explanation:**
- `df['Status'] = 'Active'` adds a column with the same value for all rows
- `df['City'] = [list]` adds a column with different values (must match number of rows)
- The new columns appear on the right side of the DataFrame

---

### Solution 1.2

```python
import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Age': [25, 30, 35, 28],
    'Score': [85, 90, 78, 92]
})

# Add a column 'Total_Points' that is Age + Score
df['Total_Points'] = df['Age'] + df['Score']

# Add a column 'Score_Per_Age' that is Score divided by Age
df['Score_Per_Age'] = df['Score'] / df['Age']

# Print the DataFrame
print(df)
```

**Output:**
```
      Name  Age  Score  Total_Points  Score_Per_Age
0    Alice   25     85           110       3.400000
1      Bob   30     90           120       3.000000
2  Charlie   35     78           113       2.228571
3    Diana   28     92           120       3.285714
```

**Explanation:**
- `df['Age'] + df['Score']` performs element-wise addition (25+85=110, 30+90=120, etc.)
- `df['Score'] / df['Age']` performs element-wise division (85/25=3.4, 90/30=3.0, etc.)
- Calculations are done row by row automatically

---

### Solution 1.3

```python
import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Age': [25, 30, 35, 28],
    'Score': [85, 90, 78, 92]
})

# Add a column 'Grade' based on Score using apply() with lambda
df['Grade'] = df['Score'].apply(lambda x: 'A' if x >= 90 else 'B' if x >= 80 else 'C')

# Print the DataFrame
print(df)
```

**Output:**
```
      Name  Age  Score Grade
0    Alice   25     85     B
1      Bob   30     90     A
2  Charlie   35     78     C
3    Diana   28     92     A
```

**Explanation:**
- `lambda x: 'A' if x >= 90 else 'B' if x >= 80 else 'C'` is a nested conditional
- For each Score value:
  - If >= 90 → 'A'
  - Else if >= 80 → 'B'
  - Else → 'C'
- `.apply()` applies this function to each value in the 'Score' column

**Alternative approach using NumPy:**
```python
import numpy as np
df['Grade'] = np.where(df['Score'] >= 90, 'A',
              np.where(df['Score'] >= 80, 'B', 'C'))
```

---

## Exercise 2: Removing Columns

### Solution 2.1

```python
import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Score': [85, 90, 78],
    'City': ['NY', 'LA', 'CHI'],
    'Country': ['USA', 'USA', 'USA']
})

# Remove the 'City' column using drop()
df = df.drop('City', axis=1)

# Remove the 'Country' column using del
del df['Country']

# Print the DataFrame
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
- `df.drop('City', axis=1)` removes the 'City' column (axis=1 means columns)
- We reassign `df = ...` because `drop()` returns a new DataFrame by default
- `del df['Country']` directly modifies the DataFrame (no reassignment needed)
- Both methods achieve the same result

**Alternative with inplace:**
```python
df.drop('City', axis=1, inplace=True)  # Modifies df directly
```

---

### Solution 2.2

```python
import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Score': [85, 90, 78],
    'Temp1': [1, 2, 3],
    'Temp2': [4, 5, 6]
})

# Remove both 'Temp1' and 'Temp2' columns in one operation
df = df.drop(['Temp1', 'Temp2'], axis=1)

# Print the DataFrame
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
- `drop(['Temp1', 'Temp2'], axis=1)` removes multiple columns at once
- Pass a list of column names to remove multiple columns
- `axis=1` is still required (means "columns")

**Alternative:**
```python
# Using inplace
df.drop(['Temp1', 'Temp2'], axis=1, inplace=True)
```

---

## Exercise 3: Using `.apply()` Method

### Solution 3.1

```python
import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    'Name': ['alice', 'bob', 'charlie']
})

# Use apply() to convert all names to uppercase
df['Name'] = df['Name'].apply(str.upper)
# Or: df['Name'] = df['Name'].apply(lambda x: x.upper())

# Print the DataFrame
print(df)
```

**Output:**
```
      Name
0    ALICE
1      BOB
2  CHARLIE
```

**Explanation:**
- `str.upper` is a built-in string method (note: no parentheses when passing as argument)
- `.apply(str.upper)` applies the upper() method to each string
- Each name is converted to uppercase

**Alternative with lambda:**
```python
df['Name'] = df['Name'].apply(lambda x: x.upper())
```

---

### Solution 3.2

```python
import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    'Numbers': [1, 2, 3, 4, 5]
})

# Use apply() with lambda to create 'Squared' column
df['Squared'] = df['Numbers'].apply(lambda x: x ** 2)

# Print the DataFrame
print(df)
```

**Output:**
```
   Numbers  Squared
0        1        1
1        2        4
2        3        9
3        4       16
4        5       25
```

**Explanation:**
- `lambda x: x ** 2` is a function that squares each value
- `x` represents each number in the 'Numbers' column
- `x ** 2` squares the number
- `.apply()` applies this to each value: 1²=1, 2²=4, 3²=9, etc.

**Note:** For simple operations like this, you could also do:
```python
df['Squared'] = df['Numbers'] ** 2  # Simpler, no apply needed
```
But using `.apply()` is good practice for learning!

---

### Solution 3.3

```python
import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    'Score': [85, 90, 78, 92, 88]
})

# Use apply() with lambda to create 'Result' column
df['Result'] = df['Score'].apply(lambda x: 'Pass' if x >= 80 else 'Fail')

# Print the DataFrame
print(df)
```

**Output:**
```
   Score Result
0     85   Pass
1     90   Pass
2     78   Fail
3     92   Pass
4     88   Pass
```

**Explanation:**
- `lambda x: 'Pass' if x >= 80 else 'Fail'` is a conditional expression
- For each Score:
  - If Score >= 80 → 'Pass'
  - Otherwise → 'Fail'
- Scores 85, 90, 92, 88 are >= 80 → 'Pass'
- Score 78 is < 80 → 'Fail'

---

### Solution 3.4

```python
import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    'Name': ['Alice Smith', 'Bob Johnson', 'Charlie Brown']
})

# Use apply() with lambda to create 'Name_Length' column
df['Name_Length'] = df['Name'].apply(lambda x: len(x))

# Print the DataFrame
print(df)
```

**Output:**
```
            Name  Name_Length
0    Alice Smith           11
1    Bob Johnson           11
2  Charlie Brown           13
```

**Explanation:**
- `lambda x: len(x)` gets the length of each string
- `len('Alice Smith')` = 11 (including the space)
- `len('Bob Johnson')` = 11
- `len('Charlie Brown')` = 13
- `.apply()` calculates the length for each name

**Alternative:**
```python
# You could also use the built-in len function directly
df['Name_Length'] = df['Name'].apply(len)
```

---

## Additional Practice Ideas

Once you're comfortable with these, try:

1. **More complex calculations:**
   ```python
   # Calculate percentage
   df['Percentage'] = df['Score'].apply(lambda x: (x / 100) * 100)
   
   # Format text
   df['Formatted'] = df['Name'].apply(lambda x: f"Student: {x}")
   ```

2. **Using regular functions:**
   ```python
   def categorize_age(age):
       if age < 25:
           return 'Young'
       elif age < 35:
           return 'Adult'
       else:
           return 'Senior'
   
   df['Age_Group'] = df['Age'].apply(categorize_age)
   ```

3. **Chaining operations:**
   ```python
   # Clean and transform in one go
   df['Name'] = df['Name'].apply(lambda x: x.strip().upper())
   ```

---

## Common Questions

**Q: When should I use `.apply()` vs direct operations?**
A:
- **Direct operations** (`df['Col'] * 2`) for simple math
- **`.apply()`** for complex logic, functions, or transformations

**Q: Do I need parentheses when using `str.upper` in apply()?**
A:
- No! Pass the function itself: `apply(str.upper)`
- Not: `apply(str.upper())` (this would call it immediately)

**Q: Can I use `.apply()` on the entire DataFrame?**
A:
- Yes! `df.apply(function)` applies to each element
- Use `axis=0` for rows or `axis=1` for columns if needed

**Q: What's the difference between `drop()` with and without `inplace=True`?**
A:
- Without `inplace=True`: Returns new DataFrame (need to reassign)
- With `inplace=True`: Modifies original DataFrame directly

**Q: Can I add a column with different data types?**
A:
- Yes! Pandas handles mixed types, but it's better to keep consistent types in a column

---

## Key Takeaways

✅ **Add column:** `df['New_Col'] = values` (constant, list, or calculation)

✅ **Remove column:** `df.drop('Col', axis=1)` or `del df['Col']`

✅ **Remove multiple:** `df.drop(['Col1', 'Col2'], axis=1)`

✅ **`.apply()` with lambda:** `df['Col'].apply(lambda x: expression)`

✅ **`.apply()` with function:** `df['Col'].apply(function_name)`

✅ **Always use `axis=1`** when dropping columns

✅ **Reassign or use `inplace=True`** when using `drop()`

✅ **List length must match** number of rows when adding columns

---

## Final Reminder

**The most important things to remember:**
1. **Adding columns** is simple assignment: `df['New'] = values`
2. **Removing columns** needs `axis=1`: `df.drop('Col', axis=1)`
3. **`.apply()`** is powerful for transformations
4. **Lambda functions** are great for simple operations: `lambda x: expression`

**Great job completing the exercises! 🎉**

You've learned how to add/remove columns and use the `.apply()` method - these are essential skills for data manipulation. Keep practicing and you'll get faster and more comfortable with it!

