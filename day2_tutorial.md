# Day 2: Python Basics II — Conditionals and Loops

## Introduction

Today we'll learn how to make your programs **decide** and **repeat**. These are fundamental concepts that make programs dynamic and powerful:

- **Conditionals** (`if`, `elif`, `else`) — Let your program make decisions
- **Loops** (`for`, `while`) — Let your program repeat actions

These concepts are used in almost every program you'll write!

---

## 1. Conditionals — Making Decisions

### What are Conditionals?

**Conditionals** allow your program to execute different code based on whether a condition is `True` or `False`. Think of it like a fork in the road: "If this is true, go left; otherwise, go right."

### The `if` Statement

The simplest conditional checks if a condition is `True` and executes code if it is:

```python
age = 20

if age >= 18:
    print("You are an adult!")
```

**Key Points:**
- The condition after `if` must evaluate to `True` or `False`
- The code block after `if` is indented (usually 4 spaces)
- The colon `:` at the end of the `if` line is required

**Example:**
```python
temperature = 25

if temperature > 30:
    print("It's hot outside!")
    print("Stay hydrated!")
```

### The `else` Statement

`else` provides an alternative path when the `if` condition is `False`:

```python
age = 15

if age >= 18:
    print("You are an adult!")
else:
    print("You are a minor!")
```

**Example:**
```python
password = "secret123"

if password == "secret123":
    print("Access granted!")
else:
    print("Access denied!")
```

### The `elif` Statement

`elif` (short for "else if") allows you to check multiple conditions in sequence:

```python
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
```

**Important:** Python checks conditions from top to bottom and executes the **first** condition that is `True`, then skips the rest.

### Multiple Conditions

You can combine conditions using `and`, `or`, and `not`:

```python
age = 25
has_license = True

if age >= 18 and has_license:
    print("You can drive!")
else:
    print("You cannot drive!")

# Using 'or'
if age < 13 or age > 65:
    print("You get a discount!")
else:
    print("Regular price")

# Using 'not'
is_weekend = False
if not is_weekend:
    print("It's a weekday!")
```

### Nested Conditionals

You can put `if` statements inside other `if` statements:

```python
age = 25
has_license = True

if age >= 18:
    if has_license:
        print("You can drive!")
    else:
        print("You need a license!")
else:
    print("You're too young to drive!")
```

### Common Comparison Operators

```python
x = 10
y = 5

x == y   # Equal to (False)
x != y   # Not equal to (True)
x > y    # Greater than (True)
x < y    # Less than (False)
x >= y   # Greater than or equal (True)
x <= y   # Less than or equal (False)
```

### Truthiness in Python

In Python, many values are considered "truthy" or "falsy":

**Falsy values:**
- `False`
- `None`
- `0` (zero)
- `""` (empty string)
- `[]` (empty list)
- `{}` (empty dictionary)

**Truthy values:**
- Everything else (non-zero numbers, non-empty strings, non-empty lists, etc.)

```python
name = "Saad"

if name:  # This is True because name is not empty
    print(f"Hello, {name}!")

# This is equivalent to:
if name != "":
    print(f"Hello, {name}!")
```

### Common Mistakes

1. **Forgetting the colon `:`**
   ```python
   # ❌ WRONG
   if age >= 18
       print("Adult")
   
   # ✅ CORRECT
   if age >= 18:
       print("Adult")
   ```

2. **Wrong indentation**
   ```python
   # ❌ WRONG
   if age >= 18:
   print("Adult")  # Not indented!
   
   # ✅ CORRECT
   if age >= 18:
       print("Adult")  # Properly indented
   ```

3. **Using `=` instead of `==`**
   ```python
   # ❌ WRONG
   if age = 18:  # This is assignment, not comparison!
   
   # ✅ CORRECT
   if age == 18:  # This is comparison
   ```

4. **Missing `elif` logic**
   ```python
   # ❌ WRONG - All conditions are checked
   if score >= 90:
       print("A")
   if score >= 80:  # This will also run if score is 95!
       print("B")
   
   # ✅ CORRECT - Only first matching condition runs
   if score >= 90:
       print("A")
   elif score >= 80:
       print("B")
   ```

---

## 2. For Loops — Repeating with a Known Count

### What are For Loops?

A **for loop** repeats a block of code a specific number of times or iterates over a collection of items. It's perfect when you know how many times you want to repeat something.

### Basic For Loop Syntax

```python
for variable in sequence:
    # code to repeat
```

### Looping Through a List

The most common use is to iterate through each item in a list:

```python
fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print(fruit)

# Output:
# apple
# banana
# orange
```

**What happens:**
1. `fruit` takes the value of the first item: `"apple"`
2. The code block executes (prints "apple")
3. `fruit` takes the value of the next item: `"banana"`
4. The code block executes (prints "banana")
5. This continues until all items are processed

### Using `range()`

The `range()` function generates a sequence of numbers, perfect for repeating code a specific number of times:

```python
# range(stop) - from 0 to stop-1
for i in range(5):
    print(i)

# Output:
# 0
# 1
# 2
# 3
# 4
```

```python
# range(start, stop) - from start to stop-1
for i in range(2, 6):
    print(i)

# Output:
# 2
# 3
# 4
# 5
```

```python
# range(start, stop, step) - with step size
for i in range(0, 10, 2):
    print(i)

# Output:
# 0
# 2
# 4
# 6
# 8
```

**Common patterns:**
```python
# Count from 1 to 10
for i in range(1, 11):
    print(i)

# Count backwards
for i in range(10, 0, -1):
    print(i)

# Even numbers
for i in range(0, 11, 2):
    print(i)
```

### Looping with Index

Sometimes you need both the index and the value:

```python
fruits = ["apple", "banana", "orange"]

# Method 1: Using range and len
for i in range(len(fruits)):
    print(f"Index {i}: {fruits[i]}")

# Output:
# Index 0: apple
# Index 1: banana
# Index 2: orange

# Method 2: Using enumerate() (more Pythonic)
for i, fruit in enumerate(fruits):
    print(f"Index {i}: {fruit}")
```

### Nested For Loops

You can put loops inside other loops:

```python
# Multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")
    print()  # Empty line after each row

# Output:
# 1 x 1 = 1
# 1 x 2 = 2
# 1 x 3 = 3
#
# 2 x 1 = 2
# 2 x 2 = 4
# 2 x 3 = 6
#
# 3 x 1 = 3
# 3 x 2 = 6
# 3 x 3 = 9
```

### Loop Control: `break` and `continue`

**`break`** — Exits the loop immediately:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    if num == 5:
        break  # Exit loop when we find 5
    print(num)

# Output:
# 1
# 2
# 3
# 4
```

**`continue`** — Skips the rest of the current iteration and continues with the next:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    if num % 2 == 0:  # Skip even numbers
        continue
    print(num)

# Output:
# 1
# 3
# 5
# 7
# 9
```

### The `else` Clause with For Loops

A `for` loop can have an `else` clause that runs if the loop completes normally (without `break`):

```python
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num == 10:
        print("Found 10!")
        break
else:
    print("10 not found in the list")
```

---

## 3. While Loops — Repeating Until a Condition Changes

### What are While Loops?

A **while loop** repeats a block of code as long as a condition is `True`. It's perfect when you don't know how many times you need to repeat something.

### Basic While Loop Syntax

```python
while condition:
    # code to repeat
    # Make sure to eventually make condition False!
```

### Simple While Loop

```python
count = 0

while count < 5:
    print(f"Count: {count}")
    count = count + 1  # or count += 1

# Output:
# Count: 0
# Count: 1
# Count: 2
# Count: 3
# Count: 4
```

### Common While Loop Patterns

**1. Counter pattern:**
```python
i = 0
while i < 10:
    print(i)
    i += 1
```

**2. User input validation:**
```python
password = ""

while password != "secret":
    password = input("Enter password: ")
    if password != "secret":
        print("Wrong password! Try again.")

print("Access granted!")
```

**3. Processing until a condition:**
```python
numbers = [1, 2, 3, 4, 5]
index = 0

while index < len(numbers):
    print(numbers[index])
    index += 1
```

### Infinite Loops and How to Break Them

**⚠️ WARNING:** If the condition never becomes `False`, you get an infinite loop:

```python
# ❌ DANGEROUS - This runs forever!
# count = 0
# while count < 5:
#     print(count)
#     # Forgot to increment count!

# ✅ CORRECT
count = 0
while count < 5:
    print(count)
    count += 1  # Always update the condition variable!
```

**Breaking out of loops:**
```python
while True:  # Infinite loop
    user_input = input("Enter 'quit' to exit: ")
    if user_input == "quit":
        break  # Exit the loop
    print(f"You entered: {user_input}")
```

### `break` and `continue` in While Loops

They work the same as in `for` loops:

```python
count = 0
while count < 10:
    count += 1
    if count == 5:
        break  # Exit loop
    if count % 2 == 0:
        continue  # Skip even numbers
    print(count)

# Output:
# 1
# 3
```

### For vs While: When to Use Which?

**Use `for` when:**
- You know how many times to repeat
- You're iterating over a collection (list, string, etc.)
- You have a specific sequence to follow

**Use `while` when:**
- You don't know how many times to repeat
- You're waiting for a condition to change
- You need to repeat until something happens

**Example comparison:**
```python
# Using for (better for this case)
for i in range(1, 11):
    print(i)

# Using while (works but more verbose)
i = 1
while i <= 10:
    print(i)
    i += 1
```

---

## 4. Combining Conditionals and Loops

### Conditionals Inside Loops

You can use `if` statements inside loops to make decisions during each iteration:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
```

### Loops Inside Conditionals

You can also put loops inside `if` statements:

```python
user_choice = "yes"

if user_choice == "yes":
    for i in range(5):
        print(f"Printing {i}")
else:
    print("Not printing anything")
```

### Complex Example

```python
# Find all even numbers and their squares
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = []

for num in numbers:
    if num % 2 == 0:  # Check if even
        square = num * num
        even_squares.append(square)
        print(f"{num} is even, its square is {square}")

print(f"All even squares: {even_squares}")
```

---

## 5. Common Patterns and Examples

### Pattern 1: Finding Items

```python
# Find the first number greater than 5
numbers = [1, 3, 7, 2, 9, 4]

for num in numbers:
    if num > 5:
        print(f"Found: {num}")
        break
```

### Pattern 2: Counting Items

```python
# Count how many even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
count = 0

for num in numbers:
    if num % 2 == 0:
        count += 1

print(f"Number of even numbers: {count}")
```

### Pattern 3: Accumulating Values

```python
# Sum all numbers
numbers = [1, 2, 3, 4, 5]
total = 0

for num in numbers:
    total += num

print(f"Sum: {total}")  # 15
```

### Pattern 4: Filtering

```python
# Create a list of only positive numbers
numbers = [-2, 5, -1, 8, -3, 10]
positive = []

for num in numbers:
    if num > 0:
        positive.append(num)

print(positive)  # [5, 8, 10]
```

### Pattern 5: Searching

```python
# Check if a value exists
fruits = ["apple", "banana", "orange"]
search = "banana"
found = False

for fruit in fruits:
    if fruit == search:
        found = True
        break

if found:
    print(f"{search} is in the list!")
else:
    print(f"{search} is not in the list!")
```

---

## 6. Common Pitfalls and Best Practices

### Common Mistakes

1. **Infinite loops**
   ```python
   # ❌ WRONG
   # while True:
   #     print("Forever!")
   
   # ✅ CORRECT - Always have an exit condition
   count = 0
   while count < 5:
       print(count)
       count += 1
   ```

2. **Modifying list while iterating**
   ```python
   # ❌ WRONG - Can cause unexpected behavior
   # numbers = [1, 2, 3, 4, 5]
   # for num in numbers:
   #     if num == 3:
   #         numbers.remove(num)
   
   # ✅ CORRECT - Create a copy or use list comprehension
   numbers = [1, 2, 3, 4, 5]
   numbers = [num for num in numbers if num != 3]
   ```

3. **Off-by-one errors**
   ```python
   # ❌ WRONG - range(5) gives 0-4, not 1-5
   # for i in range(5):
   #     print(i)  # Prints 0, 1, 2, 3, 4
   
   # ✅ CORRECT
   for i in range(1, 6):  # Prints 1, 2, 3, 4, 5
       print(i)
   ```

4. **Forgetting to initialize variables**
   ```python
   # ❌ WRONG
   # total = ???  # Not defined!
   # for num in [1, 2, 3]:
   #     total += num
   
   # ✅ CORRECT
   total = 0  # Initialize before loop
   for num in [1, 2, 3]:
       total += num
   ```

### Best Practices

1. **Use descriptive variable names**
   ```python
   # ❌ Bad
   for i in lst:
       if i > 5:
           print(i)
   
   # ✅ Good
   for number in numbers:
       if number > 5:
           print(number)
   ```

2. **Keep loops simple**
   ```python
   # ✅ Good - Clear and readable
   even_numbers = []
   for num in numbers:
       if num % 2 == 0:
           even_numbers.append(num)
   ```

3. **Use `for` when possible**
   ```python
   # ✅ Prefer for loops when iterating over collections
   for item in my_list:
       print(item)
   
   # Use while when you need conditional repetition
   while user_input != "quit":
       user_input = input("Enter command: ")
   ```

---

## Putting It All Together

Here's a complete example using everything we've learned:

```python
# Grade calculator with multiple students
students = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

# Process each student
for i in range(len(students)):
    student = students[i]
    score = scores[i]
    
    # Determine grade
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    
    # Print result
    print(f"{student}: {score} -> Grade {grade}")

# Calculate average
total = 0
for score in scores:
    total += score
average = total / len(scores)

print(f"\nAverage score: {average:.2f}")
```

---

## Key Takeaways

1. **Conditionals** (`if`, `elif`, `else`) let programs make decisions
2. **For loops** repeat code a known number of times or iterate over collections
3. **While loops** repeat code until a condition becomes `False`
4. **`break`** exits a loop immediately
5. **`continue`** skips to the next iteration
6. Always ensure loops have an exit condition to avoid infinite loops
7. Use `for` for collections, `while` for conditional repetition
8. Combine conditionals and loops to create powerful programs

---

## Next Steps

Practice with the exercises file! Try to solve each problem yourself before checking the solutions. The more you practice, the more natural these concepts will become.

Good luck! 🚀

