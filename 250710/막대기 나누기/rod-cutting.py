n = int(input())
profit = list(map(int, input().split()))
idx = list(range(1, len(profit) + 1))

dp = [0] * (n + 1)

for i in range(n) : # 나무숫자 
    for j in range(1, n + 1) : # 나무길이
        if j - idx[i] >= 0 :
            dp[j] = max(dp[j], dp[j - idx[i]] + profit[i])  
            #print(i, j, dp, j - idx[i])

print(max(dp))