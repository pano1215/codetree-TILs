n, m = map(int, input().split()) # 원소 수, 합 
arr = list(map(int, input().split()))

dp = [False for _ in range(m + 1)]
dp[0] = True

for i in range(n) : 
    for j in range(m, -1, -1) : 
        if j >= arr[i] and dp[j - arr[i]] :
            dp[j] = True 

if dp[m] :
    print('Yes')
else : 
    print('No')
# print(dp[m])
