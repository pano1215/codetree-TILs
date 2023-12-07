n = int(input())

for i in range(1, (n * 2) + 2) :
    if i % 2 == 1 : #홀수인 경우
        for j in range((n * 2) + 1) :
            print('*', end = ' ')
        print()
    else :
        for j in range((n * 2) + 1) : # 0~7
            if j % 2 == 0 :
                print('*', end = ' ')
            else :
                print(' ', end = ' ')
        print()