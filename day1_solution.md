# Day 1: Python Exercises — Solutions

**Note:** Only check these solutions after you've attempted the problems yourself!

---

## Exercise 1: Variables and Basic Types

### Solution 1.1

```python
my_name = "Saad"
my_age = 21
my_height = 1.75

print(f"My name is {my_name}, I am {my_age} years old, and I am {my_height} meters tall.")
# Or using concatenation:
# print("My name is " + my_name + ", I am " + str(my_age) + " years old, and I am " + str(my_height) + " meters tall.")
```

---

### Solution 1.2

```python
a = 15
b = 4

print("Sum:", a + b)           # 19
print("Difference:", a - b)    # 11
print("Product:", a * b)       # 60
print("Quotient:", a / b)      # 3.75
print("Floor division:", a // b)  # 3
print("Remainder:", a % b)     # 3
```

---

### Solution 1.3

```python
text = "Python Programming"

print("First character:", text[0])        # P
print("Last character:", text[-1])        # g
print("Substring 0-6:", text[0:6])       # Python
print("Substring from 7:", text[7:])      # Programming
print("Length:", len(text))               # 18
```

---

## Exercise 2: Boolean Logic

### Solution 2.1

```python
age = 20
has_license = True

print("Is 18 or older?", age >= 18)                           # True
print("Has license?", has_license)                            # True
print("Can drive?", age >= 18 and has_license)                # True
print("Cannot drive?", age < 18 or not has_license)          # False
```

---

### Solution 2.2

```python
is_raining = True
has_umbrella = False
is_indoor = True

should_go_outside = not is_raining or has_umbrella or is_indoor
will_get_wet = is_raining and not has_umbrella and not is_indoor

print("Should I go outside?", should_go_outside)  # True
print("Will I get wet?", will_get_wet)            # False
```

---

## Exercise 3: Lists Basics

### Solution 3.1

```python
fruits = ["apple", "banana", "orange", "grape", "mango"]

print("All fruits:", fruits)              # ['apple', 'banana', 'orange', 'grape', 'mango']
print("First fruit:", fruits[0])          # apple
print("Last fruit:", fruits[-1])          # mango
print("Fruits 1-3:", fruits[1:3])         # ['banana', 'orange']
print("Number of fruits:", len(fruits))   # 5
```

---

### Solution 3.2

```python
shopping_list = []

shopping_list.append("milk")           # ['milk']
shopping_list.append("bread")          # ['milk', 'bread']
shopping_list.insert(0, "eggs")        # ['eggs', 'milk', 'bread']
shopping_list.insert(2, "cheese")      # ['eggs', 'milk', 'cheese', 'bread']
shopping_list.remove("bread")          # ['eggs', 'milk', 'cheese']

print("Final shopping list:", shopping_list)
```

---

### Solution 3.3

```python
numbers = [5, 2, 8, 1, 9, 3]

numbers.sort()
print("Sorted:", numbers)                    # [1, 2, 3, 5, 8, 9]

largest = numbers[-1]
smallest = numbers[0]
total = sum(numbers)
average = total / len(numbers)

print("Largest:", largest)                   # 9
print("Smallest:", smallest)                 # 1
print("Sum:", total)                         # 28
print("Average:", average)                   # 4.666...
```

---

### Solution 3.4

```python
mixed = [10, "hello", 3.14, True, "world"]

# Print each item and its type
for item in mixed:
    print(f"{item} is {type(item).__name__}")

# Count strings
string_count = 0
for item in mixed:
    if type(item) == str:
        string_count += 1
print(f"Number of strings: {string_count}")

# Create list of only strings
strings_only = [item for item in mixed if type(item) == str]
# Or using a loop:
# strings_only = []
# for item in mixed:
#     if type(item) == str:
#         strings_only.append(item)

print("Strings only:", strings_only)  # ['hello', 'world']
```

---

## Exercise 4: List Operations

### Solution 4.1

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Combine lists
list3 = list1 + list2
print("Combined:", list3)  # [1, 2, 3, 4, 5, 6]

# Copy list1
list4 = list1.copy()  # or list4 = list1[:]
list4.append(10)

print("list1:", list1)  # [1, 2, 3] - unchanged!
print("list4:", list4)  # [1, 2, 3, 10] - modified
```

---

### Solution 4.2

```python
scores = [85, 92, 78, 96, 88, 91, 75]

highest = max(scores)
lowest = min(scores)
average = sum(scores) / len(scores)

print("Highest:", highest)      # 96
print("Lowest:", lowest)        # 75
print("Average:", average)      # 86.428...

# Count scores above 85
above_85_count = 0
for score in scores:
    if score > 85:
        above_85_count += 1
print("Scores above 85:", above_85_count)  # 4

# List of scores above 85
above_85 = [score for score in scores if score > 85]
# Or using a loop:
# above_85 = []
# for score in scores:
#     if score > 85:
#         above_85.append(score)

print("Scores above 85:", above_85)  # [92, 96, 88, 91]
```

---

### Solution 4.3

```python
words = ["python", "java", "javascript", "c++", "python", "java"]

# Count occurrences
python_count = words.count("python")
print("'python' appears", python_count, "times")  # 2

# Find first index
java_index = words.index("java")
print("First 'java' at index:", java_index)  # 1

# Remove duplicates
unique_words = []
for word in words:
    if word not in unique_words:
        unique_words.append(word)
print("Unique words:", unique_words)  # ['python', 'java', 'javascript', 'c++']

# Sort alphabetically
unique_words.sort()
print("Sorted unique words:", unique_words)  # ['c++', 'java', 'javascript', 'python']
```

---

## Exercise 5: Challenge Problems

### Solution 5.1

```python
numbers = list(range(1, 11))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Squares
squares = [x * x for x in numbers]
print("Squares:", squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Even numbers
evens = [x for x in numbers if x % 2 == 0]
print("Evens:", evens)  # [2, 4, 6, 8, 10]

# Divisible by 3
divisible_by_3 = [x for x in numbers if x % 3 == 0]
print("Divisible by 3:", divisible_by_3)  # [3, 6, 9]
```

---

### Solution 5.2

```python
students = ["Alice", "Bob", "Charlie", "David", "Eve"]
scores = [85, 92, 78, 96, 88]

# Find highest score and corresponding student
highest_score = max(scores)
highest_index = scores.index(highest_score)
top_student = students[highest_index]
print(f"Top student: {top_student} with {highest_score}")  # David with 96

# Find lowest score and corresponding student
lowest_score = min(scores)
lowest_index = scores.index(lowest_score)
lowest_student = students[lowest_index]
print(f"Lowest score: {lowest_student} with {lowest_score}")  # Charlie with 78

# Print all students with scores
for i in range(len(students)):
    print(f"{students[i]}: {scores[i]}")
# Or using zip (if you know it):
# for student, score in zip(students, scores):
#     print(f"{student}: {score}")
```

---

## Additional Notes

- **Alternative approaches:** Many problems can be solved in multiple ways. The solutions shown are one approach, but feel free to experiment with different methods!

- **Error handling:** In real-world code, you'd often check for edge cases (empty lists, invalid indices, etc.). For now, focus on understanding the core concepts.

- **Best practices:** 
  - Use descriptive variable names
  - Add comments to explain complex logic
  - Test your code with different inputs
  - Break down complex problems into smaller steps

---

**Keep practicing! The more you code, the more comfortable you'll become. 🚀**

