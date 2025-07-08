import sys

n, m = map(int, input().split()) # 동전 수, 합 
coin = list(map(int, input().split()))

min_num = -sys.maxsize
dp = [min_num for _ in range(m + 1)]
dp[0] = 0

for i in range(1, m + 1) : # 금액
    for j in range(n) : # 동전 
        if i >= coin[j] : 
            #if dp[i] == min_num : continue 
            dp[i] = max(dp[i], dp[i - coin[j]] + 1)

if dp[m] == min_num : 
    print(-1)
else :
    print(dp[m])