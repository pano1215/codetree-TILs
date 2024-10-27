n = int(input())

cnt = 0
while n % 5 != 0 and n > 1 :# 5의 배수가 되도록 만들기 위함
    n -= 2
    cnt += 1
    #print('n :', n)

cnt += (n // 5)
n = n % 5

if n != 0 :
    print(-1)
else :
    print(cnt)