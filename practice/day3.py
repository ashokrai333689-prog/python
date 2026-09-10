# Task 35 — Anagram

# word1 = "hello"
# word2 = "helo"
# if sorted(word1)== sorted(word2):
#     print(True)
# else:
#     print(False)


# Task 36 — Word frequency

# sentence = "python is good and python is powerful"
# words= sentence.split(" ")
# print(words)
# variable={}
# for i in words:
#     if i in variable:
#         variable[i]+=1
#     else:
#         variable[i]=1
# print(variable)


# Part 7 — 2D Lists / Matrices
# Task 37

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# for i in matrix:
#     for j in i:
#         print(j)

# Task 38 — Matrix total

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# total=0
# for i in matrix:
#     for j in i:
#         total+=j
# print(total)


# Task 39 — Diagonal

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# for i in range(len(matrix)):
#     print(matrix[i][i])

# for i in range(len(matrix)):
#     print(matrix[i][len(matrix)-1-i])


# Task 40 Count even numbers

# def count_even(numbers):
#     count=0
#     for i in numbers:
#         if i%2==0:
#             count+=1
#     return count

# result=count_even([1,2,3,4,5,6,66,90])
# print(result)



# Task 41-reverse_string

# def reverse_string(text):
#     b=text[::-1]
#     return b
# result =reverse_string("Ashok")
# print(result)


# Task 42- is_palindrome

# def is_palindrome(text):

#     return text == text[::-1]
# call=is_palindrome("madam")
# if call==True:
#     print("it is palindrome")


# Task 43- largst number
def find_largest(numbers):
    largest=0
    second_largest=0
    for i in numbers:
        
        if i>largest:
            second_largest=largest
            largest=i
        elif i != largest and ( i > second_largest):
            second_largest = i
    return second_largest, largest

a, b=find_largest([98,1011,57,88,90])
print(f'largest={b}')
print(f'secon_largest={a}')