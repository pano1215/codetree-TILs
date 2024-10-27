n = int(input())

coin = [5, 2]
coin_cnt = 0

while n % 5 != 0 and n > 0 :
    n -= 2
    coin_cnt += 1

# 5의 배수가 됐다는 것
coin_cnt = coin_cnt + (n // 5)

if n < 0 :
    print(-1)
else : 
    print(coin_cnt)