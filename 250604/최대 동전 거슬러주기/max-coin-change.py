import sys

INT_MIN = -sys.maxsize

n, m = map(int, input().split())
coin = list(map(int, input().split()))
coin.insert(0, 0)

dp = [0] * (m + 1)

for i in range(m + 1) :
    dp[i] = INT_MIN
dp[0] = 0

for i in range(1, m + 1) : 
    for j in range(1, n + 1) : 
        if i >= coin[j] : 
            if dp[i - coin[j]] == INT_MIN:
                continue
            dp[i] = max(dp[i], dp[i - coin[j]] + 1)

if dp[m] == INT_MIN :
    print(-1)
else : 
    print(dp[m])   