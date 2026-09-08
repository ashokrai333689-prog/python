skills = ["Python", "SQL", "Git"]
skills.append('FastAPI')
print(skills)
print(skills[0])
print(skills[-1])

# for i in range(1,5+1):
#     print(i)

# numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,30,40,50,68,98,44]
# for a in numbers:
#     if a%2==0 and 1<=a<=20:
#         print(a)

# numbers = [10, 25, 7, 40, 13]
# for i in numbers:
#     if i>15:
#         print(i)

# numbers = [5, 10, 15, 20]
# print(sum(numbers))
# box=0
# for i in numbers:
#     box=box+i
# print(box)

# numbers = [17, 4, 29, 10, 35, 2]
# box1=0
# for a in numbers:
#     if a>box1:
#         box1=a
# print(box1)



# Task 9 — Count even numbers
# numbers = [1, 4, 7, 10, 14, 21, 24]
# count=0
# for i in numbers:
#     if i%2==0:
#         count+=1
# print (f'there are {count} even numvers.')

# Task 10 — Create a new list of even numbers
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# even=[]
# for i in numbers:
#     if i%2==0:
#         even.append(i)
# print(even)


# Task 11 — Find a target
# numbers = [12, 7, 25, 18, 30]
# target = 100
# if target in numbers:
#     print("found")
# else: print("not found")

# Task 12 — Find position
# numbers = [12, 7, 25, 18, 30]
# print(numbers.index(18))

# Task 13 — Remove duplicates
# numbers = [1, 2, 2, 3, 4, 4, 5]
# num=[]
# for i in numbers:
#     if i in num:
#         continue
#     else:
#         num.append(i)
# print(num)

# Task 14 — Count characters
# word = "programming"
# print(len(word))

# Task 15 — Reverse a string
# a="python"
# print(a[::-1])

# Task 16 — Count vowels
# word = "assessment"
# vowels=["a","e","i","o","u"]
# count=0
# for i in word:
#     if i in vowels:
#         count+=1
# print(count)


# Task 17 — Palindrome
# a="racecar"
# if a==a[::-1]:
#     print(True)
# else:
#     print(False)


# b="Python"
# if b==b[::-1]:
#     print(True)
# else:
#     print(False)



# Task 18 — Count a specific character
# word = "banana"
# letter = "a"
# count=0
# for i in word:
#     if i == letter:
#         count+=1
# print(count)

# print(word.count(letter))

# Task 19 — Longest word
# words = ["cat", "elephant", "dog", "giraffe"]
# c=""
# for i in words:
#     if len(i)>len(c):
#         c=i
# print(c)

# Part 4 — Dictionaries

# Task 20
# student = {
#     "name": "Ashok",
#     "score": 90
# }
# print(student["name"])
# print(student["score"])
# student["course"]= "AI"
# print(student)
# for key,value in student.items():
#     print(key,value)

numbers = [1, 2, 2, 3, 3, 3]
number={}

for i in numbers:
    if i in numbers:
        number[i]+=1
    else:
        number[i]=1