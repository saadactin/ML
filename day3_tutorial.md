# Day 3: Python Basics III — Functions and Dictionaries

## Introduction

Today we'll learn two powerful concepts that will make your code more organized and efficient:

- **Functions** — Reusable blocks of code that perform specific tasks
- **Dictionaries** — Key-value pairs for storing and organizing data

These concepts are essential for writing clean, maintainable, and efficient Python programs!

---

## 1. Functions — Reusable Code Blocks

### What are Functions?

A **function** is a named block of code that performs a specific task. Think of it as a recipe: you define it once, then you can use it whenever you need it.

**Why use functions?**
- **Reusability** — Write once, use many times
- **Organization** — Break complex problems into smaller pieces
- **Maintainability** — Fix bugs in one place
- **Readability** — Code becomes more understandable

### Defining a Function

The basic syntax for defining a function:

```python
def function_name():
    # code to execute
    pass
```

**Example:**
```python
def greet():
    print("Hello, World!")

# To use (call) the function:
greet()  # Output: Hello, World!
```

### Functions with Parameters

**Parameters** are variables that receive values when the function is called:

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Saad")    # Output: Hello, Saad!
greet("Alice")   # Output: Hello, Alice!
```

**Multiple parameters:**
```python
def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")

introduce("Saad", 21)  # Output: My name is Saad and I am 21 years old.
```

### Return Values

Functions can **return** values using the `return` statement:

```python
def add(a, b):
    result = a + b
    return result

sum_result = add(5, 3)
print(sum_result)  # Output: 8

# You can also return directly:
def multiply(x, y):
    return x * y

product = multiply(4, 7)
print(product)  # Output: 28
```

**Important:** Once a function hits a `return` statement, it immediately exits:

```python
def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    return "Zero"  # This only runs if num is 0

print(check_number(5))   # Output: Positive
print(check_number(-3))  # Output: Negative
print(check_number(0))   # Output: Zero
```

### Functions Without Return

If a function doesn't have a `return` statement, it returns `None`:

```python
def print_message(msg):
    print(msg)

result = print_message("Hello")
print(result)  # Output: None (because nothing was returned)
```

### Default Parameters

You can provide default values for parameters:

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Saad")              # Output: Hello, Saad!
greet("Saad", "Hi")        # Output: Hi, Saad!
greet("Alice", "Goodbye")  # Output: Goodbye, Alice!
```

**Important:** Parameters with defaults must come after parameters without defaults:

```python
# ✅ CORRECT
def func(a, b=10):
    return a + b

# ❌ WRONG
# def func(a=10, b):  # Syntax error!
#     return a + b
```

### Keyword Arguments

You can call functions using parameter names (keywords):

```python
def create_profile(name, age, city):
    print(f"Name: {name}, Age: {age}, City: {city}")

# Positional arguments (order matters)
create_profile("Saad", 21, "New York")

# Keyword arguments (order doesn't matter)
create_profile(age=21, city="New York", name="Saad")
create_profile("Saad", city="New York", age=21)  # Mix is OK
```

### Variable Scope

**Scope** determines where variables can be accessed:

**Local scope** — Variables inside a function:
```python
def my_function():
    local_var = 10  # Local variable
    print(local_var)

my_function()
# print(local_var)  # ❌ Error! local_var doesn't exist outside function
```

**Global scope** — Variables outside functions:
```python
global_var = 20  # Global variable

def my_function():
    print(global_var)  # ✅ Can access global variables

my_function()  # Output: 20
```

**Modifying global variables:**
```python
count = 0

def increment():
    global count  # Need to declare 'global' to modify
    count += 1

increment()
print(count)  # Output: 1
```

**Best practice:** Avoid using global variables when possible. Pass values as parameters instead.

### Multiple Return Values

Functions can return multiple values (as a tuple):

```python
def get_name_and_age():
    name = "Saad"
    age = 21
    return name, age  # Returns a tuple

result = get_name_and_age()
print(result)  # Output: ('Saad', 21)

# Unpack the tuple
name, age = get_name_and_age()
print(f"Name: {name}, Age: {age}")  # Output: Name: Saad, Age: 21
```

### Docstrings

**Docstrings** document what a function does:

```python
def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Parameters:
    length (float): The length of the rectangle
    width (float): The width of the rectangle
    
    Returns:
    float: The area of the rectangle
    """
    return length * width

# Access the docstring
print(calculate_area.__doc__)
```

### Common Function Patterns

**1. Validation function:**
```python
def is_even(num):
    return num % 2 == 0

print(is_even(4))   # True
print(is_even(5))   # False
```

**2. Calculation function:**
```python
def calculate_total(prices):
    total = 0
    for price in prices:
        total += price
    return total

prices = [10, 20, 30]
print(calculate_total(prices))  # 60
```

**3. Transformation function:**
```python
def capitalize_names(names):
    capitalized = []
    for name in names:
        capitalized.append(name.capitalize())
    return capitalized

names = ["alice", "bob", "charlie"]
print(capitalize_names(names))  # ['Alice', 'Bob', 'Charlie']
```

### Lambda Functions (Brief Introduction)

**Lambda functions** are small, anonymous functions:

```python
# Regular function
def square(x):
    return x * x

# Lambda function (equivalent)
square = lambda x: x * x

print(square(5))  # 25

# Often used with map, filter, etc.
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x * x, numbers))
print(squared)  # [1, 4, 9, 16, 25]
```

**Note:** We'll cover lambda functions in more detail later. For now, regular functions are usually clearer.

### Common Mistakes

1. **Forgetting to call the function**
   ```python
   def greet():
       print("Hello!")
   
   greet  # ❌ This doesn't call the function, just references it
   greet()  # ✅ This calls the function
   ```

2. **Missing return statement**
   ```python
   def add(a, b):
       result = a + b
       # Forgot return!
   
   sum = add(3, 4)
   print(sum)  # Output: None
   ```

3. **Wrong number of arguments**
   ```python
   def greet(name, age):
       print(f"Hello, {name}, age {age}")
   
   greet("Saad")  # ❌ Error! Missing argument
   greet("Saad", 21)  # ✅ Correct
   ```

4. **Modifying mutable parameters**
   ```python
   def add_item(lst, item):
       lst.append(item)  # Modifies the original list!
   
   my_list = [1, 2, 3]
   add_item(my_list, 4)
   print(my_list)  # [1, 2, 3, 4] - original list changed!
   ```

---

## 2. Dictionaries — Key-Value Pairs

### What are Dictionaries?

A **dictionary** is a collection of key-value pairs. Think of it like a real dictionary: you look up a word (key) to find its definition (value).

**Key characteristics:**
- **Unordered** (in Python < 3.7, ordered in 3.7+)
- **Mutable** (can be changed)
- **Keys must be unique**
- **Keys must be immutable** (strings, numbers, tuples)

### Creating Dictionaries

**Empty dictionary:**
```python
empty_dict = {}
# or
empty_dict = dict()
```

**Dictionary with values:**
```python
# Method 1: Using curly braces
student = {
    "name": "Saad",
    "age": 21,
    "grade": "A"
}

# Method 2: Using dict() constructor
student = dict(name="Saad", age=21, grade="A")
```

**Keys can be different types:**
```python
mixed_dict = {
    "name": "Saad",
    1: "one",
    (2, 3): "tuple key"
}
```

### Accessing Dictionary Values

**Using square brackets:**
```python
student = {"name": "Saad", "age": 21, "grade": "A"}

print(student["name"])   # Output: Saad
print(student["age"])    # Output: 21

# print(student["city"])  # ❌ KeyError if key doesn't exist
```

**Using `.get()` method (safer):**
```python
student = {"name": "Saad", "age": 21}

print(student.get("name"))        # Output: Saad
print(student.get("city"))        # Output: None (no error!)
print(student.get("city", "N/A")) # Output: N/A (default value)
```

### Modifying Dictionaries

**Adding/Updating items:**
```python
student = {"name": "Saad", "age": 21}

# Add new key-value pair
student["grade"] = "A"
print(student)  # {'name': 'Saad', 'age': 21, 'grade': 'A'}

# Update existing value
student["age"] = 22
print(student)  # {'name': 'Saad', 'age': 22, 'grade': 'A'}
```

**Removing items:**
```python
student = {"name": "Saad", "age": 21, "grade": "A"}

# Method 1: del statement
del student["grade"]
print(student)  # {'name': 'Saad', 'age': 21}

# Method 2: pop() method (returns the value)
age = student.pop("age")
print(age)      # 21
print(student)  # {'name': 'Saad'}

# Method 3: popitem() - removes and returns last item (Python 3.7+)
student = {"name": "Saad", "age": 21}
item = student.popitem()
print(item)     # ('age', 21)
print(student)  # {'name': 'Saad'}

# Method 4: clear() - removes all items
student.clear()
print(student)  # {}
```

### Dictionary Methods

**Common methods:**

```python
student = {"name": "Saad", "age": 21, "grade": "A"}

# Get all keys
print(student.keys())    # dict_keys(['name', 'age', 'grade'])

# Get all values
print(student.values())   # dict_values(['Saad', 21, 'A'])

# Get all key-value pairs (items)
print(student.items())   # dict_items([('name', 'Saad'), ('age', 21), ('grade', 'A')])

# Check if key exists
print("name" in student)  # True
print("city" in student)  # False

# Get number of items
print(len(student))       # 3

# Copy dictionary
student_copy = student.copy()
```

### Iterating Over Dictionaries

**Iterate over keys:**
```python
student = {"name": "Saad", "age": 21, "grade": "A"}

for key in student:
    print(key)

# Output:
# name
# age
# grade

# Or explicitly:
for key in student.keys():
    print(key)
```

**Iterate over values:**
```python
for value in student.values():
    print(value)

# Output:
# Saad
# 21
# A
```

**Iterate over key-value pairs:**
```python
for key, value in student.items():
    print(f"{key}: {value}")

# Output:
# name: Saad
# age: 21
# grade: A
```

### Nested Dictionaries

Dictionaries can contain other dictionaries:

```python
students = {
    "student1": {
        "name": "Saad",
        "age": 21,
        "grades": [85, 90, 88]
    },
    "student2": {
        "name": "Alice",
        "age": 20,
        "grades": [92, 87, 95]
    }
}

# Access nested values
print(students["student1"]["name"])           # Saad
print(students["student1"]["grades"][0])      # 85

# Modify nested values
students["student1"]["age"] = 22
```

### Dictionary Comprehensions

Similar to list comprehensions, but for dictionaries:

```python
# Create dictionary from numbers and their squares
squares = {x: x*x for x in range(1, 6)}
print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# With condition
even_squares = {x: x*x for x in range(1, 11) if x % 2 == 0}
print(even_squares)  # {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}
```

### Common Dictionary Patterns

**1. Counting occurrences:**
```python
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
count = {}

for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

print(count)  # {'apple': 3, 'banana': 2, 'orange': 1}

# Using get() method (cleaner):
count = {}
for word in words:
    count[word] = count.get(word, 0) + 1
```

**2. Grouping data:**
```python
students = [
    {"name": "Saad", "grade": "A"},
    {"name": "Alice", "grade": "B"},
    {"name": "Bob", "grade": "A"},
    {"name": "Charlie", "grade": "C"}
]

# Group by grade
by_grade = {}
for student in students:
    grade = student["grade"]
    if grade not in by_grade:
        by_grade[grade] = []
    by_grade[grade].append(student["name"])

print(by_grade)  # {'A': ['Saad', 'Bob'], 'B': ['Alice'], 'C': ['Charlie']}
```

**3. Default values:**
```python
# Using setdefault()
data = {}
data.setdefault("count", 0)
data["count"] += 1
print(data)  # {'count': 1}

# Using defaultdict (from collections module - advanced)
from collections import defaultdict
count = defaultdict(int)  # Default value is 0
count["apple"] += 1
print(count["apple"])  # 1
```

### Dictionary vs List

**When to use a dictionary:**
- You need to look up values by a key (name, ID, etc.)
- Data has a natural key-value relationship
- You need fast lookups by key

**When to use a list:**
- Order matters
- You need to access items by position (index)
- You're storing a simple sequence of items

**Example comparison:**
```python
# List - accessing by index
students = ["Saad", "Alice", "Bob"]
print(students[0])  # Saad

# Dictionary - accessing by key
students = {1: "Saad", 2: "Alice", 3: "Bob"}
print(students[1])  # Saad

# Dictionary with meaningful keys
students = {"id1": "Saad", "id2": "Alice", "id3": "Bob"}
print(students["id1"])  # Saad
```

### Common Mistakes

1. **Accessing non-existent key**
   ```python
   student = {"name": "Saad"}
   # print(student["age"])  # ❌ KeyError
   
   # ✅ Use get() instead
   print(student.get("age", "N/A"))  # N/A
   ```

2. **Using mutable objects as keys**
   ```python
   # ❌ WRONG - lists are mutable
   # my_dict = {[1, 2]: "value"}  # TypeError!
   
   # ✅ CORRECT - tuples are immutable
   my_dict = {(1, 2): "value"}  # OK
   ```

3. **Confusing keys() and values()**
   ```python
   student = {"name": "Saad", "age": 21}
   
   # Keys are the left side
   print(list(student.keys()))    # ['name', 'age']
   
   # Values are the right side
   print(list(student.values()))  # ['Saad', 21]
   ```

---

## 3. Combining Functions and Dictionaries

### Functions That Work with Dictionaries

```python
def get_student_info(student_dict):
    """Extract and format student information."""
    name = student_dict.get("name", "Unknown")
    age = student_dict.get("age", "N/A")
    return f"Name: {name}, Age: {age}"

student = {"name": "Saad", "age": 21}
print(get_student_info(student))  # Name: Saad, Age: 21
```

### Functions That Return Dictionaries

```python
def create_student(name, age, grade):
    """Create a student dictionary."""
    return {
        "name": name,
        "age": age,
        "grade": grade
    }

student = create_student("Saad", 21, "A")
print(student)  # {'name': 'Saad', 'age': 21, 'grade': 'A'}
```

### Processing Dictionary Data

```python
def calculate_average_grades(students):
    """Calculate average grade for each student."""
    averages = {}
    for name, grades in students.items():
        avg = sum(grades) / len(grades)
        averages[name] = avg
    return averages

students = {
    "Saad": [85, 90, 88],
    "Alice": [92, 87, 95]
}

averages = calculate_average_grades(students)
print(averages)  # {'Saad': 87.67..., 'Alice': 91.33...}
```

---

## Putting It All Together

Here's a complete example using functions and dictionaries:

```python
def create_student(name, age, grades):
    """Create a student dictionary."""
    return {
        "name": name,
        "age": age,
        "grades": grades
    }

def calculate_average(grades):
    """Calculate average of a list of grades."""
    if not grades:
        return 0
    return sum(grades) / len(grades)

def get_student_summary(student):
    """Get a formatted summary of a student."""
    name = student["name"]
    age = student["age"]
    avg = calculate_average(student["grades"])
    return f"{name} (age {age}) has an average grade of {avg:.2f}"

# Create students
students = [
    create_student("Saad", 21, [85, 90, 88]),
    create_student("Alice", 20, [92, 87, 95]),
    create_student("Bob", 22, [78, 82, 80])
]

# Process and display
for student in students:
    print(get_student_summary(student))
```

---

## Key Takeaways

1. **Functions** are reusable blocks of code that can take parameters and return values
2. **Parameters** receive values when a function is called
3. **Return** statements send values back from functions
4. **Dictionaries** store key-value pairs for efficient data organization
5. **Keys** must be unique and immutable
6. Use `.get()` for safe dictionary access
7. Functions and dictionaries work great together for organizing code and data
8. **Scope** determines where variables can be accessed

---

## Next Steps

Practice with the exercises file! Functions and dictionaries are powerful tools that you'll use constantly in Python programming. The more you practice, the more natural they'll become.

Good luck! 🚀

