# Day 1: Python Exercises — Variables, Data Types, and Lists

**Estimated Time: 30 minutes**

**Instructions:**
- Read each question carefully
- Try to solve it yourself before checking the solution
- Type out the code (don't just read it) — muscle memory helps!
- If you get stuck, read the hint, then try again
- Check the solutions in `day1_solution.md` only after you've attempted the problem

---

## Exercise 1: Variables and Basic Types (5 minutes)

### Question 1.1
Create three variables:
- `my_name` storing your name as a string
- `my_age` storing your age as an integer
- `my_height` storing your height in meters as a float

Then print them in a sentence like: "My name is [name], I am [age] years old, and I am [height] meters tall."

<details>
<summary>Hint</summary>
Use the print() function with string concatenation or f-strings.
</details>

---

### Question 1.2
Create two integer variables `a = 15` and `b = 4`. Calculate and print:
- The sum of a and b
- The difference (a - b)
- The product (a * b)
- The quotient (a / b)
- The floor division (a // b)
- The remainder (a % b)

<details>
<summary>Hint</summary>
Use the arithmetic operators: +, -, *, /, //, %
</details>

---

### Question 1.3
Create a string variable `text = "Python Programming"`. Print:
- The first character
- The last character
- The substring from index 0 to 6 (exclusive)
- The substring from index 7 to the end
- The length of the string

<details>
<summary>Hint</summary>
Use indexing [0], [-1], slicing [0:6], [7:], and len()
</details>

---

## Exercise 2: Boolean Logic (5 minutes)

### Question 2.1
Create variables `age = 20` and `has_license = True`. Write expressions to check and print:
- Is the person 18 or older?
- Does the person have a license?
- Can the person drive? (must be 18+ AND have a license)
- Is the person either under 18 OR doesn't have a license?

<details>
<summary>Hint</summary>
Use comparison operators (>=) and logical operators (and, or)
</details>

---

### Question 2.2
Create three boolean variables: `is_raining = True`, `has_umbrella = False`, `is_indoor = True`. Determine and print:
- Should I go outside? (not raining OR has umbrella OR is indoor)
- Will I get wet? (raining AND not has_umbrella AND not is_indoor)

<details>
<summary>Hint</summary>
Use logical operators: and, or, not
</details>

---

## Exercise 3: Lists Basics (10 minutes)

### Question 3.1
Create a list called `fruits` with: "apple", "banana", "orange", "grape", "mango"
- Print the entire list
- Print the first fruit
- Print the last fruit (using negative index)
- Print fruits from index 1 to 3 (inclusive of 1, exclusive of 3)
- Print the number of fruits

<details>
<summary>Hint</summary>
Use list indexing [0], [-1], slicing [1:3], and len()
</details>

---

### Question 3.2
Start with an empty list called `shopping_list`. Then:
- Add "milk" to the list
- Add "bread" to the list
- Add "eggs" at the beginning (index 0)
- Add "cheese" at index 2
- Remove "bread" from the list
- Print the final list

<details>
<summary>Hint</summary>
Use append(), insert(), and remove() methods
</details>

---

### Question 3.3
Create a list `numbers = [5, 2, 8, 1, 9, 3]`. Then:
- Sort the list in ascending order
- Find the largest number (hint: after sorting, it's the last item)
- Find the smallest number (first item after sorting)
- Calculate the sum of all numbers
- Calculate the average

<details>
<summary>Hint</summary>
Use sort(), indexing, and sum() function
</details>

---

### Question 3.4
Create a list `mixed = [10, "hello", 3.14, True, "world"]`. Write code to:
- Print each item and its type
- Count how many strings are in the list
- Create a new list containing only the strings from `mixed`

<details>
<summary>Hint</summary>
Use type() to check types, isinstance(item, str) or type(item) == str, and a loop or list comprehension
</details>

---

## Exercise 4: List Operations (10 minutes)

### Question 4.1
Create two lists: `list1 = [1, 2, 3]` and `list2 = [4, 5, 6]`.
- Create `list3` that combines both lists (all items from list1 and list2)
- Create `list4` as a copy of `list1`
- Modify `list4` by adding 10 to it
- Verify that `list1` was not changed

<details>
<summary>Hint</summary>
Use + to combine lists, .copy() or [:] to copy, and append() to modify
</details>

---

### Question 4.2
Create a list `scores = [85, 92, 78, 96, 88, 91, 75]`. Write code to:
- Find the highest score
- Find the lowest score
- Calculate the average score
- Count how many scores are above 85
- Create a new list with only scores above 85

<details>
<summary>Hint</summary>
Use max(), min(), sum(), len(), and a loop or list comprehension with condition
</details>

---

### Question 4.3
Create a list `words = ["python", "java", "javascript", "c++", "python", "java"]`. Write code to:
- Count how many times "python" appears
- Find the index of the first occurrence of "java"
- Remove all duplicates (create a new list with unique values only)
- Sort the unique list alphabetically

<details>
<summary>Hint</summary>
Use count(), index(), and think about how to get unique values (you can use a loop to check if item already exists, or convert to set and back - but we haven't learned sets yet, so use a loop)
</details>

---

## Exercise 5: Challenge Problems (Optional - if you have time)

### Question 5.1
Create a list of numbers from 1 to 10. Using list comprehension, create:
- A list of squares: [1, 4, 9, 16, ...]
- A list of even numbers: [2, 4, 6, 8, 10]
- A list of numbers divisible by 3: [3, 6, 9]

<details>
<summary>Hint</summary>
List comprehension syntax: [expression for item in iterable if condition]
</details>

---

### Question 5.2
You have a list of student names: `students = ["Alice", "Bob", "Charlie", "David", "Eve"]` and their corresponding scores: `scores = [85, 92, 78, 96, 88]`.

Write code to:
- Find the student with the highest score
- Find the student with the lowest score
- Print each student's name with their score in the format: "Alice: 85"

<details>
<summary>Hint</summary>
Use index() to find the position of max/min score, then use that index to get the student name
</details>

---

## Final Check

Before moving on, make sure you can:
- ✅ Create and use variables of different types
- ✅ Perform arithmetic operations
- ✅ Work with strings (indexing, slicing)
- ✅ Use boolean logic and comparisons
- ✅ Create and modify lists
- ✅ Access list elements by index
- ✅ Use common list methods (append, remove, sort, etc.)
- ✅ Understand the difference between mutable and immutable types

---

## Tips for Learning

1. **Type the code yourself** - Don't just copy-paste. Typing helps you remember.

2. **Experiment** - Try changing values, adding print statements, breaking things to see what happens.

3. **Read error messages** - They tell you exactly what went wrong and where.

4. **Practice daily** - Even 15-20 minutes of practice is better than long sessions once a week.

5. **Build something** - After completing exercises, try to create a small program using what you learned (e.g., a simple shopping list manager).

---

**Great job completing Day 1! 🎉**

You've learned the fundamentals of Python. Tomorrow we'll cover control flow (if statements, loops) to make your programs more dynamic and powerful!
