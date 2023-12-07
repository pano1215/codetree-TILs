n = int(input())

cnt = n
for i in range(1, n+1) :
    for j in range(n) :
        if j % 2 == 0 :
            print(i, end = '')
        else :
            print(cnt, end = '')
    cnt -= 1
    print()