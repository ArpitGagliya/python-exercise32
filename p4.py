number = [12, 75, 150, 180, 145, 525, 50]

for a in number:
    if a % 5 == 0:
        if a > 500:
            break
        elif a > 150:
            continue
        else:
            print(a)