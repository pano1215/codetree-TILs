a, b = map(int, input().split())

for i in range(1, 10) :
    for j in range(b, a - 1, -2) :
        if j == a :
            print(f'{j} * {i} = {i * j}', end = '')
        else :
            print(f'{j} * {i} = {i * j}', end = ' / ')
    print()