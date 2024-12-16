k, n = map(int, input().split())
temp = []

def stat(num) :
    if len(temp) == n :
        for num in temp :
            print(num, end = ' ')
        print()
        return 

    for i in range(1, k + 1) :
        if len(temp) >= 2 and temp[-1] == temp[-2] == i :
            continue

        temp.append(i)
        stat(i + 1)
        temp.pop()

stat(1)