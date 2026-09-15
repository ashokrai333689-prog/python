# numbers = [10, 20, 30]

# for i in range(len(numbers)):
#     print(numbers[i])


# Task-47
# word = "python"

# if word == "python":
#     print("Found")



#Task-48
# numbers = [10, 20, 30]

# total = 0

# for number in numbers:
#     total += number

# print(total)


# count positive numbers
def count_positive(numberss):
    count=0
    for i in numberss:
        if i <0:
            count+=1
    return(count)

a=count_positive([-2, 3, 5, -1, 0, 8])
print(a)

# remove dublicate
def remove_dublicate(numbers):
    c=[]
    for i in numbers:
        if i not in c:
            c.append(i)
    return c

b=remove_dublicate([4, 2, 4, 1, 2, 5])
print(b)