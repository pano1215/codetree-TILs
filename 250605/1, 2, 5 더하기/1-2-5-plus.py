n = int(input())
nums = [1, 2, 5]

dp = [0] * (n + 1)
dp[0] = 1

for i in range(1, n + 1) :
    for j in range(len(nums)) :
        if i >= nums[j] :
            dp[i] = dp[i] + dp[i - nums[j]]
print(dp[n] % 10007)