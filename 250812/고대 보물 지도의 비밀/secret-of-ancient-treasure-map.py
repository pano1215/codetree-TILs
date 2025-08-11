n, k = map(int, input().split())
numbers = [0] + list(map(int, input().split()))

dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(1, n + 1) : 
    dp[i][i] = numbers[i]


for i in range(1, n + 1) : 
    minus_cnt = 0 
    for j in range(i, n + 1) : 
        if numbers[j] < 0 : 
            minus_cnt += 1

        if minus_cnt > k :
            break
        
        dp[i][j] = dp[i][j - 1] + numbers[j]

result = 0 
for i in range(n + 1) :
    result = max(result, max(dp[i]))
print(result)
        
        



        