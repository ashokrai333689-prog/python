# 🐍 Python Cheat Sheet — Capital One Assessment

## 1. The biggest thing to remember

You **do not need to memorise every Python syntax**.

For the assessment, focus mainly on these patterns:

**Loop → Condition → Store/Count → Return**

Example:

```python
def count_positive(numbers):
    count = 0

    for num in numbers:
        if num > 0:
            count += 1

    return count
```

Think:

> Go through each value → check something → update something → return the result.

---

# 2. Variables: `0` vs `[]` vs `{}` vs `set()`

This confused you before, so remember it like this:

| What you need               | Start with | Example          |
| --------------------------- | ---------- | ---------------- |
| Number / counter / total    | `0`        | `count = 0`      |
| List of results             | `[]`       | `result = []`    |
| Frequency / key-value pairs | `{}`       | `count = {}`     |
| Unique values / duplicates  | `set()`    | `seen = set()`   |
| Unknown value               | `None`     | `largest = None` |

### Example

If adding numbers:

```python
total = 0
total += 5
```

If collecting numbers:

```python
result = []
result.append(5)
```

❌ Wrong:

```python
result = []
result = result + 5
```

A list cannot be directly added to an integer.

---

# 3. `append()` means add something to a LIST

```python
numbers = []

numbers.append(10)
numbers.append(20)

print(numbers)
```

Result:

```python
[10, 20]
```

Remember:

```python
[] → append()
0  → +=
```

---

# 4. Value vs Index

This is one of the most important things you were confused about.

Given:

```python
numbers = [10, 20, 30]
```

### VALUE loop

```python
for i in numbers:
    print(i)
```

`i` becomes:

```text
10
20
30
```

### INDEX loop

```python
for i in range(len(numbers)):
    print(i)
```

`i` becomes:

```text
0
1
2
```

Then:

```python
numbers[i]
```

gives:

```text
10
20
30
```

### Remember

```python
for i in numbers:
```

means:

> Give me each **VALUE**.

```python
for i in range(len(numbers)):
```

means:

> Give me each **INDEX**.

---

# 5. `box[0]` means INDEX

Example:

```python
box = [50, 60, 70]
```

```python
box[0]
```

means:

> Give me the value stored at index `0`.

Result:

```python
50
```

Indexes start at:

```text
0
```

not 1.

---

# 6. Lists

```python
skills = ["Python", "SQL", "Git"]
```

Access:

```python
skills[0]
```

Result:

```text
Python
```

Last item:

```python
skills[-1]
```

Add:

```python
skills.append("FastAPI")
```

Remove by value:

```python
skills.remove("SQL")
```

Remove last item:

```python
skills.pop()
```

Change:

```python
skills[1] = "PostgreSQL"
```

Length:

```python
len(skills)
```

Check membership:

```python
if "Python" in skills:
    print("Found")
```

---

# 7. Important `.remove()` problem

This caused one of your errors.

```python
numbers.remove(5)
```

only works if `5` exists.

Otherwise:

```text
ValueError
```

Safer:

```python
if 5 in numbers:
    numbers.remove(5)
```

---

# 8. `del` and IndexError

If:

```python
skills = ["Python", "SQL", "Git"]
```

there are only indexes:

```text
0
1
2
```

So:

```python
del skills[4]
```

❌ causes:

```text
IndexError
```

Because index 4 does not exist.

---

# 9. Slicing

Given:

```python
text = "python"
```

General pattern:

```python
text[start:stop:step]
```

### First characters

```python
text[:3]
```

Result:

```text
pyt
```

### From index 2 onward

```python
text[2:]
```

Result:

```text
thon
```

### Every second character

```python
text[::2]
```

### Reverse

```python
text[::-1]
```

This is extremely useful.

---

# 10. Palindrome

A palindrome reads the same backwards.

Example:

```text
madam
racecar
```

Easy solution:

```python
def is_palindrome(text):
    return text == text[::-1]
```

Usage:

```python
result = is_palindrome("madam")

if result:
    print("Palindrome")
```

You do NOT need:

```python
if result == True:
```

This works:

```python
if result:
```

---

# 11. Functions

Basic structure:

```python
def function_name(parameter):
    # code
    return answer
```

Example:

```python
def add(a, b):
    return a + b
```

Calling it:

```python
result = add(5, 3)
print(result)
```

Think:

```text
INPUT → FUNCTION → RETURN → STORE
```

---

# 12. `return` vs `print`

Very important.

### `print()`

Shows something:

```python
print(total)
```

### `return`

Sends the answer back from the function:

```python
return total
```

Example:

```python
def add(a, b):
    return a + b

result = add(5, 2)
```

The returned `7` is stored inside:

```python
result
```

---

# 13. Returning two values

You did this with largest and second-largest.

```python
def example():
    return 10, 20
```

Store them:

```python
a, b = example()
```

Now:

```text
a = 10
b = 20
```

That's why this works:

```python
second, largest = find_largest(numbers)
```

---

# 14. Conditions

```python
if condition:
    ...
elif condition:
    ...
else:
    ...
```

Example:

```python
if age >= 18:
    print("Adult")
else:
    print("Under 18")
```

Comparison operators:

```text
>    greater than
<    less than
>=   greater than or equal
<=   less than or equal
==   equal
!=   not equal
```

Be careful:

```python
=
```

means assign.

```python
==
```

means compare.

---

# 15. `for` loop

```python
for i in numbers:
    print(i)
```

Think:

> For every item in numbers, do something.

---

# 16. `range()`

```python
for i in range(1, 6):
    print(i)
```

Result:

```text
1
2
3
4
5
```

The STOP number is not included.

So:

```python
range(1, 11)
```

gives:

```text
1 → 10
```

---

# 17. `while`

```python
number = 1

while number <= 5:
    print(number)
    number += 1
```

Always make sure something changes:

```python
number += 1
```

Otherwise you may create an infinite loop.

---

# 18. `break`

Stops the loop completely.

```python
for i in range(10):
    if i == 5:
        break
```

---

# 19. `continue`

Skip the current iteration and continue with the next one.

```python
for i in range(5):
    if i == 2:
        continue

    print(i)
```

Output:

```text
0
1
3
4
```

---

# 20. Dictionary — VERY IMPORTANT

This was one of your main areas of confusion.

```python
count = {}
```

A dictionary stores:

```text
KEY → VALUE
```

Example:

```python
count = {
    3: 2,
    5: 1
}
```

means:

```text
3 appears 2 times
5 appears 1 time
```

---

# 21. Frequency Counter Pattern ⭐

Memorise this pattern.

```python
numbers = [1, 3, 3, 2, 1, 3]

count = {}

for num in numbers:

    if num in count:
        count[num] += 1

    else:
        count[num] = 1

print(count)
```

Result:

```python
{1: 2, 3: 3, 2: 1}
```

---

# 22. Understanding `count[num] += 1`

Suppose:

```python
count = {3: 2}
```

Then:

```python
count[3]
```

means:

> Give me the VALUE belonging to key `3`.

Result:

```text
2
```

So:

```python
count[3] = count[3] + 1
```

means:

```text
count[3] = 2 + 1
```

Now:

```python
{3: 3}
```

Important:

In:

```python
count[3] = count[3] + 1
```

both `count[3]` refer to the **value stored under key 3**.

The `3` itself is the key.

---

# 23. Avoiding `KeyError`

This can cause an error:

```python
count[num] += 1
```

if `num` does not exist yet.

That's why:

```python
if num in count:
    count[num] += 1
else:
    count[num] = 1
```

is important.

---

# 24. Sets ⭐

A set stores unique values.

```python
seen = set()
```

Add:

```python
seen.add(5)
```

Check:

```python
if 5 in seen:
```

Sets are especially useful for:

```text
duplicates
Two Sum
membership checking
unique values
```

---

# 25. First Duplicate Pattern ⭐

```python
numbers = [2, 1, 3, 5, 3, 2]

seen = set()

for num in numbers:

    if num in seen:
        print(num)
        break

    seen.add(num)
```

Result:

```text
3
```

Why?

The first time `3` appears:

```text
seen = {2, 1, 3}
```

The second time `3` appears:

```python
if 3 in seen:
```

is True.

---

# 26. Remove Duplicates ⭐

```python
def remove_duplicates(numbers):

    result = []

    for num in numbers:

        if num not in result:
            result.append(num)

    return result
```

Example:

```python
remove_duplicates([4, 2, 4, 1, 2, 5])
```

Result:

```python
[4, 2, 1, 5]
```

---

# 27. Count Positive Numbers

Be careful with the condition.

Correct:

```python
def count_positive(numbers):

    count = 0

    for num in numbers:
        if num > 0:
            count += 1

    return count
```

You previously wrote:

```python
if num < 0:
```

That counts negative numbers, not positive numbers.

Always read your condition in English:

```python
num > 0
```

means:

> Is the number greater than zero?

---

# 28. Find Largest Number

```python
def find_largest(numbers):

    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num

    return largest
```

---

# 29. Second Largest ⭐

You understood this pattern well after practising it.

```python
def find_largest(numbers):

    largest = float("-inf")
    second_largest = float("-inf")

    for num in numbers:

        if num > largest:
            second_largest = largest
            largest = num

        elif num != largest and num > second_largest:
            second_largest = num

    return second_largest, largest
```

Then:

```python
second, largest = find_largest([98, 1011, 57, 88, 90])

print(f"Largest = {largest}")
print(f"Second largest = {second}")
```

### Important logic

When a NEW largest appears:

```python
second_largest = largest
largest = num
```

The old largest becomes the second-largest.

---

# 30. Why starting largest at `0` can be dangerous

This:

```python
largest = 0
```

works for:

```python
[4, 10, 3]
```

But fails for:

```python
[-10, -5, -2]
```

because `0` isn't even in the list.

Safer:

```python
largest = numbers[0]
```

or:

```python
largest = float("-inf")
```

---

# 31. Two Sum ⭐⭐⭐

One of the most useful CodeSignal patterns.

Problem:

```text
numbers = [2, 7, 11, 15]
target = 9
```

Need:

```text
2 + 7 = 9
```

Simple version:

```python
for i in range(len(numbers)):

    for j in range(i + 1, len(numbers)):

        if numbers[i] + numbers[j] == target:
            return i, j
```

Remember:

```text
i = first index
j = second index
```

---

# 32. Better Two Sum with Dictionary

Useful if you remember it:

```python
def two_sum(numbers, target):

    seen = {}

    for i, num in enumerate(numbers):

        needed = target - num

        if needed in seen:
            return seen[needed], i

        seen[num] = i
```

Think:

```text
Target = 9
Current number = 7

What do I need?

9 - 7 = 2
```

Then check:

```python
if 2 in seen:
```

---

# 33. Move Zeros

Example:

```python
[0, 1, 0, 3, 12]
```

Wanted:

```python
[1, 3, 12, 0, 0]
```

Simple approach:

```python
result = []
zeros = 0

for num in numbers:

    if num == 0:
        zeros += 1
    else:
        result.append(num)

result.extend([0] * zeros)
```

---

# 34. Most Frequent Number ⭐

Use the dictionary frequency pattern.

```python
numbers = [1, 2, 2, 3, 2, 1]

count = {}

for num in numbers:

    if num in count:
        count[num] += 1
    else:
        count[num] = 1
```

Then find which key has the largest value.

Useful shortcut:

```python
max(count, key=count.get)
```

But understanding the dictionary pattern is more important than memorising the shortcut.

---

# 35. Anagram ⭐

Anagrams contain the same characters.

Example:

```text
listen
silent
```

Easy solution:

```python
def is_anagram(a, b):
    return sorted(a) == sorted(b)
```

---

# 36. Strings

Useful methods:

```python
text.lower()
text.upper()
text.strip()
text.split()
```

Length:

```python
len(text)
```

Membership:

```python
if "a" in text:
```

---

# 37. Counting vowels

```python
def count_vowels(text):

    count = 0

    for char in text.lower():

        if char in "aeiou":
            count += 1

    return count
```

Pattern:

```text
loop characters → check membership → count
```

---

# 38. FizzBuzz

```python
for num in range(1, 101):

    if num % 15 == 0:
        print("FizzBuzz")

    elif num % 3 == 0:
        print("Fizz")

    elif num % 5 == 0:
        print("Buzz")

    else:
        print(num)
```

Important:

Check `15` before `3` and `5`.

---

# 39. Modulo `%`

```python
10 % 2
```

gives:

```text
0
```

Meaning there is no remainder.

Even number:

```python
if num % 2 == 0:
```

Odd:

```python
if num % 2 != 0:
```

---

# 40. Common CodeSignal Thinking Process ⭐⭐⭐

When you see a question, DON'T immediately code.

First ask:

### Step 1

What is the input?

```text
list?
string?
number?
```

### Step 2

What do I need to return?

```text
number?
list?
True/False?
index?
```

### Step 3

Do I need to examine every item?

Usually:

```python
for item in something:
```

### Step 4

What am I storing?

Count:

```python
count = 0
```

List:

```python
result = []
```

Duplicates:

```python
seen = set()
```

Frequency:

```python
frequency = {}
```

Largest:

```python
largest = numbers[0]
```

### Step 5

Write the condition.

```python
if ...
```

### Step 6

Update your stored value.

```python
count += 1
```

or

```python
result.append(item)
```

### Step 7

Return.

```python
return result
```

---

# 41. The 5 patterns you should recognise immediately ⭐⭐⭐

## Pattern 1 — Count

```python
count = 0

for x in items:
    if condition:
        count += 1

return count
```

Used for:

* vowels
* positive numbers
* even numbers
* matching items

---

## Pattern 2 — Build a result list

```python
result = []

for x in items:
    if condition:
        result.append(x)

return result
```

Used for:

* filtering
* removing duplicates
* moving values
* collecting results

---

## Pattern 3 — Frequency Dictionary

```python
count = {}

for x in items:

    if x in count:
        count[x] += 1

    else:
        count[x] = 1
```

Used for:

* most frequent number
* character frequency
* duplicate counting
* anagrams

---

## Pattern 4 — Seen Set

```python
seen = set()

for x in items:

    if x in seen:
        # duplicate found

    seen.add(x)
```

Used for:

* first duplicate
* duplicates
* fast membership checking

---

## Pattern 5 — Largest / Best So Far

```python
largest = items[0]

for x in items:

    if x > largest:
        largest = x

return largest
```

Used for:

* largest
* smallest
* second-largest
* best score

---

# 42. Common mistakes YOU should watch for ⚠️

### Mistake 1

```python
if num < 0:
```

when the question says positive.

Read the condition carefully.

---

### Mistake 2

Confusing:

```python
[]
```

with:

```python
0
```

Remember:

```text
[] = collect things
0 = count/add things
```

---

### Mistake 3

Confusing INDEX and VALUE.

```python
for x in numbers:
```

`x` is normally the value.

---

### Mistake 4

Using an index that doesn't exist.

Remember:

```python
len(numbers) - 1
```

is the last valid positive index.

---

### Mistake 5

Dictionary key does not exist yet.

Don't immediately do:

```python
count[x] += 1
```

Use:

```python
if x in count:
```

first.

---

### Mistake 6

Forgetting `return`.

CodeSignal functions normally need something like:

```python
return answer
```

Printing is usually not enough.

---

### Mistake 7

Changing the wrong variable.

For second largest:

```python
second_largest = largest
largest = num
```

Order matters.

---

### Mistake 8

Starting largest at `0`.

This fails with negative numbers.

Use:

```python
largest = numbers[0]
```

---

# 43. Debugging checklist

If your program gives an error, don't panic.

Check:

### `TypeError`

Usually:

> I'm combining incompatible things.

Example:

```python
[] + 5
```

---

### `IndexError`

Usually:

> That list position does not exist.

---

### `KeyError`

Usually:

> That dictionary key hasn't been created.

---

### `ValueError`

Often:

> I'm trying to remove/find/convert something that isn't valid.

Example:

```python
numbers.remove(10)
```

when 10 isn't present.

---

# 44. Before submitting a CodeSignal solution

Test these cases whenever possible:

```text
normal case
one item
duplicates
zeros
negative numbers
already sorted
all same values
empty input — if allowed
```

Example:

If finding largest, test:

```python
[5, 10, 2]
```

and:

```python
[-10, -2, -30]
```

---

# 45. Your priority before Capital One

Don't try to learn dozens of new Python topics now.

Your highest priority is:

**1. Lists**

```python
append()
indexing
loops
membership
```

**2. Strings**

```python
slicing
[::-1]
characters
```

**3. Dictionaries**

```python
frequency counting
```

**4. Sets**

```python
duplicate detection
```

**5. Functions**

```python
parameters
return
```

**6. Problem patterns**

```text
count
filter
duplicates
frequency
largest/second-largest
Two Sum
palindrome
anagram
```

**7. Debugging**

Understand:

```text
TypeError
IndexError
KeyError
ValueError
```

---

# 46. Ultra-short memory card 🧠

If you forget everything else, remember this:

```python
# COUNT
count = 0
count += 1
```

```python
# COLLECT
result = []
result.append(x)
```

```python
# UNIQUE / DUPLICATES
seen = set()
seen.add(x)

if x in seen:
    ...
```

```python
# FREQUENCY
freq = {}

if x in freq:
    freq[x] += 1
else:
    freq[x] = 1
```

```python
# LOOP VALUES
for x in numbers:
```

```python
# LOOP INDEXES
for i in range(len(numbers)):
```

```python
# REVERSE
text[::-1]
```

```python
# EVEN
x % 2 == 0
```

```python
# RETURN
return answer
```

---

# 47. Assessment rule

When you're stuck:

**Don't ask “What syntax do I need?” first.**

Ask:

> “What needs to happen to each value?”

For example:

**Find first duplicate**

Think:

```text
Take number
↓
Have I seen it before?
↓
YES → return it
NO → remember it
```

Then translate that into:

```python
seen = set()

for num in numbers:

    if num in seen:
        return num

    seen.add(num)
```

That is exactly the type of thinking you should practise.

---

# Final focus

You already understand more of the concepts than you sometimes think you do. Your main weakness right now is **recalling syntax quickly and choosing the correct pattern**, not understanding what programming is.

For the assessment, your job is therefore:

```text
Recognise pattern
↓
Choose storage
↓
Loop
↓
Condition
↓
Update
↓
Return
↓
Test
```

**Storage shortcut:**

```text
Need a count?       → 0
Need results?       → []
Need frequencies?   → {}
Need duplicates?    → set()
Need best value?    → first item / -infinity
```
