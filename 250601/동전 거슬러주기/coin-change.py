import sys 

n, m = map(int, input().split())
coin = list(map(int, input().split()))

dp = [0] * (m + 1)
coin.insert(0, 0)
max_val = sys.maxsize

for i in range(m + 1) : 
    dp[i] = max_val
dp[0] = 0

for i in range(1, m + 1) :
    for j in range(1, n + 1) : 
        if i >= coin[j] :
            if dp[i - coin[j]] == max_val :
                continue

            dp[i] = min(dp[i], dp[i - coin[j]] + 1)
#print(dp)
if dp[m] == max_val :
    print(-1)
else : 
    print(dp[m])