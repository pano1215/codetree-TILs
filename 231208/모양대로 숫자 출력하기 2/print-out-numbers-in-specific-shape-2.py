n = int(input())

cnt = 1
for i in range(n) :
    for j in range(n) :
        print(cnt * 2, end = ' ')
        cnt += 1
        if cnt == 5 :
            cnt = 1
    print()