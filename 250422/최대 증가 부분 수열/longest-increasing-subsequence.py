import sys

n = int(input())
arr = list(map(int, input().split()))

min_val = -sys.maxsize
dp = [0] * n

for i in range(1, n) : 
    for j in range(i) : 

        if arr[j] < arr[i] : 
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp) + 1)