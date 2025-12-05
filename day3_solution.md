# Day 3: Python Exercises — Solutions

**Note:** Only check these solutions after you've attempted the problems yourself!

---

## Exercise 1: Functions Basics

### Solution 1.1

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Saad")  # Output: Hello, Saad!

# Or using string concatenation:
# def greet(name):
#     print("Hello, " + name + "!")
```

---

### Solution 1.2

```python
def add(a, b):
    return a + b

result1 = add(5, 3)
result2 = add(10, 20)

print(result1)  # 8
print(result2)  # 30

# Or directly:
# print(add(5, 3))   # 8
# print(add(10, 20)) # 30
```

---

### Solution 1.3

```python
def is_even(num):
    return num % 2 == 0

print(is_even(4))   # True
print(is_even(5))   # False
print(is_even(0))   # True
print(is_even(-3))  # False
```

---

### Solution 1.4

```python
def find_max(numbers):
    if not numbers:  # Handle empty list
        return None
    
    max_value = numbers[0]  # Start with first number
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value

result = find_max([3, 7, 2, 9, 1])
print(result)  # 9

# Test with other cases:
# print(find_max([1]))        # 1
# print(find_max([-5, -2, -8]))  # -2
```

---

### Solution 1.5

```python
def count_words(words):
    return len(words)

result = count_words(["apple", "banana", "orange"])
print(result)  # 3

# Or with empty list:
# print(count_words([]))  # 0
```

---

## Exercise 2: Function Parameters

### Solution 2.1

```python
def calculate_area(length, width):
    return length * width

area = calculate_area(5, 3)
print(area)  # 15

# Or directly:
# print(calculate_area(5, 3))  # 15
```

---

### Solution 2.2

```python
def introduce(name, age, city):
    print(f"My name is {name}, I am {age} years old, and I live in {city}.")

introduce("Saad", 21, "New York")
# Output: My name is Saad, I am 21 years old, and I live in New York.

# Or using string concatenation:
# def introduce(name, age, city):
#     print("My name is " + name + ", I am " + str(age) + " years old, and I live in " + city + ".")
```

---

### Solution 2.3

```python
def greet_with_default(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet_with_default("Saad")        # Output: Hello, Saad!
greet_with_default("Saad", "Hi") # Output: Hi, Saad!
```

---

### Solution 2.4

```python
def multiply(a, b, factor=1):
    return a * b * factor

print(multiply(3, 4))    # 12 (3 * 4 * 1)
print(multiply(3, 4, 2)) # 24 (3 * 4 * 2)
```

---

## Exercise 3: Dictionaries Basics

### Solution 3.1

```python
student = {
    "name": "Saad",
    "age": 21,
    "grade": "A"
}

print(student)           # {'name': 'Saad', 'age': 21, 'grade': 'A'}
print(student["name"])   # Saad
print(student["age"])    # 21
```

---

### Solution 3.2

```python
person = {"name": "Alice", "age": 25, "city": "New York"}

# Add new key
person["occupation"] = "Engineer"

# Update age
person["age"] = 26

# Remove city
del person["city"]
# Or: person.pop("city")

print(person)  # {'name': 'Alice', 'age': 26, 'occupation': 'Engineer'}
```

---

### Solution 3.3

```python
scores = {"math": 85, "science": 92, "english": 78}

# Print all keys
print(list(scores.keys()))    # ['math', 'science', 'english']

# Print all values
print(list(scores.values()))  # [85, 92, 78]

# Print all key-value pairs
print(list(scores.items()))   # [('math', 85), ('science', 92), ('english', 78)]

# Calculate average
average = sum(scores.values()) / len(scores)
print(f"Average score: {average}")  # Average score: 85.0
```

---

### Solution 3.4

```python
fruits = {"apple": 5, "banana": 3, "orange": 8}

# Check if "banana" exists
print("banana" in fruits)  # True

# Get value for "banana" with default
banana_count = fruits.get("banana", 0)
print(banana_count)  # 3

# Get value for "grape" with default (doesn't exist)
grape_count = fruits.get("grape", 0)
print(grape_count)  # 0

print(f"Banana: {banana_count}, Grape: {grape_count}")
```

---

## Exercise 4: Working with Dictionaries

### Solution 4.1

```python
def count_letters(text):
    count = {}
    for char in text:
        # Get current count (0 if not found) and add 1
        count[char] = count.get(char, 0) + 1
    return count

result = count_letters("hello")
print(result)  # {'h': 1, 'e': 1, 'l': 2, 'o': 1}

# Alternative approach:
# def count_letters(text):
#     count = {}
#     for char in text:
#         if char in count:
#             count[char] += 1
#         else:
#             count[char] = 1
#     return count
```

---

### Solution 4.2

```python
def merge_dicts(dict1, dict2):
    merged = {}
    
    # Add all items from first dictionary
    for key, value in dict1.items():
        merged[key] = value
    
    # Add/update with items from second dictionary
    for key, value in dict2.items():
        merged[key] = value
    
    return merged

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

result = merge_dicts(dict1, dict2)
print(result)  # {'a': 1, 'b': 3, 'c': 4}

# Note: dict2's values overwrite dict1's for duplicate keys
```

---

### Solution 4.3

```python
def get_averages(students):
    averages = {}
    for name, grades in students.items():
        avg = sum(grades) / len(grades)
        averages[name] = avg
    return averages

students = {
    "Alice": [85, 90, 88],
    "Bob": [78, 82, 80],
    "Charlie": [92, 87, 95]
}

result = get_averages(students)
print(result)  # {'Alice': 87.666..., 'Bob': 80.0, 'Charlie': 91.333...}

# To print with 2 decimal places:
# for name, avg in result.items():
#     print(f"{name}: {avg:.2f}")
```

---

## Exercise 5: Challenge Problems

### Solution 5.1

```python
def filter_dict(dictionary, min_value):
    filtered = {}
    for key, value in dictionary.items():
        if value >= min_value:
            filtered[key] = value
    return filtered

scores = {"math": 85, "science": 92, "english": 78, "history": 65}
min_score = 80

result = filter_dict(scores, min_score)
print(result)  # {'math': 85, 'science': 92}

# Using dictionary comprehension (more Pythonic):
# def filter_dict(dictionary, min_value):
#     return {k: v for k, v in dictionary.items() if v >= min_value}
```

---

### Solution 5.2

```python
def invert_dict(original):
    inverted = {}
    for key, value in original.items():
        inverted[value] = key
    return inverted

original = {"a": 1, "b": 2, "c": 3}
result = invert_dict(original)
print(result)  # {1: 'a', 2: 'b', 3: 'c'}

# Using dictionary comprehension:
# def invert_dict(original):
#     return {value: key for key, value in original.items()}

# Note: This will fail if values are not unique or are mutable
# original = {"a": 1, "b": 1}  # Duplicate values!
# result = invert_dict(original)  # Only one will be kept
```

---

### Solution 5.3

```python
def group_by_category(items):
    grouped = {}
    for item in items:
        category = item["category"]
        name = item["name"]
        
        # If category doesn't exist, create empty list
        if category not in grouped:
            grouped[category] = []
        
        # Add name to the category's list
        grouped[category].append(name)
    
    return grouped

items = [
    {"name": "apple", "category": "fruit"},
    {"name": "carrot", "category": "vegetable"},
    {"name": "banana", "category": "fruit"},
    {"name": "broccoli", "category": "vegetable"}
]

result = group_by_category(items)
print(result)
# Output: {'fruit': ['apple', 'banana'], 'vegetable': ['carrot', 'broccoli']}

# Alternative using setdefault():
# def group_by_category(items):
#     grouped = {}
#     for item in items:
#         category = item["category"]
#         name = item["name"]
#         grouped.setdefault(category, []).append(name)
#     return grouped
```

---

## Additional Notes

- **Function design:** Functions should do one thing well. If a function is doing too much, consider breaking it into smaller functions.

- **Dictionary methods:** Remember that `.keys()`, `.values()`, and `.items()` return view objects. Convert to lists if you need to modify them: `list(dict.keys())`.

- **Error handling:** In real-world code, you'd often add error handling (checking if keys exist, handling empty lists, etc.). For now, focus on understanding the core concepts.

- **Performance:** Dictionary lookups are very fast (O(1) average case), making them ideal for frequent lookups by key.

- **Best practices:**
  - Use descriptive function names (verbs: `calculate`, `get`, `find`)
  - Use descriptive parameter names
  - Return values instead of printing (unless the function's purpose is to print)
  - Document complex functions with docstrings

---

**Keep practicing! Functions and dictionaries are fundamental tools you'll use constantly. 🚀**

