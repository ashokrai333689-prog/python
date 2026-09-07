# Practice: Removing items from a list using remove(), pop(), and del

skills = ["Python", "SQL", "Java", "Git", "React", "C++"]

skills.remove("Java")
skills.pop()
del skills[3]
print (skills)
for i in skills:
    print(i)


# Practice: Sorting numbers in ascending and descending order
numbers = [45, 12, 78, 3, 56, 21]

numbers.sort()
print (numbers)
numbers.sort(reverse=True)
print(numbers)


# Practice: Reversing a list and then sorting names alphabetically
names = ["Ashok", "Sam", "John", "David"]

names.reverse()
print(names)
names.sort()
print(names)


# Practice: Adding, removing, sorting, counting, and looping through list items
scores = [65, 82, 49, 91, 73]


scores.append(88)
scores.remove(49)
print(scores)
scores.sort(reverse=True)
print(scores)
print(f'there are {len(scores)} scores in the list')
for i in scores:
    print(i)


# Practice: Finding the index of an item and counting repeated items in a list
languages = ["Python", "Java", "Python", "C++", "SQL", "Python"]

print(languages.index("C++"))
print(languages.count("Python"))
print(f'Python appears {languages.count("Python")} times')


# Practice: Finding the minimum, maximum, and total of numbers in a list
marks = [72, 85, 61, 90, 77]

print(min(marks))
print(max(marks))
print(sum(marks))
print(f'The highes marks is {max(marks)}')


# Practice: Copying a list and showing that changes to the copy do not affect the original list
languages = ["Python", "Java", "C++"]

copied_languages= languages.copy()
print(copied_languages)
copied_languages.append("SQL")
print(copied_languages)
print(languages)


# Practice: Accessing items inside a nested list using indexes
students = [
    ["Ashok", 85],
    ["John", 72],
    ["Sam", 90]
]


print(students[1])
print(students[1][1])
print(students[2][0])
print(students[0][1])



# Practice: Combining common list operations in one exercise
skills = ["Python", "SQL", "Git", "React", "Python"]


print(f'there are {len(skills)} skills in the list')
print(f'Python appears {skills.count("Python")} times in the list')
skills.append("FASTAPI")
print(skills)
skills.remove("React")
print(skills)
skills.sort()
print(skills)
for i in skills:
    print(i)


