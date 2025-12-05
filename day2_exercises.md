# Day 2: Python Exercises — Conditionals and Loops

**Estimated Time: 30 minutes**

**Instructions:**
- Read each question carefully
- Try to solve it yourself before checking the solution
- Type out the code (don't just read it) — muscle memory helps!
- If you get stuck, read the hint, then try again
- Check the solutions in `day2_solution.md` only after you've attempted the problem

---

## Exercise 1: Conditionals (8 minutes)

### Question 1.1
Write a program that checks if a number is positive, negative, or zero. Use variables `num = 5` and test with different values.

<details>
<summary>Hint</summary>
Use if, elif, and else to check if the number is greater than, less than, or equal to zero.
</details>

---

### Question 1.2
Create a program that determines if a person can vote. Variables: `age = 20` and `is_citizen = True`. A person can vote if they are 18 or older AND are a citizen.

<details>
<summary>Hint</summary>
Use the `and` operator to check both conditions.
</details>

---

### Question 1.3
Write a program that assigns a letter grade based on a score:
- 90-100: A
- 80-89: B
- 70-79: C
- 60-69: D
- Below 60: F

Test with `score = 85`.

<details>
<summary>Hint</summary>
Use if, elif, and else. Remember to check from highest to lowest.
</details>

---

### Question 1.4
Create a program that checks if a year is a leap year. A year is a leap year if:
- It is divisible by 4, AND
- It is NOT divisible by 100, OR
- It IS divisible by 400

Test with `year = 2024`.

<details>
<summary>Hint</summary>
Use the modulo operator (%) to check divisibility. Combine conditions with `and` and `or`.
</details>

---

## Exercise 2: For Loops (10 minutes)

### Question 2.1
Write a program that prints all numbers from 1 to 10 using a for loop.

<details>
<summary>Hint</summary>
Use `range(1, 11)` to generate numbers from 1 to 10.
</details>

---

### Question 2.2
Create a program that prints the square of each number from 1 to 5. Output should be:
```
1 squared is 1
2 squared is 4
3 squared is 9
4 squared is 16
5 squared is 25
```

<details>
<summary>Hint</summary>
Use a for loop with range, and calculate the square inside the loop.
</details>

---

### Question 2.3
Given a list `fruits = ["apple", "banana", "orange", "grape", "mango"]`, write a program that:
- Prints each fruit with its index (starting from 1, not 0)
- Counts how many fruits have more than 5 letters

<details>
<summary>Hint</summary>
Use `enumerate()` or `range(len())` to get both index and value. Use `len()` to check string length.
</details>

---

### Question 2.4
Create a program that finds the sum of all even numbers from 1 to 20 (inclusive).

<details>
<summary>Hint</summary>
Use a for loop with range, check if number is even using modulo (%), and accumulate the sum.
</details>

---

### Question 2.5
Given a list `numbers = [12, 45, 23, 67, 34, 89, 56]`, write a program that:
- Finds the largest number in the list (without using `max()`)
- Finds the smallest number in the list (without using `min()`)

<details>
<summary>Hint</summary>
Initialize variables to track max and min, then loop through the list and update them.
</details>

---

## Exercise 3: While Loops (7 minutes)

### Question 3.1
Write a program that counts down from 10 to 1 using a while loop, then prints "Blast off!".

<details>
<summary>Hint</summary>
Start with a counter at 10, decrement it in each iteration, and stop when it reaches 0.
</details>

---

### Question 3.2
Create a program that keeps asking the user for a number until they enter a positive number. (For this exercise, simulate with a variable `user_input = -5`, then `user_input = 0`, then `user_input = 10`)

<details>
<summary>Hint</summary>
Use a while loop that continues while the number is not positive. You can simulate user input by changing the variable value.
</details>

---

### Question 3.3
Write a program that calculates the factorial of a number using a while loop. Factorial of 5 = 5 × 4 × 3 × 2 × 1 = 120. Test with `n = 5`.

<details>
<summary>Hint</summary>
Start with result = 1, use a counter that decreases from n to 1, multiply result by the counter each time.
</details>

---

## Exercise 4: Combining Conditionals and Loops (5 minutes)

### Question 4.1
Given a list `numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`, write a program that:
- Prints "even" for even numbers
- Prints "odd" for odd numbers
- Skips numbers divisible by 3 (use `continue`)

<details>
<summary>Hint</summary>
Use a for loop, check if divisible by 3 first (continue), then check if even or odd.
</details>

---

### Question 4.2
Create a program that finds the first number in a list that is greater than 50. Use `numbers = [12, 45, 23, 67, 34, 89, 56]`. Stop searching once you find it (use `break`).

<details>
<summary>Hint</summary>
Loop through the list, check if number > 50, print it and break.
</details>

---

### Question 4.3
Write a program that processes a list of scores and categorizes them:
- `scores = [85, 92, 78, 96, 88, 91, 75]`
- Count how many are "High" (>= 90), "Medium" (70-89), and "Low" (< 70)
- Print the counts

<details>
<summary>Hint</summary>
Use a for loop with if/elif/else to categorize each score, and use counters for each category.
</details>

---

## Exercise 5: Challenge Problems (Optional - if you have time)

### Question 5.1
Write a program that prints a multiplication table for numbers 1 to 5. The output should look like:
```
1 x 1 = 1   1 x 2 = 2   1 x 3 = 3   1 x 4 = 4   1 x 5 = 5
2 x 1 = 2   2 x 2 = 4   2 x 3 = 6   2 x 4 = 8   2 x 5 = 10
...
```

<details>
<summary>Hint</summary>
Use nested for loops. The outer loop for the first number, inner loop for the second number.
</details>

---

### Question 5.2
Create a program that finds all prime numbers between 1 and 20. A prime number is only divisible by 1 and itself.

<details>
<summary>Hint</summary>
For each number from 2 to 20, check if it's divisible by any number from 2 to number-1. If not, it's prime.
</details>

---

### Question 5.3
Write a program that processes a list of words and:
- `words = ["python", "java", "javascript", "c++", "python", "java"]`
- Counts how many times each word appears
- Prints each word and its count (only once per unique word)

<details>
<summary>Hint</summary>
Create a list to track which words you've already counted. For each word, if not already counted, count its occurrences and mark it as counted.
</details>

---

## Final Check

Before moving on, make sure you can:
- ✅ Write if/elif/else statements
- ✅ Use comparison and logical operators
- ✅ Create for loops to iterate over lists and ranges
- ✅ Create while loops with proper exit conditions
- ✅ Use break and continue in loops
- ✅ Combine conditionals and loops
- ✅ Avoid infinite loops

---

## Tips for Learning

1. **Trace through your code** - Step through each iteration mentally or with print statements.

2. **Start simple** - Get a basic loop working, then add complexity.

3. **Watch your indentation** - Python is very sensitive to indentation in loops and conditionals.

4. **Test edge cases** - What happens with empty lists? What if the condition is never met?

5. **Use print statements** - Add `print()` statements to see what's happening in your loops.

6. **Practice with real data** - Try applying these concepts to problems you care about.

---

**Great job completing Day 2! 🎉**

You've learned how to make programs that can make decisions and repeat actions. These are fundamental skills that you'll use in every program you write!

