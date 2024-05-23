number=int(input("enter a number : "))
a=0
b=2
for i in range(1,number+1):
    a += b
    b = b * 10 + 2
print(a)