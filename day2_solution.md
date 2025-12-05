# Day 2: Python Exercises — Solutions

**Note:** Only check these solutions after you've attempted the problems yourself!

---

## Exercise 1: Conditionals

### Solution 1.1

```python
num = 5

if num > 0:
    print(f"{num} is positive")
elif num < 0:
    print(f"{num} is negative")
else:
    print(f"{num} is zero")

# Test with different values:
# num = -3  -> "-3 is negative"
# num = 0   -> "0 is zero"
# num = 5   -> "5 is positive"
```

---

### Solution 1.2

```python
age = 20
is_citizen = True

if age >= 18 and is_citizen:
    print("You can vote!")
else:
    print("You cannot vote!")

# Alternative with more detailed messages:
# if age >= 18 and is_citizen:
#     print("You can vote!")
# elif age < 18:
#     print("You cannot vote - too young!")
# else:
#     print("You cannot vote - not a citizen!")
```

---

### Solution 1.3

```python
score = 85

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

print(f"Score: {score}, Grade: {grade}")  # Score: 85, Grade: B
```

---

### Solution 1.4

```python
year = 2024

# A year is a leap year if:
# - divisible by 4 AND not divisible by 100, OR
# - divisible by 400
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

# Test cases:
# 2024 -> leap year (divisible by 4, not by 100)
# 2000 -> leap year (divisible by 400)
# 1900 -> not leap year (divisible by 100 but not 400)
# 2023 -> not leap year (not divisible by 4)
```

---

## Exercise 2: For Loops

### Solution 2.1

```python
for i in range(1, 11):
    print(i)

# Output:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
```

---

### Solution 2.2

```python
for i in range(1, 6):
    square = i * i
    print(f"{i} squared is {square}")

# Or more concisely:
# for i in range(1, 6):
#     print(f"{i} squared is {i * i}")
```

---

### Solution 2.3

```python
fruits = ["apple", "banana", "orange", "grape", "mango"]

# Print each fruit with index starting from 1
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}")

# Count fruits with more than 5 letters
count = 0
for fruit in fruits:
    if len(fruit) > 5:
        count += 1

print(f"\nFruits with more than 5 letters: {count}")

# Alternative using enumerate:
# count = 0
# for i, fruit in enumerate(fruits, start=1):
#     print(f"{i}. {fruit}")
#     if len(fruit) > 5:
#         count += 1
```

---

### Solution 2.4

```python
total = 0

for num in range(1, 21):
    if num % 2 == 0:  # Check if even
        total += num

print(f"Sum of even numbers from 1 to 20: {total}")  # 110

# Alternative using range with step:
# total = 0
# for num in range(2, 21, 2):  # Start at 2, go to 20, step by 2
#     total += num
# print(f"Sum of even numbers from 1 to 20: {total}")
```

---

### Solution 2.5

```python
numbers = [12, 45, 23, 67, 34, 89, 56]

# Find largest
largest = numbers[0]  # Start with first number
for num in numbers:
    if num > largest:
        largest = num

print(f"Largest number: {largest}")  # 89

# Find smallest
smallest = numbers[0]  # Start with first number
for num in numbers:
    if num < smallest:
        smallest = num

print(f"Smallest number: {smallest}")  # 12

# Or do both in one loop:
# largest = numbers[0]
# smallest = numbers[0]
# for num in numbers:
#     if num > largest:
#         largest = num
#     if num < smallest:
#         smallest = num
```

---

## Exercise 3: While Loops

### Solution 3.1

```python
count = 10

while count >= 1:
    print(count)
    count -= 1  # Decrement count

print("Blast off!")

# Output:
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# Blast off!
```

---

### Solution 3.2

```python
# Simulating user input
user_input = -5

while user_input <= 0:
    print(f"Invalid input: {user_input}. Please enter a positive number.")
    # Simulate getting new input
    if user_input == -5:
        user_input = 0
    elif user_input == 0:
        user_input = 10
    else:
        break

if user_input > 0:
    print(f"Thank you! You entered: {user_input}")

# In a real program with actual user input:
# user_input = int(input("Enter a positive number: "))
# while user_input <= 0:
#     print("Invalid! Please enter a positive number.")
#     user_input = int(input("Enter a positive number: "))
# print(f"Thank you! You entered: {user_input}")
```

---

### Solution 3.3

```python
n = 5
factorial = 1
counter = n

while counter > 0:
    factorial *= counter
    counter -= 1

print(f"Factorial of {n} is {factorial}")  # 120

# Alternative approach:
# n = 5
# factorial = 1
# while n > 0:
#     factorial *= n
#     n -= 1
# print(f"Factorial is {factorial}")
```

---

## Exercise 4: Combining Conditionals and Loops

### Solution 4.1

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    # Skip numbers divisible by 3
    if num % 3 == 0:
        continue
    
    # Check if even or odd
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

# Output:
# 1 is odd
# 2 is even
# 4 is even
# 5 is odd
# 7 is odd
# 8 is even
# 10 is even
```

---

### Solution 4.2

```python
numbers = [12, 45, 23, 67, 34, 89, 56]

for num in numbers:
    if num > 50:
        print(f"First number greater than 50: {num}")
        break

# Output: First number greater than 50: 67
```

---

### Solution 4.3

```python
scores = [85, 92, 78, 96, 88, 91, 75]

high_count = 0
medium_count = 0
low_count = 0

for score in scores:
    if score >= 90:
        high_count += 1
    elif score >= 70:
        medium_count += 1
    else:
        low_count += 1

print(f"High scores (>= 90): {high_count}")    # 3
print(f"Medium scores (70-89): {medium_count}")  # 4
print(f"Low scores (< 70): {low_count}")       # 0
```

---

## Exercise 5: Challenge Problems

### Solution 5.1

```python
# Multiplication table for 1 to 5
for i in range(1, 6):
    # Print one row
    row = ""
    for j in range(1, 6):
        result = i * j
        row += f"{i} x {j} = {result:2d}   "  # :2d formats to 2 digits
    print(row)

# Output:
# 1 x 1 =  1    1 x 2 =  2    1 x 3 =  3    1 x 4 =  4    1 x 5 =  5
# 2 x 1 =  2    2 x 2 =  4    2 x 3 =  6    2 x 4 =  8    2 x 5 = 10
# 3 x 1 =  3    3 x 2 =  6    3 x 3 =  9    3 x 4 = 12    3 x 5 = 15
# 4 x 1 =  4    4 x 2 =  8    4 x 3 = 12    4 x 4 = 16    4 x 5 = 20
# 5 x 1 =  5    5 x 2 = 10    5 x 3 = 15    5 x 4 = 20    5 x 5 = 25
```

---

### Solution 5.2

```python
print("Prime numbers between 1 and 20:")

for num in range(2, 21):  # Start from 2 (1 is not prime)
    is_prime = True
    
    # Check if num is divisible by any number from 2 to num-1
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break  # Found a divisor, not prime
    
    if is_prime:
        print(num)

# Output:
# Prime numbers between 1 and 20:
# 2
# 3
# 5
# 7
# 11
# 13
# 17
# 19
```

---

### Solution 5.3

```python
words = ["python", "java", "javascript", "c++", "python", "java"]
counted = []  # Track which words we've already counted

for word in words:
    # Only count if we haven't counted this word yet
    if word not in counted:
        count = words.count(word)
        print(f"{word}: {count} time(s)")
        counted.append(word)  # Mark as counted

# Output:
# python: 2 time(s)
# java: 2 time(s)
# javascript: 1 time(s)
# c++: 1 time(s)

# Alternative approach using a loop to count:
# words = ["python", "java", "javascript", "c++", "python", "java"]
# counted = []
# 
# for word in words:
#     if word not in counted:
#         count = 0
#         for w in words:
#             if w == word:
#                 count += 1
#         print(f"{word}: {count} time(s)")
#         counted.append(word)
```

---

## Additional Notes

- **Loop efficiency:** In Solution 5.3, using `words.count(word)` is simpler but less efficient for large lists. The alternative approach with a nested loop is more explicit.

- **Prime number optimization:** The prime number solution can be optimized further (e.g., only check divisors up to √n), but the current solution is clear and correct.

- **Formatting:** In Solution 5.1, `:2d` formats numbers to 2 digits with leading spaces for alignment. You can experiment with different formatting options.

- **Edge cases:** Always consider edge cases:
  - Empty lists
  - Single-item lists
  - All items meeting/not meeting conditions
  - Boundary values (0, negative numbers, etc.)

---

**Keep practicing! Loops and conditionals are the building blocks of all programming. 🚀**

