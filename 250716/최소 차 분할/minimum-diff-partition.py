n = int(input())
arr = list(map(int, input().split()))

total_sum = sum(arr)
max_sum = total_sum // 2
dp = [False] * (max_sum + 1)
dp[0] = True

for num in arr : 
    for i in range(max_sum, num - 1, -1) : 
        dp[i] |= dp[i - num]

min_val = max_sum
for i in range(len(dp)) : 
    if dp[i] : 
        temp_min_val = total_sum - i * 2
    min_val = min(min_val, temp_min_val)
print(min_val)
