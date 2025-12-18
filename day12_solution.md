# Day 12: Grouping and Aggregation Exercises — Solutions

**Note:** Only check these solutions after you've attempted the problems yourself!

Remember: The goal is to understand how to group data and calculate statistics. Take your time! 💪

---

## Exercise 1: Basic Grouping

### Solution 1.1

```python
import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank'],
    'City': ['New York', 'Los Angeles', 'New York', 'Chicago', 'Los Angeles', 'Chicago'],
    'Score': [85, 90, 78, 92, 88, 75]
})

# Group by 'City' and count people in each city
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

**Explanation:**
- `df.groupby('City')` groups rows by City values
- `['Name']` selects the Name column to count
- `.count()` counts how many names (people) in each city
- Each city has 2 people

**Alternative:**
```python
# Using size() - simpler for counting rows
result = df.groupby('City').size()
print(result)
```

---

### Solution 1.2

```python
import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank'],
    'City': ['New York', 'Los Angeles', 'New York', 'Chicago', 'Los Angeles', 'Chicago'],
    'Score': [85, 90, 78, 92, 88, 75]
})

# Group by 'City' and calculate average score
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

**Explanation:**
- `df.groupby('City')` groups by City
- `['Score']` selects the Score column
- `.mean()` calculates the average score for each city
- Chicago: (92 + 75) / 2 = 83.5
- Los Angeles: (90 + 88) / 2 = 89.0
- New York: (85 + 78) / 2 = 81.5

**Key point:** Always select the column you want to aggregate: `['Score']`

---

### Solution 1.3

```python
import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank'],
    'City': ['New York', 'Los Angeles', 'New York', 'Chicago', 'Los Angeles', 'Chicago'],
    'Score': [85, 90, 78, 92, 88, 75]
})

# Group by 'City' and calculate min and max score
result = df.groupby('City')['Score'].agg(['min', 'max'])
print(result)
```

**Output:**
```
            min  max
City                
Chicago       75   92
Los Angeles   88   90
New York      78   85
```

**Explanation:**
- `df.groupby('City')['Score']` groups by City and selects Score column
- `.agg(['min', 'max'])` applies both min and max functions
- Result shows minimum and maximum score for each city
- Chicago: min=75, max=92
- Los Angeles: min=88, max=90
- New York: min=78, max=85

**Key point:** Pass a list of function names to `.agg()` for multiple functions

---

## Exercise 2: Using `.agg()` Method

### Solution 2.1

```python
import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank'],
    'Department': ['Sales', 'Sales', 'IT', 'IT', 'Sales', 'IT'],
    'Score': [85, 90, 78, 92, 88, 75],
    'Age': [25, 30, 35, 28, 22, 40]
})

# Group by 'Department' and use agg() for multiple statistics
result = df.groupby('Department').agg({
    'Score': 'mean',
    'Name': 'count'
})
print(result)
```

**Output:**
```
            Score  Name
Department             
IT           81.67     3
Sales        87.67     3
```

**Explanation:**
- `df.groupby('Department')` groups by Department
- `.agg({'Score': 'mean', 'Name': 'count'})` applies:
  - 'mean' to Score column (average score)
  - 'count' to Name column (number of people)
- IT: average score 81.67, 3 people
- Sales: average score 87.67, 3 people

**Calculation check:**
- IT scores: (78 + 92 + 75) / 3 = 81.67
- Sales scores: (85 + 90 + 88) / 3 = 87.67

---

### Solution 2.2

```python
import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank'],
    'Department': ['Sales', 'Sales', 'IT', 'IT', 'Sales', 'IT'],
    'Score': [85, 90, 78, 92, 88, 75],
    'Age': [25, 30, 35, 28, 22, 40]
})

# Group by 'Department' and calculate multiple statistics for Score
result = df.groupby('Department')['Score'].agg(['mean', 'min', 'max', 'count'])
print(result)
```

**Output:**
```
            mean  min  max  count
Department                       
IT         81.67   75   92      3
Sales      87.67   85   90      3
```

**Explanation:**
- `df.groupby('Department')['Score']` groups by Department and selects Score
- `.agg(['mean', 'min', 'max', 'count'])` applies 4 functions:
  - mean: average score
  - min: minimum score
  - max: maximum score
  - count: number of scores
- Result shows all 4 statistics for each department

**Key point:** When applying multiple functions to one column, pass a list of function names

---

### Solution 2.3

```python
import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank'],
    'Department': ['Sales', 'Sales', 'IT', 'IT', 'Sales', 'IT'],
    'Score': [85, 90, 78, 92, 88, 75],
    'Age': [25, 30, 35, 28, 22, 40]
})

# Group by 'Department' and use agg() with different functions for different columns
result = df.groupby('Department').agg({
    'Score': ['mean', 'max'],
    'Age': ['mean', 'min'],
    'Name': 'count'
})
print(result)
```

**Output:**
```
           Score      Age  Name
            mean  max  mean  min count
Department                           
IT         81.67   92  34.33   28     3
Sales      87.67   90  25.67   22     3
```

**Explanation:**
- `df.groupby('Department')` groups by Department
- `.agg({...})` applies different functions to different columns:
  - Score: mean and max (2 functions)
  - Age: mean and min (2 functions)
  - Name: count (1 function)
- Result shows all statistics in a multi-level column structure

**Key point:** You can mix single functions and lists of functions in the dictionary

---

## Exercise 3: Multiple Grouping and Real-World Scenarios

### Solution 3.1

```python
import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank', 'Grace', 'Henry'],
    'City': ['New York', 'New York', 'Chicago', 'Chicago', 'New York', 'Chicago', 'New York', 'Chicago'],
    'Department': ['Sales', 'IT', 'Sales', 'IT', 'Sales', 'IT', 'Sales', 'IT'],
    'Score': [85, 90, 78, 92, 88, 75, 95, 82]
})

# Group by both 'City' and 'Department', calculate average score
result = df.groupby(['City', 'Department'])['Score'].mean()
print(result)
```

**Output:**
```
City      Department
Chicago   IT           83.5
          Sales        78.0
New York  IT           90.0
          Sales        89.0
Name: Score, dtype: float64
```

**Explanation:**
- `df.groupby(['City', 'Department'])` groups by both columns
- Creates groups for each combination:
  - Chicago-IT
  - Chicago-Sales
  - New York-IT
  - New York-Sales
- `.mean()` calculates average score for each combination
- Chicago-IT: (92 + 75) / 2 = 83.5
- Chicago-Sales: 78.0 (only one person)
- New York-IT: 90.0 (only one person)
- New York-Sales: (85 + 88 + 95) / 3 = 89.0

**Key point:** Pass a list of column names to group by multiple columns

---

### Solution 3.2

```python
import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank', 'Grace', 'Henry'],
    'City': ['New York', 'New York', 'Chicago', 'Chicago', 'New York', 'Chicago', 'New York', 'Chicago'],
    'Department': ['Sales', 'IT', 'Sales', 'IT', 'Sales', 'IT', 'Sales', 'IT'],
    'Score': [85, 90, 78, 92, 88, 75, 95, 82]
})

# Group by 'City', calculate count and average score
result = df.groupby('City').agg({
    'Name': 'count',
    'Score': 'mean'
})
print(result)
```

**Output:**
```
          Name  Score
City                 
Chicago      4  81.75
New York     4  89.50
```

**Explanation:**
- `df.groupby('City')` groups by City
- `.agg({'Name': 'count', 'Score': 'mean'})` calculates:
  - Count of names (number of people) in each city
  - Average score in each city
- Chicago: 4 people, average score 81.75
- New York: 4 people, average score 89.50

**Calculation check:**
- Chicago scores: (78 + 92 + 75 + 82) / 4 = 81.75
- New York scores: (85 + 90 + 88 + 95) / 4 = 89.50

---

### Solution 3.3

```python
import pandas as pd

# Create DataFrame with sales data
df = pd.DataFrame({
    'Product': ['A', 'A', 'B', 'B', 'C', 'C', 'A', 'B'],
    'Salesperson': ['John', 'Jane', 'John', 'Jane', 'John', 'Jane', 'John', 'Jane'],
    'Sales': [100, 150, 200, 180, 120, 130, 110, 190]
})

# Group by 'Product', calculate total and average sales
result = df.groupby('Product').agg({
    'Sales': ['sum', 'mean']
})
print(result)
```

**Output:**
```
        Sales      
          sum   mean
Product             
A         360  120.0
B         570  190.0
C         250  125.0
```

**Explanation:**
- `df.groupby('Product')` groups by Product
- `.agg({'Sales': ['sum', 'mean']})` calculates:
  - sum: total sales for each product
  - mean: average sales for each product
- Product A: total 360, average 120.0
- Product B: total 570, average 190.0
- Product C: total 250, average 125.0

**Calculation check:**
- Product A: (100 + 150 + 110) = 360, average = 360/3 = 120.0
- Product B: (200 + 180 + 190) = 570, average = 570/3 = 190.0
- Product C: (120 + 130) = 250, average = 250/2 = 125.0

---

## Additional Practice Ideas

Once you're comfortable with these, try:

1. **More complex aggregations:**
   ```python
   # Calculate percentage of total
   result = df.groupby('City').agg({
       'Name': 'count',
       'Score': ['mean', 'std']
   })
   ```

2. **Filter after grouping:**
   ```python
   # Group, calculate, then filter
   result = df.groupby('City')['Score'].mean()
   high_avg = result[result > 85]
   ```

3. **Real-world scenarios:**
   - Group sales by month and calculate totals
   - Group students by class and find averages
   - Group products by category and find best sellers

---

## Common Questions

**Q: What's the difference between `.count()` and `.size()`?**
A:
- `.count()` counts non-null values (excludes missing data)
- `.size()` counts all rows (includes missing data)
- Usually they're the same, but `.size()` is simpler for counting rows

**Q: Can I group by more than 2 columns?**
A:
- Yes! `df.groupby(['Col1', 'Col2', 'Col3'])` works for any number of columns

**Q: What if I want to group but not aggregate?**
A:
- `groupby()` returns a GroupBy object
- You need to apply a function (mean, count, etc.) to get results
- You can iterate over groups if needed: `for name, group in df.groupby('City'):`

**Q: Can I use custom functions in `.agg()`?**
A:
- Yes! You can pass function names as strings or actual functions
- `agg({'Score': 'mean'})` or `agg({'Score': lambda x: x.max() - x.min()})`

**Q: What's the difference between `.agg()` and individual methods?**
A:
- Individual methods (`.mean()`, `.count()`) are simpler for one function
- `.agg()` is better when you need multiple functions or different functions for different columns

---

## Key Takeaways

✅ **`groupby()`** - Split data into groups: `df.groupby('Column')`

✅ **Select column first** - `df.groupby('Col')['Score'].mean()` not just `df.groupby('Col').mean()`

✅ **`.count()`** - Count items in each group

✅ **`.mean()`** - Calculate average for each group

✅ **`.agg()`** - Apply multiple functions: `agg({'Col': 'function'})` or `agg(['func1', 'func2'])`

✅ **Multiple grouping** - `df.groupby(['Col1', 'Col2'])`

✅ **Dictionary in `.agg()`** - Different functions for different columns

---

## Final Reminder

**The most important things to remember:**
1. **Always select columns** before aggregating: `['Score']`
2. **Use `.agg()`** when you need multiple statistics
3. **Group by multiple columns** using a list: `['Col1', 'Col2']`
4. **Dictionary syntax** for `.agg()`: `{'Column': 'function'}`

**Great job completing the exercises! 🎉**

You've learned how to group data and calculate statistics - these are essential skills for data analysis. Keep practicing and you'll get faster and more comfortable with grouping and aggregation!

