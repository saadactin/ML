# Day 5: NumPy Operations Exercises — Solutions

**Note:** Only check these solutions after you've attempted the problems yourself!

Remember: It's okay if you didn't get it right the first time. Learning takes practice! 💪

---

## Exercise 1: Basic Math Operations

### Solution 1.1

```python
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Add them together
result_add = arr1 + arr2
print("Addition:", result_add)  # [5 7 9]

# Subtract arr2 from arr1
result_sub = arr1 - arr2
print("Subtraction:", result_sub)  # [-3 -3 -3]
```

**Explanation:**
- Addition: 1+4=5, 2+5=7, 3+6=9
- Subtraction: 1-4=-3, 2-5=-3, 3-6=-3

---

### Solution 1.2

```python
import numpy as np

arr = np.array([2, 4, 6, 8, 10])

# Multiply every number by 3
multiplied = arr * 3
print("Multiplied by 3:", multiplied)  # [ 6 12 18 24 30]

# Add 5 to every number
added = arr + 5
print("Added 5:", added)  # [ 7  9 11 13 15]
```

**Explanation:**
- Multiplying: 2×3=6, 4×3=12, 6×3=18, 8×3=24, 10×3=30
- Adding: 2+5=7, 4+5=9, 6+5=11, 8+5=13, 10+5=15

---

### Solution 1.3

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

# Square each number (raise to power of 2)
squared = arr ** 2
print("Squared:", squared)  # [ 1  4  9 16 25]
```

**Explanation:**
- 1² = 1
- 2² = 4
- 3² = 9
- 4² = 16
- 5² = 25

---

## Exercise 2: Aggregation Functions

### Solution 2.1

```python
import numpy as np

scores = np.array([85, 90, 78, 92, 88])

# Find the sum (total)
total = scores.sum()
print("Total:", total)  # 433

# Find the mean (average)
average = scores.mean()
print("Average:", average)  # 86.6
```

**Explanation:**
- Sum: 85 + 90 + 78 + 92 + 88 = 433
- Mean: 433 ÷ 5 = 86.6

---

### Solution 2.2

```python
import numpy as np

temperatures = np.array([72, 75, 68, 80, 73])

# Find maximum (hottest)
hottest = temperatures.max()
print("Hottest:", hottest)  # 80

# Find minimum (coldest)
coldest = temperatures.min()
print("Coldest:", coldest)  # 68
```

**Explanation:**
- Maximum: 80 is the highest temperature
- Minimum: 68 is the lowest temperature

---

### Solution 2.3

```python
import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

# Find standard deviation
std_dev = numbers.std()
print("Standard deviation:", std_dev)  # 14.142...
```

**Explanation:**
- Standard deviation measures how spread out the numbers are
- For these numbers (10, 20, 30, 40, 50), the std is about 14.14
- Don't worry about the exact calculation - just know it measures "spread"

---

## Exercise 3: 2D Arrays

### Solution 3.1

```python
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

# Sum of ALL numbers
total_all = arr.sum()
print("Sum of all:", total_all)  # 21

# Sum of each ROW (axis=1 means across)
row_sums = arr.sum(axis=1)
print("Sum of each row:", row_sums)  # [6 15]
# Row 0: 1+2+3 = 6
# Row 1: 4+5+6 = 15

# Sum of each COLUMN (axis=0 means down)
col_sums = arr.sum(axis=0)
print("Sum of each column:", col_sums)  # [5 7 9]
# Column 0: 1+4 = 5
# Column 1: 2+5 = 7
# Column 2: 3+6 = 9
```

**Explanation:**
- **All numbers**: 1+2+3+4+5+6 = 21
- **Rows (axis=1)**: Think "going across" each row
  - Row 0: 1+2+3 = 6
  - Row 1: 4+5+6 = 15
- **Columns (axis=0)**: Think "going down" each column
  - Column 0: 1+4 = 5
  - Column 1: 2+5 = 7
  - Column 2: 3+6 = 9

---

### Solution 3.2

```python
import numpy as np

grades = np.array([[85, 90, 88], [78, 82, 80]])

# Average of ALL grades
overall_avg = grades.mean()
print("Average of all grades:", overall_avg)  # 83.833...

# Average of each ROW (each student's average)
student_averages = grades.mean(axis=1)
print("Each student's average:", student_averages)  # [87.67 80.  ]
# Student 0: (85+90+88)÷3 = 87.67
# Student 1: (78+82+80)÷3 = 80.0
```

**Explanation:**
- **All grades**: (85+90+88+78+82+80) ÷ 6 = 83.83
- **Each student (axis=1)**: Average across their tests
  - Student 0: (85+90+88) ÷ 3 = 87.67
  - Student 1: (78+82+80) ÷ 3 = 80.0

---

## Additional Practice Ideas

Once you're comfortable with these, try:

1. **Real-world practice:**
   ```python
   # Your own test scores
   my_scores = np.array([...])  # Fill in your scores
   print(f"My average: {my_scores.mean()}")
   ```

2. **Combine operations:**
   ```python
   arr = np.array([1, 2, 3, 4, 5])
   result = (arr * 2) + 10
   print(result)  # What do you think this will be?
   ```

3. **Experiment:**
   - Try different arrays
   - Try different operations
   - See what happens!

---

## Common Questions

**Q: Why do I get decimal numbers sometimes?**
A: When you divide or calculate averages, Python uses floating-point numbers (decimals). This is normal!

**Q: What's the difference between axis=0 and axis=1?**
A: 
- `axis=0` = **down** (think: going down the rows, working with columns)
- `axis=1` = **across** (think: going across the columns, working with rows)

**Q: Can I use these operations on regular Python lists?**
A: No, these are NumPy-specific. You need to convert lists to arrays first: `np.array([1, 2, 3])`

---

## Key Takeaways

✅ **Math operations** work on entire arrays automatically
✅ **Aggregation functions** give you one answer from many numbers
✅ **axis=0** = down (columns), **axis=1** = across (rows)
✅ **Practice makes perfect** - Keep trying and you'll get it!

---

**Great job completing the exercises! 🎉**

Remember: Every expert was once a beginner. You're learning something new, and that's awesome! Keep practicing and don't give up! 💪

