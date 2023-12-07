n = int(input())

for i in range(1, (n * 2)+1):
    if i % 2 == 0 : # 홀수인 경우  
        for j in range((i // 2)) :
            print('*', end = ' ')
        print()
    else : # 짝수인 경우 
        for j in range(n - (i // 2)) :
            print('*', end = ' ')
        print()