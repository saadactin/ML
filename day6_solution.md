# Day 6: Matplotlib Exercises — Solutions

**Note:** Only check these solutions after you've attempted the problems yourself!

Remember: The most important part is understanding how to create plots with proper labels! 📊

---

## Exercise 1: Line Plots

### Solution 1.1

```python
import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create line plot
plt.plot(x, y)

# Add labels (IMPORTANT!)
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.title('Simple Line Plot')

# Show the plot
plt.show()
```

**What you'll see:** A straight line going up from left to right.

---

### Solution 1.2

```python
import matplotlib.pyplot as plt

# Data
days = [1, 2, 3, 4, 5]
temperature = [72, 75, 73, 78, 80]

# Create line plot with markers
plt.plot(days, temperature, marker='o')

# Add labels
plt.xlabel('Day')
plt.ylabel('Temperature (°F)')
plt.title('Temperature Over 5 Days')

# Show the plot
plt.show()
```

**What you'll see:** A line with circles at each point showing temperature changes.

**Note:** The `marker='o'` adds dots at each data point, making it easier to see the exact values.

---

### Solution 1.3

```python
import matplotlib.pyplot as plt

# Data
days = [1, 2, 3, 4, 5]
temp_city_a = [72, 75, 73, 78, 80]
temp_city_b = [68, 70, 69, 72, 74]

# Plot first line
plt.plot(days, temp_city_a, label='City A', marker='o')

# Plot second line
plt.plot(days, temp_city_b, label='City B', marker='s')

# Add labels
plt.xlabel('Day')
plt.ylabel('Temperature (°F)')
plt.title('Temperature Comparison: City A vs City B')
plt.legend()  # Shows which line is which

# Show the plot
plt.show()
```

**What you'll see:** Two lines on the same plot, with a legend box showing which line represents which city.

**Key points:**
- `label='City A'` names the line
- `plt.legend()` creates a box explaining which line is which
- Different markers (`'o'` and `'s'`) help distinguish the lines

---

## Exercise 2: Bar Charts

### Solution 2.1

```python
import matplotlib.pyplot as plt

# Data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
sales = [100, 150, 120, 180, 200]

# Create bar chart
plt.bar(months, sales)

# Add labels
plt.xlabel('Month')
plt.ylabel('Sales ($)')
plt.title('Monthly Sales')

# Show the plot
plt.show()
```

**What you'll see:** Five bars of different heights showing sales for each month.

---

### Solution 2.2

```python
import matplotlib.pyplot as plt

# Data
subjects = ['Math', 'Science', 'English', 'History']
scores = [85, 92, 78, 88]

# Create bar chart with green color
plt.bar(subjects, scores, color='green')

# Add labels
plt.xlabel('Subject')
plt.ylabel('Score')
plt.title('Test Scores by Subject')

# Show the plot
plt.show()
```

**What you'll see:** Four green bars showing scores for each subject.

**Note:** The `color='green'` makes all bars green. You can use any color name like 'blue', 'red', 'orange', etc.

---

### Solution 2.3

```python
import matplotlib.pyplot as plt

# Data
subjects = ['Math', 'Science', 'English', 'History']
scores = [85, 92, 78, 88]

# Create horizontal bar chart
plt.barh(subjects, scores)

# Add labels (note: for horizontal bars, x and y are swapped!)
plt.xlabel('Score')  # This is now the horizontal axis
plt.ylabel('Subject')  # This is now the vertical axis
plt.title('Test Scores by Subject (Horizontal)')

# Show the plot
plt.show()
```

**What you'll see:** Four horizontal bars showing scores for each subject.

**Important note:** For horizontal bars (`barh`), the x and y labels are conceptually swapped:
- `xlabel` describes what's on the horizontal axis (the scores)
- `ylabel` describes what's on the vertical axis (the subjects)

---

## Exercise 3: Scatter Plots

### Solution 3.1

```python
import matplotlib.pyplot as plt

# Data
hours = [1, 2, 3, 4, 5, 6, 7, 8]
scores = [50, 60, 65, 70, 75, 80, 85, 90]

# Create scatter plot
plt.scatter(hours, scores)

# Add labels
plt.xlabel('Hours Studied')
plt.ylabel('Test Score')
plt.title('Study Time vs Test Score')

# Show the plot
plt.show()
```

**What you'll see:** Eight dots showing the relationship between hours studied and test scores. The dots should go up from left to right, showing that more study time = higher scores.

---

### Solution 3.2

```python
import matplotlib.pyplot as plt

# Data
hours = [1, 2, 3, 4, 5, 6, 7, 8]
scores = [50, 60, 65, 70, 75, 80, 85, 90]

# Create scatter plot with customization
plt.scatter(hours, scores, 
            color='red',      # Red points
            s=100,            # Bigger points (size)
            alpha=0.6)        # Slightly transparent

# Add labels
plt.xlabel('Hours Studied')
plt.ylabel('Test Score')
plt.title('Study Time vs Test Score')

# Show the plot
plt.show()
```

**What you'll see:** Red, larger, slightly transparent dots showing the relationship.

**Customization explained:**
- `color='red'` — Makes points red
- `s=100` — Makes points bigger (default is usually 20)
- `alpha=0.6` — Makes points 60% opaque (40% transparent)

---

### Solution 3.3

```python
import matplotlib.pyplot as plt

# Group A data
hours_a = [1, 2, 3, 4, 5]
scores_a = [50, 60, 65, 70, 75]

# Group B data
hours_b = [2, 3, 4, 5, 6]
scores_b = [55, 65, 70, 80, 85]

# Plot Group A
plt.scatter(hours_a, scores_a, 
            label='Group A', 
            color='blue', 
            s=100)

# Plot Group B
plt.scatter(hours_b, scores_b, 
            label='Group B', 
            color='red', 
            s=100)

# Add labels
plt.xlabel('Hours Studied')
plt.ylabel('Test Score')
plt.title('Study Time vs Test Score by Group')
plt.legend()  # Shows which group is which

# Show the plot
plt.show()
```

**What you'll see:** Two sets of dots in different colors (blue for Group A, red for Group B), with a legend showing which color represents which group.

**Key points:**
- Different colors help distinguish groups
- `label='Group A'` names each group
- `plt.legend()` creates a box explaining which color is which group

---

## Additional Practice Ideas

Once you're comfortable with these, try:

1. **Use your own data:**
   ```python
   # Plot your own test scores over time
   my_scores = [85, 88, 90, 87, 92]
   weeks = [1, 2, 3, 4, 5]
   plt.plot(weeks, my_scores, marker='o')
   plt.xlabel('Week')
   plt.ylabel('Score')
   plt.title('My Test Scores Over Time')
   plt.show()
   ```

2. **Experiment with colors:**
   - Try: 'blue', 'red', 'green', 'orange', 'purple', 'cyan', 'magenta'
   - Or use hex codes: '#FF5733', '#33FF57', etc.

3. **Try different markers:**
   - 'o' (circle), 's' (square), '^' (triangle), 'x' (x mark), '+' (plus)

4. **Combine plot types:**
   - You can use `plt.plot()` and `plt.scatter()` on the same plot!

---

## Common Questions

**Q: My plot doesn't show up. What's wrong?**
A: Make sure you have `plt.show()` at the end of your code!

**Q: Can I save my plot instead of showing it?**
A: Yes! Use `plt.savefig('filename.png')` instead of (or before) `plt.show()`

**Q: How do I make my plot bigger?**
A: Add this before creating the plot:
```python
plt.figure(figsize=(10, 6))  # Width, height in inches
```

**Q: Can I change the font size of labels?**
A: Yes! Use:
```python
plt.xlabel('Day', fontsize=14)
plt.ylabel('Temperature', fontsize=14)
plt.title('My Plot', fontsize=16)
```

**Q: What if my x or y labels are too long and get cut off?**
A: Use `plt.tight_layout()` before `plt.show()`:
```python
plt.tight_layout()
plt.show()
```

---

## Key Takeaways

✅ **Always import:** `import matplotlib.pyplot as plt`

✅ **Three essential labels:**
   - `plt.xlabel()` — What's on the x-axis
   - `plt.ylabel()` — What's on the y-axis
   - `plt.title()` — What the plot shows

✅ **Always show:** `plt.show()` at the end

✅ **Line plots:** Use `plt.plot()` for trends over time

✅ **Bar charts:** Use `plt.bar()` for comparing categories

✅ **Scatter plots:** Use `plt.scatter()` for relationships

✅ **Legends:** Use `plt.legend()` when showing multiple groups/lines

---

## Final Reminder

**The most important rule:** Always label your axes! A plot without labels is like a map without a legend — it doesn't help anyone understand what they're looking at.

**Great job completing the exercises! 🎉**

You've learned how to create visualizations — that's a super valuable skill for data analysis and sharing insights!

