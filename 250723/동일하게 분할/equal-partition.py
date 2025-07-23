import sys
n = int(input())
arr = list(map(int, input().split()))

total_sum = sum(arr)

if total_sum % 2 != 0:
    print('No')
    sys.exit()

avg_sum = total_sum // 2

dp = [False] * (avg_sum + 1)
dp[0] = True

for num in arr :
    for i in range(avg_sum, num - 1, -1) :
        dp[i] |= dp[i - num]
        #print(dp)

if not dp[avg_sum]:
    print('No')
else : 
    print('Yes')
