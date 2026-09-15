
# number=[5,9,12]
# for i in range(len(number)):
#     print(i)
#     print(number[i])

# numbers = [2, 5, 3, 5, 8, 2]

# a=[]
# for i in numbers:
#     if i in a:
#         print(f'{i} is the first dublicate number')
#         break
#     else:
#         a.append(i)
# Return the first duplicate number.
# Expected: 5


numbers = [2, 4, 2, 5, 4, 2]
store={}
# Count how many times each number appears.
# Expected:
# {2: 3, 4: 2, 5: 1}
# for i in numbers:
#     if i in store:
#         store[i]+=1
#     else:
#         store[i]=1
# print(store)



numbers = [4, 2, 4, 1, 2, 4, 3, 2]

# Task:
# 1. Create a dictionary called frequency
# 2. Count how many times each number appears
# 3. Print the dictionary
# 4. Then loop through the dictionary using .items()
#    and print like:
#    4 appears 3 times

# a={}
# for i in numbers:
#     if i in a:
#         a[i]+=1
#     else:
#         a[i]=1
# print(a)
# for key,value in a.items():
#     print(key,value)

# Given a 2D list (matrix), return the sum of all numbers.


matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
# count=0
# total=0
# largest_number=0
# for row in matrix:
#     for i in row:
#         total+=i
#         if i>largest_number:
#             largest_number=i
#         if i % 2 == 0:
#             count += 1
# print(total)
# print(f'largest number is {largest_number}')
# print(count)

def find_even_numbers(numbers):
    even_numbers=[]
    for i in numbers:
        if i%2==0:
            even_numbers.append(i)
    return even_numbers
even=find_even_numbers([2,4,5,6,8,10,15,19,23])
print(even)