# Day 5: NumPy Operations — Mathematical Operations and Aggregation

## Introduction

Today we'll learn how to do **math with arrays**! NumPy makes it super easy to:
- Add, subtract, multiply, divide arrays
- Find averages, sums, and other statistics
- Do calculations on entire arrays at once

**Don't worry!** We'll go step by step and use simple examples. You've got this! 💪

---

## 1. Mathematical Operations — Easy as 1, 2, 3!

### What are Mathematical Operations?

Mathematical operations are just fancy words for:
- **Addition** (+)
- **Subtraction** (-)
- **Multiplication** (×)
- **Division** (÷)
- **Power** (raising to a power, like 2³)

The cool thing about NumPy: you can do these operations on **entire arrays at once**!

### Adding Arrays Together

Think of it like adding two shopping lists together:

```python
import numpy as np

# Two arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Add them together
result = arr1 + arr2
print(result)  # [5 7 9]

# What happened?
# Position 0: 1 + 4 = 5
# Position 1: 2 + 5 = 7
# Position 2: 3 + 6 = 9
```

**It's that simple!** NumPy adds each position together automatically.

### Subtracting Arrays

Same idea, but with subtraction:

```python
arr1 = np.array([10, 20, 30])
arr2 = np.array([3, 5, 7])

result = arr1 - arr2
print(result)  # [7 15 23]

# What happened?
# Position 0: 10 - 3 = 7
# Position 1: 20 - 5 = 15
# Position 2: 30 - 7 = 23
```

### Multiplying Arrays

**Important:** This is **NOT** matrix multiplication. It multiplies each position:

```python
arr1 = np.array([2, 3, 4])
arr2 = np.array([5, 6, 7])

result = arr1 * arr2
print(result)  # [10 18 28]

# What happened?
# Position 0: 2 × 5 = 10
# Position 1: 3 × 6 = 18
# Position 2: 4 × 7 = 28
```

### Dividing Arrays

```python
arr1 = np.array([10, 20, 30])
arr2 = np.array([2, 4, 5])

result = arr1 / arr2
print(result)  # [5. 5. 6.]

# What happened?
# Position 0: 10 ÷ 2 = 5.0
# Position 1: 20 ÷ 4 = 5.0
# Position 2: 30 ÷ 5 = 6.0
```

### Power (Raising to a Power)

```python
arr = np.array([2, 3, 4])

# Square each number (raise to power of 2)
result = arr ** 2
print(result)  # [4 9 16]

# What happened?
# Position 0: 2² = 4
# Position 1: 3² = 9
# Position 2: 4² = 16

# Cube each number (raise to power of 3)
result = arr ** 3
print(result)  # [8 27 64]
```

### Operations with a Single Number

You can also do operations with just **one number** (called a "scalar"):

```python
arr = np.array([1, 2, 3, 4, 5])

# Add 10 to every number
result = arr + 10
print(result)  # [11 12 13 14 15]

# Multiply every number by 2
result = arr * 2
print(result)  # [2 4 6 8 10]

# Divide every number by 2
result = arr / 2
print(result)  # [0.5 1. 1.5 2. 2.5]
```

**This is super useful!** You can change all numbers in an array at once.

### Real-World Example

Let's say you have test scores and want to add a bonus point to everyone:

```python
scores = np.array([85, 90, 78, 92, 88])

# Add 5 bonus points to everyone
bonus_scores = scores + 5
print(bonus_scores)  # [90 95 83 97 93]
```

---

## 2. Aggregation Functions — Finding Totals and Averages

### What is Aggregation?

**Aggregation** means "bringing things together" to get one answer. Like:
- What's the **total** of all numbers?
- What's the **average** of all numbers?
- What's the **biggest** number?
- What's the **smallest** number?

### Finding the Sum (Total)

Add up all the numbers in an array:

```python
arr = np.array([1, 2, 3, 4, 5])

total = arr.sum()
print(total)  # 15

# What happened?
# 1 + 2 + 3 + 4 + 5 = 15
```

**Real example:** Total sales for the week:
```python
daily_sales = np.array([100, 150, 200, 180, 120])
weekly_total = daily_sales.sum()
print(f"Total sales: ${weekly_total}")  # Total sales: $750
```

### Finding the Mean (Average)

Find the average of all numbers:

```python
arr = np.array([10, 20, 30, 40, 50])

average = arr.mean()
print(average)  # 30.0

# What happened?
# (10 + 20 + 30 + 40 + 50) ÷ 5 = 30.0
```

**Real example:** Average test score:
```python
test_scores = np.array([85, 90, 78, 92, 88])
average_score = test_scores.mean()
print(f"Average score: {average_score}")  # Average score: 86.6
```

### Finding the Maximum (Biggest Number)

```python
arr = np.array([3, 7, 2, 9, 1, 5])

maximum = arr.max()
print(maximum)  # 9

# Or you can use:
maximum = np.max(arr)
print(maximum)  # 9 (same thing)
```

**Real example:** Highest temperature:
```python
temperatures = np.array([72, 75, 68, 80, 73])
hottest = temperatures.max()
print(f"Hottest day: {hottest}°F")  # Hottest day: 80°F
```

### Finding the Minimum (Smallest Number)

```python
arr = np.array([3, 7, 2, 9, 1, 5])

minimum = arr.min()
print(minimum)  # 1

# Or you can use:
minimum = np.min(arr)
print(minimum)  # 1 (same thing)
```

**Real example:** Lowest score:
```python
scores = np.array([85, 90, 78, 92, 88])
lowest = scores.min()
print(f"Lowest score: {lowest}")  # Lowest score: 78
```

### Finding Standard Deviation (Spread of Numbers)

**Standard deviation** tells you how "spread out" your numbers are.

**Simple explanation:**
- **Small standard deviation** = numbers are close together (like [9, 10, 11])
- **Large standard deviation** = numbers are far apart (like [1, 10, 20])

```python
# Numbers close together
arr1 = np.array([9, 10, 11])
std1 = arr1.std()
print(std1)  # Small number (about 0.82)

# Numbers far apart
arr2 = np.array([1, 10, 20])
std2 = arr2.std()
print(std2)  # Large number (about 7.79)
```

**Real example:** Test score consistency:
```python
class_a = np.array([85, 87, 86, 88, 84])  # Consistent scores
class_b = np.array([60, 90, 70, 95, 75])  # Varied scores

print(f"Class A std: {class_a.std():.2f}")  # Small (about 1.41)
print(f"Class B std: {class_b.std():.2f}")  # Large (about 12.25)
```

### Quick Reference: Common Aggregation Functions

```python
arr = np.array([1, 2, 3, 4, 5])

print(arr.sum())    # 15 (total)
print(arr.mean())   # 3.0 (average)
print(arr.max())    # 5 (biggest)
print(arr.min())    # 1 (smallest)
print(arr.std())    # 1.41... (spread)
```

---

## 3. Working with 2D Arrays (Tables)

### What are 2D Arrays?

Think of a 2D array like a **table** with rows and columns:

```
     Column 0  Column 1  Column 2
Row 0    1        2        3
Row 1    4        5        6
Row 2    7        8        9
```

### Summing 2D Arrays

You can sum in different ways:

```python
arr = np.array([[1, 2, 3], 
                [4, 5, 6], 
                [7, 8, 9]])

# Sum of ALL numbers
total = arr.sum()
print(total)  # 45

# Sum of each ROW (across columns)
row_sums = arr.sum(axis=1)
print(row_sums)  # [6 15 24]
# Row 0: 1+2+3 = 6
# Row 1: 4+5+6 = 15
# Row 2: 7+8+9 = 24

# Sum of each COLUMN (down rows)
col_sums = arr.sum(axis=0)
print(col_sums)  # [12 15 18]
# Column 0: 1+4+7 = 12
# Column 1: 2+5+8 = 15
# Column 2: 3+6+9 = 18
```

**Memory trick:**
- `axis=0` = **down** (think "going down the rows")
- `axis=1` = **across** (think "going across the columns")

### Mean of 2D Arrays

Same idea with averages:

```python
arr = np.array([[10, 20, 30], 
                [40, 50, 60]])

# Average of ALL numbers
overall_avg = arr.mean()
print(overall_avg)  # 35.0

# Average of each ROW
row_avgs = arr.mean(axis=1)
print(row_avgs)  # [20. 50.]
# Row 0: (10+20+30)÷3 = 20
# Row 1: (40+50+60)÷3 = 50

# Average of each COLUMN
col_avgs = arr.mean(axis=0)
print(col_avgs)  # [25. 35. 45.]
# Column 0: (10+40)÷2 = 25
# Column 1: (20+50)÷2 = 35
# Column 2: (30+60)÷2 = 45
```

### Real-World Example: Student Grades

```python
# Each row is a student, each column is a test
grades = np.array([[85, 90, 88],  # Student 1
                   [78, 82, 80],  # Student 2
                   [92, 87, 95]]) # Student 3

# Average grade for each student (each row)
student_averages = grades.mean(axis=1)
print(student_averages)  # [87.67 80.   91.33]

# Average score for each test (each column)
test_averages = grades.mean(axis=0)
print(test_averages)  # [85. 86.33 87.67]
```

---

## 4. Combining Operations

You can combine multiple operations:

```python
arr = np.array([1, 2, 3, 4, 5])

# Step 1: Multiply by 2
step1 = arr * 2  # [2 4 6 8 10]

# Step 2: Add 10
step2 = step1 + 10  # [12 14 16 18 20]

# Or do it all at once:
result = arr * 2 + 10
print(result)  # [12 14 16 18 20]
```

**Real example:** Convert Celsius to Fahrenheit:
```python
celsius = np.array([0, 10, 20, 30, 40])
fahrenheit = celsius * 9/5 + 32
print(fahrenheit)  # [32. 50. 68. 86. 104.]
```

---

## 5. Common Patterns

### Pattern 1: Normalize Data (Make numbers between 0 and 1)

```python
scores = np.array([50, 75, 100, 25])

# Find min and max
min_score = scores.min()  # 25
max_score = scores.max()  # 100

# Normalize: (value - min) / (max - min)
normalized = (scores - min_score) / (max_score - min_score)
print(normalized)  # [0.33 0.67 1.   0.  ]
```

### Pattern 2: Find Differences

```python
temperatures = np.array([72, 75, 68, 80, 73])

# Find difference from average
avg_temp = temperatures.mean()  # 73.6
differences = temperatures - avg_temp
print(differences)  # [-1.6  1.4 -5.6  6.4 -0.6]
```

### Pattern 3: Count How Many Meet a Condition

```python
scores = np.array([85, 90, 78, 92, 88])

# Count how many are above 85
above_85 = (scores > 85).sum()
print(above_85)  # 3

# What happened?
# scores > 85 gives: [False True False True True]
# .sum() counts True as 1, False as 0
# So: 0 + 1 + 0 + 1 + 1 = 3
```

---

## 6. Common Mistakes (And How to Avoid Them)

### Mistake 1: Forgetting NumPy Operations are Element-Wise

```python
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# This multiplies each position (NOT matrix multiplication)
result = arr1 * arr2  # [4 10 18]
# NOT: [[1×4 + 2×5 + 3×6]] = 32
```

### Mistake 2: Wrong Axis for 2D Arrays

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])

# axis=0 = down (columns)
col_sum = arr.sum(axis=0)  # [5 7 9] ✓

# axis=1 = across (rows)
row_sum = arr.sum(axis=1)  # [6 15] ✓
```

**Memory trick:** 
- `axis=0` = **0** looks like going **down** ↓
- `axis=1` = **1** looks like going **across** →

### Mistake 3: Using Python's Built-in Functions

```python
arr = np.array([1, 2, 3, 4, 5])

# ❌ WRONG - Python's sum (slower)
total = sum(arr)

# ✅ CORRECT - NumPy's sum (faster)
total = arr.sum()
# or
total = np.sum(arr)
```

---

## Key Takeaways (Simple Summary)

1. **Math operations** work on entire arrays: `arr1 + arr2`, `arr * 2`
2. **Sum** adds everything: `arr.sum()` → total
3. **Mean** finds average: `arr.mean()` → average
4. **Max/Min** finds biggest/smallest: `arr.max()`, `arr.min()`
5. **Std** measures spread: `arr.std()` → how spread out
6. **2D arrays**: `axis=0` = down (columns), `axis=1` = across (rows)
7. **Operations are element-wise**: Each position is calculated separately

---

## Practice Tips

1. **Start simple** - Try operations on small arrays first
2. **Print everything** - See what each step does
3. **Use real examples** - Think of test scores, temperatures, etc.
4. **Don't memorize** - Understand the concept, then practice
5. **It's okay to make mistakes** - That's how you learn!

---

## Next Steps

Try the exercises! They're designed to be easy and build your confidence. Remember: every expert was once a beginner. You're doing great! 🎉

Good luck! 🚀

