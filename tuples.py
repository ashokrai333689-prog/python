fruits = ("apple", "banana", "orange", "mango", "grape")


print(fruits[0])
print(fruits[2])
print(fruits[-1])
print(f'there are {len(fruits)} in tuple')


skills = ["Python", "SQL", "Git"]



skills.append("FastAPI")
print(skills)
skills.sort()
print(skills)
print(f'there are {len(skills)} skills in the list')
for i in skills:
    print(i)