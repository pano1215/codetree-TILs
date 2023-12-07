n = int(input())
# 0 6
# 1 3
# 2 2
# 3 2
# 4 1
# 5 1

for i in range(n): # 행
    for j in range(n): # 열
        if j % 2 == 0 : #열이 짝수인 경우
            if i == 0 :
                print('*', end = ' ')
            else :
                print(' ', end = ' ')
        else : 
            if j >= i :
                print('*', end = ' ')
            else :
                print(' ', end = ' ')
    print()