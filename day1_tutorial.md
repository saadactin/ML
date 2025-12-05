# Day 1: Python Basics I — Variables, Data Types, and Lists

## What is Programming?

**Programming** is the process of writing instructions (code) that a computer can understand and execute. Think of it like giving step-by-step directions to a robot:

- You write code in a **programming language** (like Python)
- The computer reads your code and performs the actions you specified
- Programming allows you to solve problems, automate tasks, and build applications

**Why Python?**
- Easy to read and write (human-friendly syntax)
- Versatile (web development, data science, automation, AI/ML)
- Great for beginners but powerful enough for professionals
- Large community and extensive libraries

---

## 1. Variables — What and Why

### What is a Variable?

A **variable** is a name that refers to a value stored in your computer's memory. Think of it as a labeled box:
- The **label** is the variable name (e.g., `age`, `name`)
- The **box** contains a value (e.g., `25`, `"Saad"`)

### How to Create Variables

In Python, you create variables by **assigning** a value using the `=` sign:

```python
x = 10
name = "Saad"
pi = 3.14159
temperature = 98.6
```

**Key Points:**
- The variable name goes on the left
- The `=` sign means "assign" (not "equals" like in math)
- The value goes on the right
- No need to declare the type beforehand (unlike some other languages)

### Dynamic Typing

Python is **dynamically typed**, meaning:
- You don't need to tell Python what type of data you're storing
- Python figures out the type based on the value you assign
- You can even change the type of a variable later:

```python
x = 10        # x is an integer
x = "hello"   # Now x is a string - this is perfectly fine!
```

### Variable Naming Rules

**Good Practices:**
- Use descriptive names: `count`, `total_price`, `user_name`
- Use `snake_case` for multi-word names: `max_value`, `first_name`
- Start with a letter or underscore (not a number)
- Can contain letters, numbers, and underscores
- Case-sensitive: `age` and `Age` are different variables

**Examples of Good Names:**
```python
student_count = 50
total_sales = 1250.75
is_active = True
user_name = "saad"
```

**Examples of Bad Names:**
```python
# Don't use Python keywords
if = 10        # ❌ 'if' is a keyword
class = "A"    # ❌ 'class' is a keyword

# Don't use built-in function names
list = [1, 2, 3]  # ❌ 'list' is a built-in
str = "hello"     # ❌ 'str' is a built-in

# Avoid unclear names
x = 10           # ❌ What does x represent?
a1 = "test"      # ❌ Not descriptive
```

### Common Mistakes

1. **Confusing `=` (assignment) with `==` (comparison)**
   ```python
   x = 10    # This assigns 10 to x
   x == 10   # This checks if x equals 10 (returns True or False)
   ```

2. **Forgetting quotes for strings**
   ```python
   name = Saad      # ❌ Error! Python thinks Saad is a variable
   name = "Saad"    # ✅ Correct
   ```

3. **Using undefined variables**
   ```python
   print(age)  # ❌ Error if age wasn't defined first
   age = 21
   print(age)  # ✅ Works now
   ```

---

## 2. Basic Data Types

Python has several **data types** (kinds of values). Let's explore the most common ones:

### `int` — Integers

**Integers** are whole numbers (positive, negative, or zero):

```python
age = 21
temperature = -5
count = 0
population = 1000000
```

**Integer Operations:**
```python
a = 10
b = 3

print(a + b)   # 13 (addition)
print(a - b)   # 7  (subtraction)
print(a * b)   # 30 (multiplication)
print(a / b)   # 3.333... (division - returns float)
print(a // b)  # 3  (floor division - returns int)
print(a % b)   # 1  (modulo - remainder)
print(a ** b)  # 1000 (exponentiation - a to the power of b)
```

**Important:** In Python 3, `/` always returns a float, even if the result is a whole number:
```python
print(10 / 2)   # 5.0 (float, not 5)
print(10 // 2)  # 5 (integer)
```

### `float` — Floating Point Numbers

**Floats** are numbers with decimal points:

```python
pi = 3.14159
price = 19.99
temperature = 98.6
negative = -0.5
```

**Float Operations:**
```python
x = 2.5
y = 1.3

print(x + y)   # 3.8
print(x - y)   # 1.2
print(x * y)   # 3.25
print(x / y)   # 1.923076923076923
```

**⚠️ Floating Point Precision Warning:**
Due to how computers represent decimals in binary, floating point arithmetic can have tiny precision errors:
```python
print(0.1 + 0.2)  # 0.30000000000000004 (not exactly 0.3!)
```

This is normal and expected. For exact decimal calculations, Python has a `decimal` module (we'll learn about modules later).

### `str` — Strings

**Strings** are sequences of characters (text). You create them by enclosing text in quotes:

```python
name = "Saad"
greeting = 'Hello'
message = "It's a beautiful day"
```

**Single vs Double Quotes:**
- Both work the same way
- Use double quotes if your string contains a single quote: `"It's great"`
- Use single quotes if your string contains a double quote: `'He said "Hello"'`
- Or use escape characters: `'It\'s great'`

**String Operations:**

**Concatenation** (joining strings):
```python
first = "Hello"
second = "World"
combined = first + " " + second  # "Hello World"
```

**Indexing** (accessing individual characters):
```python
text = "Python"
print(text[0])   # 'P' (first character, index starts at 0)
print(text[1])   # 'y'
print(text[5])   # 'n' (last character)
print(text[-1])  # 'n' (negative index: -1 is last, -2 is second-to-last)
```

**Slicing** (getting a portion of the string):
```python
text = "Python"
print(text[0:3])    # "Pyt" (from index 0 to 2, not including 3)
print(text[1:4])    # "yth"
print(text[:3])     # "Pyt" (from start to index 2)
print(text[3:])     # "hon" (from index 3 to end)
print(text[:])      # "Python" (entire string)
```

**String Methods** (functions that work on strings):
```python
name = "saad"
print(name.upper())      # "SAAD"
print(name.capitalize()) # "Saad"
print(len(name))         # 4 (length of string)

text = "  hello  "
print(text.strip())      # "hello" (removes whitespace)
```

### `bool` — Booleans

**Booleans** represent truth values: only `True` or `False` (note the capital letters):

```python
is_active = True
is_complete = False
```

**Boolean values come from:**
- Direct assignment: `x = True`
- Comparisons: `x > 5`, `name == "Saad"`, `age >= 18`
- Logical operations: `and`, `or`, `not`

**Comparison Operators:**
```python
x = 10
y = 5

print(x == y)   # False (equal to)
print(x != y)   # True  (not equal to)
print(x > y)    # True  (greater than)
print(x < y)    # False (less than)
print(x >= y)   # True  (greater than or equal)
print(x <= y)   # False (less than or equal)
```

**Logical Operators:**
```python
age = 21
has_license = True

print(age >= 18 and has_license)  # True (both must be True)
print(age < 18 or has_license)    # True (at least one True)
print(not has_license)             # False (opposite)
```

### Checking Types

Use the `type()` function to check what type a value is:

```python
print(type(10))        # <class 'int'>
print(type(3.14))     # <class 'float'>
print(type("hello"))  # <class 'str'>
print(type(True))     # <class 'bool'>

# You can also check if a variable is a specific type
x = 10
print(type(x) == int)  # True
```

---

## 3. Lists — Ordered Collections

### What is a List?

A **list** is an ordered collection of items. Think of it like a shopping list or a row of boxes:
- Items are stored in a specific order
- You can access items by their position (index)
- Lists can contain different types of data @@@
- Lists are **mutable** (you can change them after creation)

### Creating Lists

```python
# List of numbers
numbers = [1, 2, 3, 4, 5]

# List of strings
fruits = ["apple", "banana", "orange"]

# Mixed types (allowed in Python!)
mixed = [1, "two", 3.0, True]

# Empty list
empty = []
```

### Accessing List Items

**Indexing** (getting a single item):
```python
fruits = ["apple", "banana", "orange"]

print(fruits[0])   # "apple" (first item, index starts at 0)
print(fruits[1])   # "banana"
print(fruits[2])   # "orange"
print(fruits[-1])  # "orange" (last item, using negative index)
print(fruits[-2])  # "banana" (second-to-last)
```

**Slicing** (getting multiple items):
```python
numbers = [10, 20, 30, 40, 50]

print(numbers[1:3])   # [20, 30] (from index 1 to 2, not including 3)
print(numbers[:3])    # [10, 20, 30] (from start to index 2)
print(numbers[2:])    # [30, 40, 50] (from index 2 to end)
print(numbers[:])     # [10, 20, 30, 40, 50] (entire list)
```

### Modifying Lists

**Changing an item:**
```python
fruits = ["apple", "banana", "orange"]
fruits[1] = "grape"  # Change "banana" to "grape"
print(fruits)        # ["apple", "grape", "orange"]
```

**Adding items:**

1. **`append()`** - adds to the end:
```python
fruits = ["apple", "banana"]
fruits.append("orange")
print(fruits)  # ["apple", "banana", "orange"]
```

2. **`insert()`** - adds at a specific position:
```python
fruits = ["apple", "banana"]
fruits.insert(1, "grape")  # Insert "grape" at index 1
print(fruits)  # ["apple", "grape", "banana"]
```

3. **`extend()`** - adds multiple items:
```python
fruits = ["apple", "banana"]
fruits.extend(["orange", "grape"])
print(fruits)  # ["apple", "banana", "orange", "grape"]
```

**Removing items:**

1. **`remove()`** - removes by value (first occurrence):
```python
fruits = ["apple", "banana", "apple"]
fruits.remove("apple")  # Removes first "apple"
print(fruits)  # ["banana", "apple"]
```

2. **`pop()`** - removes and returns an item by index:
```python
fruits = ["apple", "banana", "orange"]
last = fruits.pop()      # Removes and returns "orange"
print(fruits)            # ["apple", "banana"]
print(last)              # "orange"

first = fruits.pop(0)    # Removes and returns "apple"
print(fruits)            # ["banana"]
```

3. **`del`** - deletes by index:
```python
fruits = ["apple", "banana", "orange"]
del fruits[1]  # Removes "banana"
print(fruits)   # ["apple", "orange"]
```

### Useful List Operations

**Length:**
```python
fruits = ["apple", "banana", "orange"]
print(len(fruits))  # 3
```

**Checking if item exists:**
```python
fruits = ["apple", "banana", "orange"]
print("apple" in fruits)   # True
print("grape" in fruits)   # False
```

**Finding index:**
```python
fruits = ["apple", "banana", "orange"]
print(fruits.index("banana"))  # 1
```

**Counting occurrences:**
```python
numbers = [1, 2, 2, 3, 2, 4]
print(numbers.count(2))  # 3
```

**Sorting:**
```python
numbers = [3, 1, 4, 1, 5]
numbers.sort()           # Sorts in place
print(numbers)           # [1, 1, 3, 4, 5]

# Or create a new sorted list
numbers = [3, 1, 4, 1, 5]
sorted_numbers = sorted(numbers)
print(sorted_numbers)    # [1, 1, 3, 4, 5]
print(numbers)           # [3, 1, 4, 1, 5] (original unchanged)
```

### List Comprehension (Advanced but Useful!)

**List comprehension** is a concise way to create lists:

**Traditional way:**
```python
squares = []
for x in range(1, 6):
    squares.append(x * x)
print(squares)  # [1, 4, 9, 16, 25]
```

**List comprehension way:**
```python
squares = [x * x for x in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]
```

**More examples:**
```python
# Even numbers
evens = [x for x in range(1, 11) if x % 2 == 0]
print(evens)  # [2, 4, 6, 8, 10]

# Uppercase strings
words = ["hello", "world"]
upper_words = [word.upper() for word in words]
print(upper_words)  # ["HELLO", "WORLD"]
```

### Mutable vs Immutable

**Lists are mutable** (can be changed):
```python
my_list = [1, 2, 3]
my_list[0] = 10  # ✅ Allowed
print(my_list)   # [10, 2, 3]
```

**Strings are immutable** (cannot be changed):
```python
my_string = "hello"
# my_string[0] = "H"  # ❌ Error! Can't change strings this way

# Instead, create a new string
my_string = "H" + my_string[1:]  # ✅ Creates new string
print(my_string)  # "Hello"
```

### Common Pitfalls

**1. Copying Lists:**
```python
# ❌ WRONG - This creates two names for the same list
list1 = [1, 2, 3]
list2 = list1
list2.append(4)
print(list1)  # [1, 2, 3, 4] - list1 also changed!

# ✅ CORRECT - Create a copy
list1 = [1, 2, 3]
list2 = list1.copy()  # or list2 = list1[:]
list2.append(4)
print(list1)  # [1, 2, 3] - list1 unchanged
print(list2)  # [1, 2, 3, 4]
```

**2. Index Out of Range:**
```python
fruits = ["apple", "banana"]
# print(fruits[5])  # ❌ Error! Index 5 doesn't exist
print(fruits[0])    # ✅ "apple"
print(fruits[-1])   # ✅ "banana" (safe way to get last item)
```

**3. Empty List Operations:**
```python
empty = []
# print(empty[0])     # ❌ Error! List is empty
# print(empty.pop())  # ❌ Error! Nothing to pop
print(len(empty))    # ✅ 0
```

---

## Putting It All Together

Here's a complete example using everything we've learned:

```python
# Variables with different types
name = "Saad"
age = 21
height = 5.9
is_student = True

# Lists
favorite_fruits = ["apple", "banana", "orange"]
grades = [85, 92, 78, 96]

# Operations
print(f"Name: {name}, Age: {age}")
print(f"Number of favorite fruits: {len(favorite_fruits)}")
print(f"First fruit: {favorite_fruits[0]}")
print(f"Average grade: {sum(grades) / len(grades)}")

# Modifying lists
favorite_fruits.append("grape")
grades.sort()
print(f"Sorted grades: {grades}")
print(f"Updated fruits: {favorite_fruits}")
```

---

## Key Takeaways

1. **Variables** are names that store values
2. **Data types** include: `int`, `float`, `str`, `bool`
3. **Lists** are ordered, mutable collections
4. Python is **dynamically typed** (no type declarations needed)
5. **Indexing starts at 0** (first item is at index 0)
6. Lists are **mutable**, strings are **immutable**
7. Always **copy lists** if you don't want to modify the original

---

## Next Steps

Practice with the exercises file! The best way to learn programming is by doing. Try to solve each problem yourself before looking at the solutions.

Good luck! 🚀

