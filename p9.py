start=int(input("enter a starting point : "))
end=int(input("enter a ending point : "))

for i in range(start,end+1,1):
    for j in range(2,end+1,1):
        if i%j == 0:
            break
        elif i==j+1 :
            print(i)
