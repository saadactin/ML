# Day 6: Matplotlib Exercises — Basic Plots and Charts

**Estimated Time: 25 minutes**

**Instructions:**
- Read each question carefully
- Try to solve it yourself before checking the solution
- Type out the code (don't just read it) — this helps you remember
- **Always include labels** (xlabel, ylabel, title) in your plots!
- Don't forget `plt.show()` at the end
- Check the solutions in `day6_solution.md` only after you've attempted the problem
- Remember: `import matplotlib.pyplot as plt` at the start!

---

## Exercise 1: Line Plots (8 minutes)

### Question 1.1
Create a simple line plot with:
- X values: `[1, 2, 3, 4, 5]`
- Y values: `[2, 4, 6, 8, 10]`
- Add labels: x-axis = "X Values", y-axis = "Y Values", title = "Simple Line Plot"

<details>
<summary>Hint</summary>
Use `plt.plot(x, y)`, then add `plt.xlabel()`, `plt.ylabel()`, and `plt.title()`. Don't forget `plt.show()`!
</details>

---

### Question 1.2
Create a line plot showing temperature over 5 days:
- Days: `[1, 2, 3, 4, 5]`
- Temperature: `[72, 75, 73, 78, 80]`
- Add markers (dots) at each point
- Add proper labels and title

<details>
<summary>Hint</summary>
Use `plt.plot()` with `marker='o'` parameter. Add all three labels!
</details>

---

### Question 1.3
Create a line plot with two lines on the same plot:
- Days: `[1, 2, 3, 4, 5]`
- City A temperatures: `[72, 75, 73, 78, 80]`
- City B temperatures: `[68, 70, 69, 72, 74]`
- Add labels for each line using `label='City A'` and `label='City B'`
- Add `plt.legend()` to show which line is which
- Add proper axis labels and title

<details>
<summary>Hint</summary>
Call `plt.plot()` twice - once for each city. Use `label=` parameter and `plt.legend()`.
</details>

---

## Exercise 2: Bar Charts (8 minutes)

### Question 2.1
Create a bar chart showing sales by month:
- Months: `['Jan', 'Feb', 'Mar', 'Apr', 'May']`
- Sales: `[100, 150, 120, 180, 200]`
- Add proper labels and title

<details>
<summary>Hint</summary>
Use `plt.bar(months, sales)`. Don't forget the labels!
</details>

---

### Question 2.2
Create a bar chart showing test scores by subject:
- Subjects: `['Math', 'Science', 'English', 'History']`
- Scores: `[85, 92, 78, 88]`
- Make the bars green
- Add proper labels and title

<details>
<summary>Hint</summary>
Use `plt.bar()` with `color='green'` parameter.
</details>

---

### Question 2.3
Create a horizontal bar chart showing the same test scores from Question 2.2:
- Use `plt.barh()` instead of `plt.bar()`
- Add proper labels (note: x and y labels might swap!)

<details>
<summary>Hint</summary>
Use `plt.barh(subjects, scores)`. For horizontal bars, xlabel is the vertical axis and ylabel is the horizontal axis.
</details>

---

## Exercise 3: Scatter Plots (9 minutes)

### Question 3.1
Create a scatter plot showing the relationship between hours studied and test scores:
- Hours: `[1, 2, 3, 4, 5, 6, 7, 8]`
- Scores: `[50, 60, 65, 70, 75, 80, 85, 90]`
- Add proper labels and title

<details>
<summary>Hint</summary>
Use `plt.scatter(hours, scores)`. Always add labels!
</details>

---

### Question 3.2
Create a scatter plot with the same data as Question 3.1, but:
- Make the points red
- Make the points bigger (use `s=100`)
- Add transparency (use `alpha=0.6`)
- Add proper labels and title

<details>
<summary>Hint</summary>
Use `plt.scatter()` with `color='red'`, `s=100`, and `alpha=0.6` parameters.
</details>

---

### Question 3.3
Create a scatter plot comparing two groups:
- Group A: hours = `[1, 2, 3, 4, 5]`, scores = `[50, 60, 65, 70, 75]`
- Group B: hours = `[2, 3, 4, 5, 6]`, scores = `[55, 65, 70, 80, 85]`
- Use different colors for each group (e.g., blue for Group A, red for Group B)
- Add labels using `label='Group A'` and `label='Group B'`
- Add `plt.legend()` to show which group is which
- Add proper axis labels and title

<details>
<summary>Hint</summary>
Call `plt.scatter()` twice - once for each group. Use different colors and labels.
</details>

---

## Final Check

Before moving on, make sure you can:
- ✅ Create a line plot with `plt.plot()`
- ✅ Create a bar chart with `plt.bar()`
- ✅ Create a scatter plot with `plt.scatter()`
- ✅ Add xlabel, ylabel, and title to every plot
- ✅ Use `plt.show()` to display plots
- ✅ Add legends when showing multiple groups/lines

---

## Tips for Success

1. **Always import first:** `import matplotlib.pyplot as plt`

2. **Always label:** Every plot needs xlabel, ylabel, and title

3. **Always show:** Don't forget `plt.show()` at the end

4. **Check your data:** Make sure x and y lists are the same length

5. **Experiment:** Try different colors, sizes, and styles

6. **If plot doesn't show:** Check that you have `plt.show()`

---

**Great job working through these exercises! 🎉**

Remember: Visualization is a powerful skill. Being able to create clear, labeled plots will help you understand and share data better!

