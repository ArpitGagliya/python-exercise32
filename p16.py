numbers = [1, 2, 3, 4, 5, 6, 7]

a=[]
for i in range(len(numbers)):
    a.append(numbers[i] * numbers[i])
print(a)