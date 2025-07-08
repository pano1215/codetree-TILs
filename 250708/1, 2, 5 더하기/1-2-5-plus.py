n = int(input())
arr = [1, 2, 5]

dp = [0 for _ in range(n + 1)]
dp[0] = 1

for i in range(n + 1) : 
    for j in range(len(arr)) : 
        if i >= arr[j] :
            dp[i] = dp[i] + dp[i - arr[j]]

if dp[n] == 0 :
    print(-1)
else : 
    print(dp[n] % 10007)