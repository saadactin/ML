# Day 3: Python Exercises — Functions and Dictionaries

**Estimated Time: 30 minutes**

**Instructions:**
- Read each question carefully
- Try to solve it yourself before checking the solution
- Type out the code (don't just read it) — muscle memory helps!
- If you get stuck, read the hint, then try again
- Check the solutions in `day3_solution.md` only after you've attempted the problem

---

## Exercise 1: Functions Basics (10 minutes)

### Question 1.1
Write a function called `greet` that takes a name as a parameter and prints "Hello, [name]!". Test it with your name.

<details>
<summary>Hint</summary>
Define a function with one parameter, then use print() with an f-string or string concatenation.
</details>

---

### Question 1.2
Create a function called `add` that takes two numbers as parameters and returns their sum. Test it with `add(5, 3)` and `add(10, 20)`.

<details>
<summary>Hint</summary>
Use the `return` statement to send back the result of the addition.
</details>

---

### Question 1.3
Write a function called `is_even` that takes a number and returns `True` if it's even, `False` otherwise. Test with both even and odd numbers.

<details>
<summary>Hint</summary>
Use the modulo operator (%) to check if a number is divisible by 2.
</details>

---

### Question 1.4
Create a function called `find_max` that takes a list of numbers and returns the largest number. Test with `[3, 7, 2, 9, 1]`. (Don't use the built-in `max()` function.)

<details>
<summary>Hint</summary>
Loop through the list, keep track of the maximum value seen so far, and return it.
</details>

---

### Question 1.5
Write a function called `count_words` that takes a list of words and returns how many words are in the list. Test with `["apple", "banana", "orange"]`.

<details>
<summary>Hint</summary>
Use `len()` to get the length of the list.
</details>

---

## Exercise 2: Function Parameters (8 minutes)

### Question 2.1
Create a function called `calculate_area` that takes `length` and `width` as parameters and returns the area of a rectangle. Test with length=5 and width=3.

<details>
<summary>Hint</summary>
Area of a rectangle = length × width.
</details>

---

### Question 2.2
Write a function called `introduce` that takes `name`, `age`, and `city` as parameters and prints a sentence like "My name is [name], I am [age] years old, and I live in [city]." Test with your information.

<details>
<summary>Hint</summary>
Use f-strings or string concatenation to format the output.
</details>

---

### Question 2.3
Create a function called `greet_with_default` that takes a `name` parameter and an optional `greeting` parameter (default value "Hello"). It should print "[greeting], [name]!". Test it:
- With one argument: `greet_with_default("Saad")`
- With two arguments: `greet_with_default("Saad", "Hi")`

<details>
<summary>Hint</summary>
Set a default value for the `greeting` parameter in the function definition.
</details>

---

### Question 2.4
Write a function called `multiply` that takes two numbers and an optional `factor` parameter (default value 1). It should return the product of the two numbers multiplied by the factor. Test with:
- `multiply(3, 4)` → should return 12
- `multiply(3, 4, 2)` → should return 24

<details>
<summary>Hint</summary>
Multiply all three numbers together, with factor defaulting to 1.
</details>

---

## Exercise 3: Dictionaries Basics (7 minutes)

### Question 3.1
Create a dictionary called `student` with keys: "name", "age", and "grade". Set values to your information. Then:
- Print the entire dictionary
- Print just the name
- Print just the age

<details>
<summary>Hint</summary>
Use curly braces to create the dictionary, then access values using square brackets.
</details>

---

### Question 3.2
Given a dictionary `person = {"name": "Alice", "age": 25, "city": "New York"}`, write code to:
- Add a new key "occupation" with value "Engineer"
- Update the age to 26
- Remove the "city" key
- Print the final dictionary

<details>
<summary>Hint</summary>
Use assignment to add/update, and `del` or `.pop()` to remove keys.
</details>

---

### Question 3.3
Create a dictionary `scores = {"math": 85, "science": 92, "english": 78}`. Write code to:
- Print all the keys
- Print all the values
- Print all key-value pairs
- Calculate and print the average score

<details>
<summary>Hint</summary>
Use `.keys()`, `.values()`, `.items()` methods, and `sum()` with `.values()` for average.
</details>

---

### Question 3.4
Given `fruits = {"apple": 5, "banana": 3, "orange": 8}`, write code to:
- Check if "banana" exists in the dictionary
- Get the value for "banana" using `.get()` with a default of 0
- Get the value for "grape" using `.get()` with a default of 0
- Print both results

<details>
<summary>Hint</summary>
Use `in` to check existence, and `.get(key, default)` for safe access.
</details>

---

## Exercise 4: Working with Dictionaries (5 minutes)

### Question 4.1
Create a function called `count_letters` that takes a string and returns a dictionary where keys are letters and values are how many times each letter appears. Test with `"hello"`.

<details>
<summary>Hint</summary>
Loop through each character, use `.get()` to safely increment counts in a dictionary.
</details>

---

### Question 4.2
Write a function called `merge_dicts` that takes two dictionaries and returns a new dictionary containing all key-value pairs from both. If there are duplicate keys, use the value from the second dictionary. Test with:
- `dict1 = {"a": 1, "b": 2}`
- `dict2 = {"b": 3, "c": 4}`

<details>
<summary>Hint</summary>
Create a new dictionary, add all items from first dict, then add/update with items from second dict.
</details>

---

### Question 4.3
Create a dictionary `students = {"Alice": [85, 90, 88], "Bob": [78, 82, 80], "Charlie": [92, 87, 95]}`. Write a function `get_averages` that takes this dictionary and returns a new dictionary with student names as keys and their average scores as values.

<details>
<summary>Hint</summary>
Loop through items, calculate average for each student's grades, store in new dictionary.
</details>

---

## Exercise 5: Challenge Problems (Optional - if you have time)

### Question 5.1
Write a function called `filter_dict` that takes a dictionary and a minimum value, and returns a new dictionary containing only key-value pairs where the value is greater than or equal to the minimum. Test with:
- `scores = {"math": 85, "science": 92, "english": 78, "history": 65}`
- `min_score = 80`

<details>
<summary>Hint</summary>
Loop through items, check if value meets condition, add to new dictionary if it does.
</details>

---

### Question 5.2
Create a function called `invert_dict` that takes a dictionary and returns a new dictionary where keys and values are swapped. Test with:
- `original = {"a": 1, "b": 2, "c": 3}`
- Should return `{1: "a", 2: "b", 3: "c"}`

**Note:** This only works if all values are unique and immutable.

<details>
<summary>Hint</summary>
Loop through items, use value as new key and key as new value.
</details>

---

### Question 5.3
Write a function called `group_by_category` that takes a list of dictionaries (each with "name" and "category" keys) and returns a dictionary where keys are categories and values are lists of names in that category. Test with:
```python
items = [
    {"name": "apple", "category": "fruit"},
    {"name": "carrot", "category": "vegetable"},
    {"name": "banana", "category": "fruit"},
    {"name": "broccoli", "category": "vegetable"}
]
```

<details>
<summary>Hint</summary>
Loop through items, check if category exists in result dict, if not create empty list, then append name.
</details>

---

## Final Check

Before moving on, make sure you can:
- ✅ Define functions with parameters
- ✅ Return values from functions
- ✅ Use default parameters
- ✅ Create and modify dictionaries
- ✅ Access dictionary values safely
- ✅ Iterate over dictionaries
- ✅ Combine functions and dictionaries
- ✅ Understand variable scope

---

## Tips for Learning

1. **Start simple** - Get a basic function working, then add complexity.

2. **Test your functions** - Call them with different inputs to make sure they work correctly.

3. **Use meaningful names** - Function and parameter names should describe what they do.

4. **Practice with real data** - Try creating functions for problems you care about.

5. **Read error messages** - They tell you exactly what went wrong (missing parameter, wrong type, etc.).

6. **Think about return vs print** - Functions should usually return values, not print them (unless that's their purpose).

---

**Great job completing Day 3! 🎉**

You've learned functions (reusable code) and dictionaries (key-value storage). These are essential tools that will make your code more organized and powerful!

