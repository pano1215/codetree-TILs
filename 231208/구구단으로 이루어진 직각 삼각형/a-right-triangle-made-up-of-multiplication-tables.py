n = int(input())

cnt = n
for i in range(1, 1+ n) :
    for j in range(1, n+1):
        if j > n - i +1 :
            print(' ', end = ' ')
        else :
            if j == n - i +1 :
                print(f'{i} * {j} = {i*j}', end = '')
            else : 
                print(f'{i} * {j} = {i*j}', end = ' / ')
        cnt -= 1
    print()