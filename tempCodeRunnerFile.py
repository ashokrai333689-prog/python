scores.append(88)
scores.remove(49)
print(scores)
scores.sort(reverse=True)
print(scores)
print(f'there are {len(scores)} scores in the list')
for i in scores:
    print(i)