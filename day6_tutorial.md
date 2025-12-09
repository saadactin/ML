# Day 6: Introduction to Matplotlib — Basic Plots and Charts

## Introduction

**Matplotlib** is a library for creating visualizations (graphs and charts) in Python. Think of it as a tool to turn your data into pictures!

**Why visualize data?**
- **Easier to understand** — A picture is worth a thousand words!
- **Spot patterns** — See trends and relationships quickly
- **Share insights** — Show others what your data means
- **Make decisions** — Visual data helps you make better choices

**What we'll learn today:**
- Creating line plots (like a line graph)
- Creating bar charts (like a bar graph)
- Creating scatter plots (dots showing relationships)
- Adding labels and titles to make charts clear

**Don't worry!** We'll start simple and build up. You've got this! 💪

---

## 1. Getting Started with Matplotlib

### Installation

If Matplotlib isn't installed:
```bash
pip install matplotlib
```

### Importing Matplotlib

The standard way to import:
```python
import matplotlib.pyplot as plt
```

We use `plt` as a short name (it's the convention everyone uses).

### Your First Plot

Let's create a simple line plot:

```python
import matplotlib.pyplot as plt

# Some data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create the plot
plt.plot(x, y)

# Show the plot
plt.show()
```

**What happened?**
- `x` = horizontal values (left to right)
- `y` = vertical values (bottom to top)
- `plt.plot()` = creates a line connecting the points
- `plt.show()` = displays the plot

**Result:** You'll see a line going up from left to right!

---

## 2. Line Plots — Showing Trends Over Time

### What is a Line Plot?

A **line plot** shows how something changes over time or across categories. Think of it like connecting dots with a line.

**When to use:** Showing trends, changes over time, or continuous data.

### Basic Line Plot

```python
import matplotlib.pyplot as plt

# Data: temperature over 7 days
days = [1, 2, 3, 4, 5, 6, 7]
temperature = [72, 75, 73, 78, 80, 77, 75]

# Create line plot
plt.plot(days, temperature)

# Show the plot
plt.show()
```

**What you'll see:** A line showing how temperature changes day by day.

### Adding Labels and Title

**Always label your axes!** This makes your plot understandable:

```python
import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5, 6, 7]
temperature = [72, 75, 73, 78, 80, 77, 75]

# Create the plot
plt.plot(days, temperature)

# Add labels (IMPORTANT!)
plt.xlabel('Day')  # Label for x-axis (horizontal)
plt.ylabel('Temperature (°F)')  # Label for y-axis (vertical)
plt.title('Temperature Over a Week')  # Title at the top

# Show the plot
plt.show()
```

**Why labels matter:**
- Without labels, no one knows what the plot shows
- Labels make your plot professional and clear
- Always include: x-label, y-label, and title!

### Customizing Line Plots

You can make your plots look better:

```python
import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5, 6, 7]
temperature = [72, 75, 73, 78, 80, 77, 75]

# Create plot with customization
plt.plot(days, temperature, 
         color='blue',      # Line color
         marker='o',         # Show dots at each point
         linewidth=2,       # Make line thicker
         markersize=8)      # Make dots bigger

# Add labels
plt.xlabel('Day')
plt.ylabel('Temperature (°F)')
plt.title('Temperature Over a Week')

plt.show()
```

**Common options:**
- `color='red'` or `color='blue'` — Change line color
- `marker='o'` — Show circles at each point
- `marker='s'` — Show squares
- `marker='x'` — Show X marks
- `linewidth=2` — Make line thicker (default is 1)
- `linestyle='--'` — Dashed line
- `linestyle=':'` — Dotted line

### Multiple Lines on One Plot

You can compare multiple things:

```python
import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5, 6, 7]
temp_city_a = [72, 75, 73, 78, 80, 77, 75]
temp_city_b = [68, 70, 69, 72, 74, 71, 70]

# Plot first line
plt.plot(days, temp_city_a, label='City A', marker='o')

# Plot second line
plt.plot(days, temp_city_b, label='City B', marker='s')

# Add labels
plt.xlabel('Day')
plt.ylabel('Temperature (°F)')
plt.title('Temperature Comparison')
plt.legend()  # Show which line is which

plt.show()
```

**Key points:**
- `label='City A'` — Name for this line
- `plt.legend()` — Shows a box explaining which line is which

---

## 3. Bar Charts — Comparing Categories

### What is a Bar Chart?

A **bar chart** uses bars (rectangles) to compare different categories. Think of it like a bar graph.

**When to use:** Comparing different categories, showing counts, or comparing groups.

### Basic Bar Chart

```python
import matplotlib.pyplot as plt

# Data: sales by month
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
sales = [100, 150, 120, 180, 200]

# Create bar chart
plt.bar(months, sales)

# Add labels
plt.xlabel('Month')
plt.ylabel('Sales ($)')
plt.title('Monthly Sales')

plt.show()
```

**What you'll see:** Bars of different heights showing sales for each month.

### Customizing Bar Charts

Make your bars look better:

```python
import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
sales = [100, 150, 120, 180, 200]

# Create bar chart with customization
plt.bar(months, sales, 
        color='green',      # Bar color
        width=0.6)          # Bar width (0.6 = 60% of space)

# Add labels
plt.xlabel('Month')
plt.ylabel('Sales ($)')
plt.title('Monthly Sales')

plt.show()
```

**Common options:**
- `color='blue'` — Bar color
- `width=0.6` — Bar width (default is 0.8)
- `edgecolor='black'` — Edge color around bars
- `linewidth=2` — Edge thickness

### Horizontal Bar Chart

Sometimes horizontal bars are better:

```python
import matplotlib.pyplot as plt

categories = ['Math', 'Science', 'English', 'History']
scores = [85, 92, 78, 88]

# Create horizontal bar chart
plt.barh(categories, scores)  # Note: barh (horizontal)

# Add labels
plt.xlabel('Score')
plt.ylabel('Subject')
plt.title('Test Scores by Subject')

plt.show()
```

**When to use horizontal bars:**
- When category names are long
- When you have many categories
- When it's easier to read horizontally

---

## 4. Scatter Plots — Showing Relationships

### What is a Scatter Plot?

A **scatter plot** shows individual points (dots) to see relationships between two things.

**When to use:** Finding relationships, correlations, or patterns between two variables.

### Basic Scatter Plot

```python
import matplotlib.pyplot as plt

# Data: hours studied vs test score
hours = [1, 2, 3, 4, 5, 6, 7, 8]
scores = [50, 60, 65, 70, 75, 80, 85, 90]

# Create scatter plot
plt.scatter(hours, scores)

# Add labels
plt.xlabel('Hours Studied')
plt.ylabel('Test Score')
plt.title('Study Time vs Test Score')

plt.show()
```

**What you'll see:** Dots showing the relationship. More hours = higher score? The plot shows you!

### Customizing Scatter Plots

Make your scatter plots clearer:

```python
import matplotlib.pyplot as plt

hours = [1, 2, 3, 4, 5, 6, 7, 8]
scores = [50, 60, 65, 70, 75, 80, 85, 90]

# Create scatter plot with customization
plt.scatter(hours, scores,
            color='red',        # Point color
            s=100,              # Point size
            alpha=0.6,          # Transparency (0-1)
            edgecolors='black') # Edge color

# Add labels
plt.xlabel('Hours Studied')
plt.ylabel('Test Score')
plt.title('Study Time vs Test Score')

plt.show()
```

**Common options:**
- `color='blue'` — Point color
- `s=100` — Point size (bigger number = bigger points)
- `alpha=0.6` — Transparency (0 = invisible, 1 = solid)
- `edgecolors='black'` — Edge around points
- `marker='s'` — Use squares instead of circles

### Multiple Groups in Scatter Plot

Compare different groups:

```python
import matplotlib.pyplot as plt

# Group A data
hours_a = [1, 2, 3, 4, 5]
scores_a = [50, 60, 65, 70, 75]

# Group B data
hours_b = [2, 3, 4, 5, 6]
scores_b = [55, 65, 70, 80, 85]

# Plot both groups
plt.scatter(hours_a, scores_a, label='Group A', color='blue', s=100)
plt.scatter(hours_b, scores_b, label='Group B', color='red', s=100)

# Add labels
plt.xlabel('Hours Studied')
plt.ylabel('Test Score')
plt.title('Study Time vs Test Score by Group')
plt.legend()  # Show which group is which

plt.show()
```

---

## 5. Important: Always Label Your Axes!

### Why Labels Matter

**Without labels:**
```
[Shows a plot with numbers but no explanation]
```
→ Nobody knows what it means!

**With labels:**
```
X-axis: "Day"
Y-axis: "Temperature (°F)"
Title: "Temperature Over a Week"
```
→ Everyone understands!

### The Three Essential Labels

Every plot should have:

1. **X-axis label** — What the horizontal axis represents
   ```python
   plt.xlabel('Day')
   ```

2. **Y-axis label** — What the vertical axis represents
   ```python
   plt.ylabel('Temperature (°F)')
   ```

3. **Title** — What the whole plot shows
   ```python
   plt.title('Temperature Over a Week')
   ```

### Complete Example with All Labels

```python
import matplotlib.pyplot as plt

# Data
days = [1, 2, 3, 4, 5]
sales = [100, 150, 120, 180, 200]

# Create plot
plt.plot(days, sales, marker='o')

# ALWAYS include these three:
plt.xlabel('Day')              # What's on the x-axis?
plt.ylabel('Sales ($)')        # What's on the y-axis?
plt.title('Daily Sales')       # What does this plot show?

plt.show()
```

**Remember:** A plot without labels is like a book without a title — confusing!

---

## 6. Common Patterns and Examples

### Pattern 1: Simple Trend Over Time

```python
import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr']
revenue = [1000, 1200, 1100, 1300]

plt.plot(months, revenue, marker='o', linewidth=2)
plt.xlabel('Month')
plt.ylabel('Revenue ($)')
plt.title('Monthly Revenue Trend')
plt.show()
```

### Pattern 2: Comparing Categories

```python
import matplotlib.pyplot as plt

fruits = ['Apple', 'Banana', 'Orange', 'Grape']
count = [25, 30, 20, 15]

plt.bar(fruits, count, color='skyblue')
plt.xlabel('Fruit')
plt.ylabel('Count')
plt.title('Fruit Inventory')
plt.show()
```

### Pattern 3: Finding Relationships

```python
import matplotlib.pyplot as plt

age = [20, 25, 30, 35, 40, 45]
salary = [30000, 40000, 50000, 60000, 70000, 80000]

plt.scatter(age, salary, s=100, alpha=0.6)
plt.xlabel('Age')
plt.ylabel('Salary ($)')
plt.title('Age vs Salary')
plt.show()
```

---

## 7. Common Mistakes (And How to Avoid Them)

### Mistake 1: Forgetting to Show the Plot

```python
# ❌ WRONG - Plot is created but never shown
plt.plot([1, 2, 3], [4, 5, 6])
# Missing plt.show()!

# ✅ CORRECT
plt.plot([1, 2, 3], [4, 5, 6])
plt.show()  # Don't forget this!
```

### Mistake 2: Forgetting Labels

```python
# ❌ WRONG - No one knows what this shows
plt.plot(days, temperature)
plt.show()

# ✅ CORRECT - Clear and understandable
plt.plot(days, temperature)
plt.xlabel('Day')
plt.ylabel('Temperature (°F)')
plt.title('Temperature Over Time')
plt.show()
```

### Mistake 3: Wrong Data Format

```python
# ❌ WRONG - Lists must be same length
x = [1, 2, 3]
y = [4, 5]  # Different length!

# ✅ CORRECT - Same length
x = [1, 2, 3]
y = [4, 5, 6]  # Same length
```

### Mistake 4: Forgetting to Import

```python
# ❌ WRONG
plot([1, 2, 3], [4, 5, 6])  # NameError!

# ✅ CORRECT
import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [4, 5, 6])
```

---

## 8. Quick Reference

### Line Plot
```python
plt.plot(x, y, color='blue', marker='o')
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Title')
plt.show()
```

### Bar Chart
```python
plt.bar(categories, values, color='green')
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Title')
plt.show()
```

### Scatter Plot
```python
plt.scatter(x, y, color='red', s=100)
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Title')
plt.show()
```

---

## Key Takeaways (Simple Summary)

1. **Import first:** `import matplotlib.pyplot as plt`
2. **Line plots** — Show trends over time: `plt.plot(x, y)`
3. **Bar charts** — Compare categories: `plt.bar(categories, values)`
4. **Scatter plots** — Show relationships: `plt.scatter(x, y)`
5. **Always label:** xlabel, ylabel, and title!
6. **Show your plot:** `plt.show()` at the end
7. **Data must match:** x and y lists must be the same length

---

## Practice Tips

1. **Start simple** — Get a basic plot working first
2. **Add labels** — Always include xlabel, ylabel, and title
3. **Experiment** — Try different colors, sizes, and styles
4. **Use real data** — Plot things you care about (your scores, expenses, etc.)
5. **Don't give up** — If a plot doesn't show, check you have `plt.show()`

---

## Next Steps

Try the exercises! They're designed to be straightforward. Remember:
- **Always label your axes!**
- **Use `plt.show()` to display your plot**
- **Start simple, then add customization**

You're learning to visualize data — that's a super useful skill! 🎉

Good luck! 🚀

