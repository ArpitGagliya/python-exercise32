list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

a=[]
length= max(len(list1),len(list2))

for i in range(length):
    c = ""

    if i < len(list1):
        c += list1[i]

    if i < len(list2):
        c += list2[i]

    a.append(c)
print(a)