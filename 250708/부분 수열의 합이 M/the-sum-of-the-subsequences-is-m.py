import sys

n, m = map(int, input().split())
arr = list(map(int, input().split()))


max_val = sys.maxsize
dp = [0] * (m + 1)
for i in range(m + 1) : 
    dp[i] = max_val
dp[0] = 0

for i in range(n) : # 수열의 원소만큼 반복 
    for j in range(m, -1, - 1) : 
        if j >= arr[i] : 
            dp[j] = min(dp[j], dp[j - arr[i]] + 1)

if dp[m] == max_val :
    print(-1)
else : 
    print(dp[m])