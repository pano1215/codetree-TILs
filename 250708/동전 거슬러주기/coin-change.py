import sys

n, m = map(int, input().split()) # 동전수, 금액 
coin = [0] + list(map(int, input().split()))

min_num = sys.maxsize

dp = [0] * (m + 1)
for i in range(len(dp)) : 
    dp[i] = min_num
dp[0] = 0 

for i in range(1, m + 1) : # 금액 
    for j in range(1, n + 1) : # 동전수 
        if i >= coin[j] : 
            dp[i] = min(dp[i], dp[i - coin[j]] + 1)

if dp[m] == min_num :
    print(-1)
else : 
    print(dp[m])

