import sys

n, m = map(int, input().split()) # 원소 수, 합 
arr = list(map(int, input().split()))

max_size = sys.maxsize
dp = [max_size for _ in range(m + 1)]
dp[0] = 0  

for i in range(n) : 
    for j in range(m, -1, -1) : 
        if j >= arr[i] : 
            dp[j] = min(dp[j], dp[j - arr[i]] + 1)

if dp[m] == max_size : 
    print(-1)
else : 
    print(dp[m])